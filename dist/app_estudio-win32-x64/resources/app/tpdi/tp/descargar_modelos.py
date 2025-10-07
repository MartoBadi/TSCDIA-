"""
Ejemplo: Descarga y uso del modelo IA más pequeño y eficiente para generación de imágenes
"""

from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion import StableDiffusionPipeline
import torch

def descargar_sd_turbo():
    print("Descargando y cargando modelo sd-turbo (el más pequeño y rápido de Stable Diffusion)...")
    pipe = StableDiffusionPipeline.from_pretrained(
        "stabilityai/sd-turbo",
        torch_dtype=torch.float32,
        low_cpu_mem_usage=True
    ).to("cpu")
    print("Modelo sd-turbo listo para usar.")
    return pipe

# Ejemplo de uso:
if __name__ == "__main__":
    pipe = descargar_sd_turbo()
   