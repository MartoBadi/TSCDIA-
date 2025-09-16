import streamlit as st
from ia_image_generator import generar_imagen_ia_streamlit
from PIL import Image
import time
import os

st.title("Estilo Chick - Moda al Instante")
st.write("Sube tu foto y genera tu atuendo con IA")

uploaded_file = st.file_uploader("Sube tu foto", type=["jpg", "jpeg", "png"])
genero = st.selectbox("Selecciona el género", ["Hombre", "Mujer"])  # Nuevo campo
prompt = st.text_input("Describe el atuendo que deseas (opcional)", "")

if uploaded_file is not None:
    img_path = f"temp_{uploaded_file.name}"
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    input_image = Image.open(img_path).convert("RGB")
    st.image(input_image, caption="Imagen subida", use_container_width=True)

    output_path = os.path.join("uploads", "ia_result.png")

    if st.button("Generar imagen IA"):
        st.write("Generando imagen IA, espera unos segundos...")
        start_time = time.time()
        try:
            ia_img_path = generar_imagen_ia_streamlit(prompt, output_path, input_image, genero)  # Pasa genero
            if ia_img_path is not None:
                st.image(ia_img_path, caption="Imagen generada por IA", use_container_width=True)
            else:
                st.error("No se pudo generar la imagen con IA. Intenta nuevamente.")
        except Exception as e:
            st.error(f"Error: {e}")