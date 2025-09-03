from flask import Flask, render_template, request, jsonify
from face_analyzer import analizar_imagen
from fashion_recommender import recomendar_atuendo
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No se envió imagen'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'Nombre de archivo vacío'}), 400
    filename = file.filename if file.filename is not None else "uploaded_file"
    filepath = os.path.join(UPLOAD_FOLDER, secure_filename(filename))
    file.save(filepath)
    # Análisis facial
    resultado = analizar_imagen(filepath)
    # Sugerencia de atuendo
    sugerencia = recomendar_atuendo(resultado)
    return jsonify({'analisis': resultado, 'sugerencia': sugerencia})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)