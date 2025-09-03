import os
import urllib.request

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
