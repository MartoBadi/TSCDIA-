import os
from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion import StableDiffusionPipeline
from PIL import Image
import numpy as np

# Inicializa el pipeline solo una vez (mejor rendimiento)
pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1")

def generar_imagen_ia(prompt, output_path):
    result = pipe(prompt)
    img = result.images[0]
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