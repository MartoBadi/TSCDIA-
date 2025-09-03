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
    landmark_predictor = dlib.shape_predictor(LANDMARKS_PATH)
else:
    raise ImportError("dlib no tiene el atributo 'shape_predictor'. Verifica la instalación de dlib y el archivo de modelo.")

gender_net = cv2.dnn.readNetFromCaffe(GENDER_PROTO, GENDER_MODEL)
GENDER_LIST = ['Hombre', 'Mujer']

def analizar_imagen(image_path):
    resultado = {
        "color_ojos": "desconocido",
        "forma_cara": "desconocido",
        "genero": "desconocido",
        "peinado": "desconocido"
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
    face_rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))

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