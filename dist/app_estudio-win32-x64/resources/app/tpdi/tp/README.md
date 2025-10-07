# ESTILO CHICK - MODA AL INSTANTE

## Problema a resolver
A menudo, las personas tienen dificultades para elegir atuendos que complementen sus características físicas o simplemente buscan inspiración personalizada.

## Objetivo principal
Desarrollar un sistema (Python + Web) que, a partir de la imagen de una persona, analice sus rasgos faciales y sugiera un atuendo completo adaptado a su género.

## Alcance inicial (MVP)
- Entrada: Imagen de una persona (retrato o medio cuerpo)
- Detección de género
- Análisis facial: ojos (color), forma de la cara, peinado
- Sugerencia de atuendo (básico por género)
- Resultado: Texto descriptivo de la sugerencia

## Cronograma sugerido
- Semana 1-2: Investigación y recopilación de datos
- Semana 3-4: Preprocesamiento, detección facial y género
- Semana 5-6: Lógica de sugerencia de atuendo
- Semana 7: Integración y pruebas
- Semana 8: Documentación y presentación

## Estructura del proyecto
- `app.py`: Servidor Flask
- `face_analyzer.py`: Análisis facial y de género
- `fashion_recommender.py`: Lógica de recomendación
- `templates/index.html`: Frontend web
- `/static/`: Archivos estáticos (CSS, JS, imágenes)

## Tecnologías
- Python, Flask, OpenCV, dlib, scikit-learn, Pillow, Pandas, NumPy
- HTML, CSS, JavaScript

## Cómo ejecutar
1. Instala dependencias: `pip install -r requirements.txt`
2. Ejecuta el servidor: `python app.py`
3. Abre el navegador en `http://localhost:5000`

---

¡Recuerda subir avances regularmente a GitHub!
