def superponer_prenda(img, prenda_path, y_offset=0, scale=1.0):
    """Superpone una prenda PNG sobre la imagen base."""
    prenda = cv2.imread(prenda_path, cv2.IMREAD_UNCHANGED)
    if prenda is None:
        return img
    # Redimensionar prenda al ancho de la imagen base
    prenda_w = int(img.shape[1] * scale)
    prenda_h = int(prenda.shape[0] * prenda_w / prenda.shape[1])
    prenda = cv2.resize(prenda, (prenda_w, prenda_h), interpolation=cv2.INTER_AREA)
    # Coordenadas para superponer
    x_offset = (img.shape[1] - prenda_w) // 2
    y_offset = y_offset
    # Separar canales
    if prenda.shape[2] == 4:
        alpha = prenda[:,:,3] / 255.0
        for c in range(3):
            y1 = y_offset
            y2 = y_offset + prenda_h
            x1 = x_offset
            x2 = x_offset + prenda_w
            if y2 > img.shape[0]:
                y2 = img.shape[0]
            if x2 > img.shape[1]:
                x2 = img.shape[1]
            img[y1:y2, x1:x2, c] = (1 - alpha[:y2-y1, :x2-x1]) * img[y1:y2, x1:x2, c] + alpha[:y2-y1, :x2-x1] * prenda[:y2-y1, :x2-x1, c]
    return img
import cv2
import cv2.data
import dlib
import numpy as np
import os

MODELS_DIR = "models"
LANDMARKS_PATH = os.path.join(MODELS_DIR, "shape_predictor_68_face_landmarks.dat")
GENDER_PROTO = os.path.join(MODELS_DIR, "gender_deploy.prototxt")
GENDER_MODEL = os.path.join(MODELS_DIR, "gender_net.caffemodel")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Manejo seguro de dlib.shape_predictor
if hasattr(dlib, "shape_predictor"):
    landmark_predictor = dlib.shape_predictor(LANDMARKS_PATH) # type: ignore
else:
    raise ImportError("dlib no tiene el atributo 'shape_predictor'. Verifica la instalación de dlib y el archivo de modelo.")

gender_net = cv2.dnn.readNetFromCaffe(GENDER_PROTO, GENDER_MODEL)
GENDER_LIST = ['Hombre', 'Mujer']

def analizar_imagen(image_path):
    resultado = {
        "color_ojos": "desconocido",
        "forma_cara": "desconocido",
        "genero": "desconocido",
        "peinado": "desconocido",
        "imagen_atuendo": None
    }
    img = cv2.imread(image_path)
    if img is None:
        print("No se pudo leer la imagen:", image_path)
        return resultado

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    if len(faces) == 0:
        print("No se detectó ningún rostro.")
        return resultado

    x, y, w, h = faces[0]
    face_img = img[y:y+h, x:x+w].copy()
    face_rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h)) # type: ignore

    # Superposición de prenda (si existe PNG de prenda)
    prendas_dir = os.path.join(os.path.dirname(__file__), 'static', 'prendas')
    if os.path.exists(prendas_dir):
        # Ejemplo: elige una prenda por género
        if resultado["genero"] == "Hombre":
            prenda_file = "camiseta_azul.png"
        else:
            prenda_file = "blusa_blanca.png"
        prenda_path = os.path.join(prendas_dir, prenda_file)
        if os.path.exists(prenda_path):
            img_con_prenda = superponer_prenda(img.copy(), prenda_path, y_offset=y+h, scale=0.7)
            out_path = image_path.replace('.jpg', '_atuendo.jpg').replace('.png', '_atuendo.png')
            cv2.imwrite(out_path, img_con_prenda)
            resultado["imagen_atuendo"] = out_path

    # Género
    try:
        blob = cv2.dnn.blobFromImage(face_img, 1.0, (227, 227), (78.426, 87.768, 114.895), swapRB=False)
        gender_net.setInput(blob)
        gender_preds = gender_net.forward()
        resultado["genero"] = GENDER_LIST[gender_preds[0].argmax()]
    except Exception as e:
        print("Error en la detección de género:", e)

    # Landmarks
    try:
        shape = landmark_predictor(gray, face_rect)
        landmarks = np.array([[p.x, p.y] for p in shape.parts()])
    except Exception as e:
        print("Error en la detección de landmarks:", e)
        return resultado

    # Color de ojos
    try:
        left_eye_pts = landmarks[36:42]
        right_eye_pts = landmarks[42:48]
        left_eye_img = img[
            np.min(left_eye_pts[:,1]):np.max(left_eye_pts[:,1]),
            np.min(left_eye_pts[:,0]):np.max(left_eye_pts[:,0])
        ]
        right_eye_img = img[
            np.min(right_eye_pts[:,1]):np.max(right_eye_pts[:,1]),
            np.min(right_eye_pts[:,0]):np.max(right_eye_pts[:,0])
        ]
        def eye_color(eye_img):
            if eye_img.size == 0:
                return None
            mean = np.mean(eye_img.reshape(-1, 3), axis=0)
            brightness = np.mean(mean)
            return "claro" if brightness > 100 else "oscuro"
        color_ojos = eye_color(left_eye_img) or eye_color(right_eye_img)
        resultado["color_ojos"] = color_ojos if color_ojos else "desconocido"
    except Exception as e:
        print("Error en la detección de color de ojos:", e)

    # Forma de cara
    try:
        jaw = landmarks[0:17]
        jaw_width = np.linalg.norm(jaw[0] - jaw[-1])
        face_height = np.linalg.norm(landmarks[8] - landmarks[27])
        ratio = jaw_width / face_height
        if ratio < 0.8:
            resultado["forma_cara"] = "alargada"
        elif ratio < 1.0:
            resultado["forma_cara"] = "ovalada"
        elif ratio < 1.2:
            resultado["forma_cara"] = "redonda"
        else:
            resultado["forma_cara"] = "cuadrada"
    except Exception as e:
        print("Error en la detección de forma de cara:", e)

    # Peinado
    try:
        brow_y = np.mean(landmarks[19:27,1])
        hairline_y = y
        if brow_y - hairline_y > h * 0.25:
            resultado["peinado"] = "largo o recogido"
        else:
            resultado["peinado"] = "corto"
    except Exception as e:
        print("Error en la detección de peinado:", e)

    return resultado