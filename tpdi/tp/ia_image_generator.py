import os
from diffusers.pipelines.pipeline_utils import DiffusionPipeline
from PIL import Image
import numpy as np
import urllib.request
import torch
import threading
import time
import streamlit as st

def mostrar_tiempo():
    inicio = time.time()
    while True:
        transcurrido = int(time.time() - inicio)
        print(f"Tiempo desde inicio: {transcurrido} segundos", end='\r')
        time.sleep(1)

# Inicia el hilo al arrancar la app
threading.Thread(target=mostrar_tiempo, daemon=True).start()

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
        _pipe_cache = DiffusionPipeline.from_pretrained(
        r"CompVis/stable-diffusion-v1-4",
            torch_dtype=torch.float32, low_cpu_mem_usage=True
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
        progreso = st.progress(0, text="Generando imagen IA...")
        tiempo_texto = st.empty()
        start_time = time.time()
        num_steps = 1
        total_steps = 0
    
        def callback(step, timestep, latents):
            try:
                print(f"[LOG] callback: step={step}, timestep={timestep}")
                if total_steps == 0:
                    percent = 0
                else:
                    percent = int((step + 1) * 100 / total_steps)
                estimated_total = (time.time() - start_time) * total_steps / (step + 1) if (step + 1) > 0 and total_steps else 0
                remaining = estimated_total - (time.time() - start_time)
                minutes = int(remaining // 60)
                seconds = int(remaining % 60)
                tiempo_texto.write(f"Tiempo restante: {minutes}m {seconds}s")
                progreso.progress(percent, text=f"Progreso: {percent}%")
            except Exception as e:
                print(f"[LOG] Error en callback: {e}")
                st.error(f"Error en callback: {e}")

        print("[LOG] generar_imagen_ia_streamlit: Llamando a pipe img2img...")
        if input_image is not None:
            print("[LOG] Antes de llamar al pipeline img2img...")
            result = pipe.images[0]
            print("[LOG] Después de llamar al pipeline img2img...")
        else:
            st.error("Debes proporcionar una imagen base para img2img.")
            return None
        print("[LOG] generar_imagen_ia_streamlit: pipe terminado.")
        print(f"[LOG] generar_imagen_ia_streamlit: result type={type(result)}")
        img = result[0] if hasattr(result, "images") else result[0] if result else None
        print(f"[LOG] generar_imagen_ia_streamlit: img type={type(img)}")
        if img is None:
            print("[LOG] generar_imagen_ia_streamlit: img es None")
            st.error("No se pudo generar la imagen. Verifica el prompt y los recursos disponibles.")
            tiempo_texto.empty()
            progreso.empty()
            return None
        if isinstance(img, Image.Image):
            print("[LOG] generar_imagen_ia_streamlit: Guardando imagen tipo PIL.Image")
            img.save(output_path)
        elif isinstance(img, np.ndarray):
            print("[LOG] generar_imagen_ia_streamlit: Guardando imagen tipo np.ndarray")
            Image.fromarray((img * 255).astype(np.uint8)).save(output_path)
        elif hasattr(img, 'cpu') and hasattr(img, 'numpy'):
            print("[LOG] generar_imagen_ia_streamlit: Guardando imagen tipo tensor")
            arr = img.cpu().numpy()
            Image.fromarray((arr * 255).astype(np.uint8)).save(output_path)
        else:
            print("[LOG] generar_imagen_ia_streamlit: Formato de imagen no soportado")
            st.error("Formato de imagen no soportado.")
            tiempo_texto.empty()
            progreso.empty()
            return None
        tiempo_texto.empty()
        progreso.empty()
        print(f"[LOG] generar_imagen_ia_streamlit: Imagen guardada en {output_path}")
        return output_path
    except Exception as e:
        print(f"[LOG] Error general: {e}")
        st.error(f"Error general: {e}")
        return None