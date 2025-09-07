import streamlit as st
from ia_image_generator import generar_imagen_ia
import os

st.title("Estilo Chick - Moda al Instante")
st.write("Sube tu foto y genera tu atuendo con IA")

uploaded_file = st.file_uploader("Sube una foto (rostro o medio cuerpo)", type=["jpg", "jpeg", "png"])
prompt = st.text_input("Describe el atuendo que deseas (opcional)", "Retrato de una persona con atuendo moderno")

if uploaded_file is not None:
    img_path = os.path.join("uploads", uploaded_file.name)
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    output_path = os.path.join("uploads", "ia_result.png")
    st.write("Generando imagen IA, espera unos segundos...")
    ia_img_path = generar_imagen_ia(prompt, output_path)
    st.image(ia_img_path, caption="Imagen generada por IA", use_column_width=True)