import streamlit as st
from ia_image_generator import generar_imagen_ia_streamlit
from PIL import Image
import time
import os

st.title("Estilo Chick - Moda al Instante")
st.write("Sube tu foto y genera tu atuendo con IA")

uploaded_file = st.file_uploader("Sube tu foto", type=["jpg", "jpeg", "png"])
prompt = st.text_input("Describe el atuendo que deseas (opcional)", "")

if uploaded_file is not None:
    img_path = f"temp_{uploaded_file.name}"
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Abrir la imagen como PIL.Image para img2img
    input_image = Image.open(img_path).convert("RGB")

    output_path = os.path.join("uploads", "ia_result.png")
    st.write("Generando imagen IA, espera unos segundos...")
    ia_img_path = generar_imagen_ia_streamlit(prompt, output_path, input_image)

    if ia_img_path is not None:
        st.image(ia_img_path, caption="Imagen generada por IA", use_container_width=True)
    else:
        st.error("No se pudo generar la imagen con IA. Intenta nuevamente.")

    st.success(f"Imagen guardada como {img_path}")

    output_path = "imagen_generada.png"  # Puedes cambiar el nombre si lo necesitas

    if st.button("Generar imagen IA"):
        start_time = time.time()
        try:
            ia_img_path = generar_imagen_ia_streamlit(prompt, output_path, input_image)
            elapsed = time.time() - start_time
            if ia_img_path is not None:
                st.image(ia_img_path)
                st.success(f"Imagen generada en {elapsed:.2f} segundos.")
            else:
                st.error("No se pudo generar la imagen con IA. Intenta nuevamente.")
        except Exception as e:
            st.error(f"Ocurrió un error al generar la imagen IA: {e}")