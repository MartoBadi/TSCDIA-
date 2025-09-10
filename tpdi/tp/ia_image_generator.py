import os
from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion import StableDiffusionPipeline
from PIL import Image
import numpy as np
import urllib.request
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1",
    torch_dtype=torch.float32,
    low_cpu_mem_usage=True
).to("cpu")

def generar_imagen_ia(prompt, output_path):  

    MODELS_DIR = 'models'
    os.makedirs(MODELS_DIR, exist_ok=True)

    # URLs de modelos preentrenados
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

            if __name__ == '__main__':
                descargar_modelos()

        result = pipe(prompt)
        img = result.images[0] # type: ignore
        # Si es PIL, guarda directo
        if isinstance(img, Image.Image):
            img.save(output_path)
        # Si es numpy, convierte a PIL
        elif isinstance(img, np.ndarray):
            Image.fromarray((img * 255).astype(np.uint8)).save(output_path)
        # Si es tensor, convierte a numpy y luego a PIL
        elif hasattr(img, 'cpu') and hasattr(img, 'numpy'):
            arr = img.cpu().numpy()
            Image.fromarray((arr * 255).astype(np.uint8)).save(output_path)
        else:
            raise TypeError("Formato de imagen no soportado")
        return output_path

        if os.path.exists(output_path):
            return output_path
        else:
            return None