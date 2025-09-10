import streamlit as st
from ia_image_generator import generar_imagen_ia
import time

st.title("Estilo Chick - Moda al Instante")
st.write("Sube tu foto y genera tu atuendo con IA")

uploaded_file = st.file_uploader("Sube tu foto", type=["jpg", "jpeg", "png"])
prompt = st.text_input("Describe el atuendo que deseas (opcional)", "")

if uploaded_file is not None:
    img_path = f"temp_{uploaded_file.name}"
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Imagen guardada como {img_path}")

    output_path = "imagen_generada.png"  # Puedes cambiar el nombre si lo necesitas

if st.button("Generar imagen IA"):
    start_time = time.time()
    try:
        ia_img_path = generar_imagen_ia(prompt, output_path)
        elapsed = time.time() - start_time
        st.image(ia_img_path)
        st.success(f"Imagen generada en {elapsed:.2f} segundos.")
    except Exception as e:
        st.error(f"Ocurrió un error al generar la imagen IA: {e}")
