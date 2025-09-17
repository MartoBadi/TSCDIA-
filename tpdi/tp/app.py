from flask import Flask, render_template, request, jsonify, make_response
from face_analyzer import analizar_imagen
from ia_image_generator import generar_imagen_ia_streamlit
import os
from flask import send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.after_request
def add_csp_header(response):
    response.headers['Content-Security-Policy'] = "script-src 'self' 'unsafe-eval';"
    return response

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
    sugerencia = "un atuendo formal y moderno" 

    # Generación de imagen IA (Stable Diffusion)
    prompt = f"Haz un retrato del o de la {'hombre' if resultado.get('genero') == 'Hombre' else 'mujer'} de la foto vistiendo: {sugerencia}"
    ia_filename = secure_filename(filename.replace('.jpg', '_ia.jpg').replace('.png', '_ia.png'))
    output_ia_path = os.path.join(UPLOAD_FOLDER, ia_filename)
    input_image = filepath  # Definir input_image como la ruta de la imagen subida
    ia_img_path = generar_imagen_ia_streamlit(prompt, output_ia_path, input_image)
    if ia_img_path:
        resultado['imagen_ia'] = f"uploads/{ia_filename}"

    return jsonify({'analisis': resultado, 'sugerencia': sugerencia})

# Ruta para servir imágenes generadas en uploads
@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)