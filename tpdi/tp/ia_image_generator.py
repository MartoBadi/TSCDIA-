import os
from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion_img2img import StableDiffusionImg2ImgPipeline
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
        _pipe_cache = StableDiffusionImg2ImgPipeline.from_pretrained(
        r"stabilityai/stable-diffusion-xl-base-1.0",
            torch_dtype=torch.float32, low_cpu_mem_usage=True, cache_dir="/tmp"
        ).to("cpu")
        print("[LOG] get_pipe: Modelo img2img cargado.")
    else:
        print("[LOG] get_pipe: Usando modelo img2img en caché.")
    return _pipe_cache

def generar_imagen_ia_streamlit(prompt, output_path, input_image, genero=None):
    try:
        print("[LOG] generar_imagen_ia_streamlit: Iniciando generación de imagen IA img2img...")
        if input_image is None or input_image.size[0] == 0 or input_image.size[1] == 0:
            print("[LOG] Error: Imagen de entrada inválida.")
            return None
        
        pipe = get_pipe()
        print("[LOG] generar_imagen_ia_streamlit: Modelo img2img obtenido.")
        
        if not prompt:
            prompt = generar_prompt_dinamico(input_image, genero)
            print(f"[LOG] Prompt generado automáticamente: {prompt}")

        result = pipe(prompt=prompt, image=input_image, num_inference_steps=1, guidance_scale=7.5)
        print("[LOG] Después de llamar al pipeline img2img...")
        
        if hasattr(result, "images") and isinstance(result.images, list) and len(result.images) > 0:
            img = result.images[0]
            print(f"[LOG] generar_imagen_ia_streamlit: img type={type(img)}")
            img.save(output_path)
            print(f"[LOG] generar_imagen_ia_streamlit: Imagen guardada en {output_path}")
            return output_path
        else:
            print("[LOG] generar_imagen_ia_streamlit: No se generaron imágenes.")
            return None
    except Exception as e:
        print(f"[LOG] Error general: {e}")
        return None

def generar_prompt_dinamico(input_image, genero=None):  # Agrega genero
    print("[LOG] generar_prompt_dinamico: Analizando la imagen para generar el prompt...")
    
    # Si no se proporciona genero, intenta detectarlo automáticamente
    if genero is None:
        # Código de detección automática (como antes)
        # ... (tu código existente para detectar genero)
        pass  # Reemplaza con la lógica real
    
    # Usa el genero proporcionado o detectado
    if genero == "Hombre":
        prompt = "Retrato de un hombre con cabello corto, ojos marrones, usando un traje elegante."
    else:
        prompt = "Retrato de una mujer con cabello largo, ojos verdes, usando un vestido moderno."
    
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