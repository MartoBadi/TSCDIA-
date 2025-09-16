import os
from diffusers.pipelines.pipeline_utils import DiffusionPipeline
from PIL import Image
import numpy as np
import urllib.request
import torch
import threading
import time
import streamlit as st
import cv2

# Variable global para detener el hilo
detener_hilo = False

def mostrar_tiempo():
    global detener_hilo
    inicio = time.time()
    while not detener_hilo:
        transcurrido = int(time.time() - inicio)
        print(f"Tiempo desde inicio: {transcurrido} segundos", end='\r')
        time.sleep(1)

# Detener el hilo al cerrar el programa
try:
    threading.Thread(target=mostrar_tiempo, daemon=True).start()
except KeyboardInterrupt:
    detener_hilo = True

MODELS_DIR = 'models'
os.makedirs(MODELS_DIR, exist_ok=True)

MODELOS = {
    'haarcascade_frontalface_default.xml': 'https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml',
    'gender_deploy.prototxt': 'https://github.com/spmallick/learnopencv/raw/master/AgeGender/gender_deploy.prototxt',
    'gender_net.caffemodel': 'https://www.dropbox.com/s/iyv483wz7ztr9gh/gender_net.caffemodel?dl=1',
}

def descargar_modelos():
    for nombre, url in MODELOS.items():
        ruta = os.path.join(MODELS_DIR, nombre)
        if not os.path.exists(ruta):
            print(f'Descargando {nombre}...')
            urllib.request.urlretrieve(url, ruta)
            print(f'{nombre} descargado.')
        else:
            print(f'{nombre} ya existe.')

descargar_modelos()

_pipe_cache = None

def get_pipe():

    global _pipe_cache
    print("[LOG] get_pipe: Iniciando carga del modelo img2img...")
    if _pipe_cache is None:
        print("[LOG] get_pipe: Cargando modelo img2img desde ruta local...")
        ruta = "/tmp/models--stable-diffusion-v1-5--stable-diffusion-v1-5"
        if os.path.exists(ruta):
            _pipe_cache = DiffusionPipeline.from_pretrained(
        r"/tmp/models--stable-diffusion-v1-5--stable-diffusion-v1-5",
            torch_dtype=torch.float32, low_cpu_mem_usage=True, 
        ).to("cpu")
        else:
            _pipe_cache = DiffusionPipeline.from_pretrained(
        r"stable-diffusion-v1-5/stable-diffusion-v1-5",
            torch_dtype=torch.float32, low_cpu_mem_usage=True, cache_dir="/tmp"
        ).to("cpu")
        print("[LOG] get_pipe: Modelo img2img cargado.")
    else:
        print("[LOG] get_pipe: Usando modelo img2img en caché.")
    return _pipe_cache

def generar_imagen_ia_streamlit(prompt, output_path, input_image):
    try:
        print("[LOG] generar_imagen_ia_streamlit: Iniciando generación de imagen IA img2img...")
        pipe = get_pipe()
        print("[LOG] generar_imagen_ia_streamlit: Modelo img2img obtenido.")

        # Generar un prompt dinámico basado en características
        if not prompt:
            prompt = generar_prompt_dinamico(input_image)
            print(f"[LOG] Prompt generado automáticamente: {prompt}")

        # Llamar al pipeline con los parámetros necesarios
        result = pipe(prompt=prompt, image=input_image, num_inference_steps=50, guidance_scale=7.5)
        print("[LOG] Después de llamar al pipeline img2img...")

        # Asegurarse de que el resultado contiene imágenes
        if hasattr(result, "images") and isinstance(result.images, list) and len(result.images) > 0:
            img = result.images[0]  # Obtener la primera imagen generada
            print(f"[LOG] generar_imagen_ia_streamlit: img type={type(img)}")
            
            # Guardar la imagen generada
            img.save(output_path)
            print(f"[LOG] generar_imagen_ia_streamlit: Imagen guardada en {output_path}")
            return output_path
        else:
            print("[LOG] generar_imagen_ia_streamlit: No se generaron imágenes.")
            return None
    except Exception as e:
        print(f"[LOG] Error general: {e}")
        return None

def generar_prompt_dinamico(input_image):
    """
    Genera un prompt dinámico basado en las características detectadas en la imagen.
    """
    print("[LOG] generar_prompt_dinamico: Analizando la imagen para generar el prompt...")
    
    # Convertir la imagen de PIL a formato OpenCV
    cv_image = np.array(input_image)
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)

    # Cargar el modelo de detección de rostros
    face_cascade = cv2.CascadeClassifier(os.path.join(MODELS_DIR, 'haarcascade_frontalface_default.xml'))
    faces = face_cascade.detectMultiScale(cv_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        print("[LOG] generar_prompt_dinamico: No se detectaron rostros en la imagen.")
        return "Foto de cuerpo entero de una persona con cabello corto, ojos marrones, usando un traje elegante."

    # Si se detecta al menos un rostro, proceder con el análisis
    print(f"[LOG] generar_prompt_dinamico: {len(faces)} rostro(s) detectado(s).")

    # Suponiendo que solo analizamos el primer rostro detectado
    x, y, w, h = faces[0]
    rostro = cv_image[y:y+h, x:x+w]

    # Cargar el modelo de género
    gender_net = cv2.dnn.readNetFromCaffe(
        os.path.join(MODELS_DIR, 'gender_deploy.prototxt'),
        os.path.join(MODELS_DIR, 'gender_net.caffemodel')
    )

    # Preprocesar el rostro para el modelo de género
    blob = cv2.dnn.blobFromImage(rostro, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)
    gender_net.setInput(blob)
    gender_preds = gender_net.forward()
    gender = "hombre" if gender_preds[0][0] > 0.5 else "mujer"

    # Detectar color de pelo (análisis simple en la parte superior del rostro)
    hair_region = cv_image[y-20:y, x:x+w] if y-20 > 0 else cv_image[0:y, x:x+w]
    hair_color = detectar_color_dominante(hair_region)

    # Detectar color de ojos (análisis en la región de los ojos)
    eye_region = rostro[int(h*0.3):int(h*0.6), int(w*0.2):int(w*0.8)]
    eye_color = detectar_color_dominante(eye_region)

    # Generar el prompt basado en las características detectadas
    prompt = f"Foto de cuerpo entero de un {gender} con cabello {hair_color}, ojos {eye_color}, usando un atuendo elegante."

    print(f"[LOG] generar_prompt_dinamico: Prompt generado: {prompt}")
    return prompt

def detectar_color_dominante(region):
    """
    Detecta el color dominante en una región de la imagen.
    """
    if region.size == 0:
        return "desconocido"
    
    # Convertir a HSV para mejor análisis de color
    hsv = cv2.cvtColor(region, cv2.COLOR_BGR2HSV)
    
    # Calcular histograma de colores
    hist = cv2.calcHist([hsv], [0], None, [180], [0, 180])
    max_idx = np.argmax(hist)
    
    # Mapear a colores básicos
    if max_idx < 15 or max_idx > 165:
        return "rojo"
    elif 15 <= max_idx < 45:
        return "amarillo"
    elif 45 <= max_idx < 75:
        return "verde"
    elif 75 <= max_idx < 105:
        return "cian"
    elif 105 <= max_idx < 135:
        return "azul"
    elif 135 <= max_idx < 165:
        return "magenta"
    else:
        return "marrón"