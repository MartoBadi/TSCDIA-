import streamlit as st
from ia_image_generator import generar_imagen_ia
import os

st.title("Estilo Chick - Moda al Instante")
st.write("Sube tu foto y genera tu atuendo con IA")

uploaded_file = st.file_uploader("Sube tu foto", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img_path = f"temp_{uploaded_file.name}"
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Imagen guardada como {img_path}")
    output_path = os.path.join("uploads", "ia_result.png")
    st.write("Generando imagen IA, espera unos segundos...")
    ia_img_path = generar_imagen_ia(prompt, output_path)
    st.image(ia_img_path, caption="Imagen generada por IA", use_column_width=True)
