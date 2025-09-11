import os
from diffusers.pipelines.stable_diffusion_xl.pipeline_stable_diffusion_xl import StableDiffusionXLPipeline
from PIL import Image
import numpy as np
import urllib.request
import torch
import threading
import time

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
    if _pipe_cache is None:
        print("Cargando modelo SDXL-Turbo (esto puede tardar unos segundos)...")
        _pipe_cache = StableDiffusionXLPipeline.from_pretrained(
            "stabilityai/sdxl-turbo",
            torch_dtype=torch.float32,
            low_cpu_mem_usage=True
        ).to("cpu")
        print("Modelo SDXL-Turbo cargado.")
    return _pipe_cache

def generar_imagen_ia(prompt, output_path):
    pipe = get_pipe()
    result = pipe(prompt)
    img = result[0]  # Access the image directly from the tuple
    if isinstance(img, Image.Image):
        img.save(output_path)
    elif isinstance(img, np.ndarray):
        Image.fromarray((img * 255).astype(np.uint8)).save(output_path)
    elif img is not None and hasattr(img, 'cpu') and hasattr(img, 'numpy'):
        arr = img.cpu().numpy()
        Image.fromarray((arr * 255).astype(np.uint8)).save(output_path)
    else:
        raise TypeError("Formato de imagen no soportado o la imagen es None")
    return output_path