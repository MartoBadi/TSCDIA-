import os
import urllib.request

MODELS_DIR = 'models'
os.makedirs(MODELS_DIR, exist_ok=True)

# URLs de modelos preentrenados
MODELOS = {
    'haarcascade_frontalface_default.xml': 'https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml',
    'deploy_gender.prototxt': 'https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy_gender.prototxt',
    'gender_net.caffemodel': 'https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/gender_net.caffemodel',
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
