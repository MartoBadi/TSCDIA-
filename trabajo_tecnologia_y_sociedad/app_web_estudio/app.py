import streamlit as st
import numpy as np
import pandas as pd
from io import BytesIO
import base64
import time

# Configuración de la página
st.set_page_config(
    page_title="Reproductor de Exposición - IA y Fintech",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para tema oscuro
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: #f0f0f0;
    }
    
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    }
    
    .audio-player {
        background: rgba(30, 30, 50, 0.95);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin: 20px 0;
    }
    
    .phrase-container {
        background: rgba(30, 30, 50, 0.95);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin: 20px 0;
    }
    
    .script-container {
        background: rgba(30, 30, 50, 0.95);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin: 20px 0;
        max-height: 400px;
        overflow-y: auto;
    }
    
    .phrase-text {
        background: rgba(40, 40, 60, 0.6);
        padding: 10px;
        margin: 10px 0;
        border-radius: 8px;
        border-left: 3px solid #4a5568;
        color: #e0e0e0;
    }
    
    .phrase-text.current {
        background: rgba(56, 161, 105, 0.2);
        border-left-color: #38a169;
        box-shadow: 0 2px 8px rgba(56, 161, 105, 0.2);
    }
    
    .phrase-text.highlight {
        background: rgba(255, 193, 7, 0.2);
        border-left-color: #ffc107;
        box-shadow: 0 2px 8px rgba(255, 193, 7, 0.2);
    }
    
    .recording-section {
        background: rgba(40, 40, 60, 0.6);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin: 20px 0;
    }
    
    h1, h2, h3, h4 {
        color: #e0e0e0 !important;
    }
    
    .stMarkdown {
        color: #e0e0e0;
    }
</style>
""", unsafe_allow_html=True)

# Textos de la exposición
textos_exposicion = [
    "Buenas tardes, somos Marto, Rocío y Naty",
    "y hoy vamos a presentar",
    "nuestro trabajo titulado",
    "IA, prevención de fraude y trabajo en Fintech: una perspectiva socio-ética",
    "El objetivo principal fue",
    "analizar cómo se aplica la inteligencia artificial",
    "en la detección de fraudes",
    "dentro del ecosistema Fintech",
    "enfocándonos no solo en lo técnico",
    "sino también en los aspectos éticos, laborales y sociales.",
    "Partimos de una hipótesis central",
    "la inteligencia artificial no es neutral",
    "Su diseño, entrenamiento y uso",
    "tienen impactos directos sobre las personas",
    "y la sociedad",
    "Por eso, creemos que su implementación",
    "debe ser crítica, responsable y ética."
]

# Duraciones exactas de cada audio individual (en segundos)
duraciones_audios = [4.44, 2.112, 2.16, 7.8, 2.376, 4.224, 2.352, 2.688, 2.928, 4.824, 3.0, 3.672, 3.408, 3.384, 1.224, 3.48, 3.96]

# Configuración de tiempos
REPETICIONES_POR_FRASE = 5

# Calcular tiempos de inicio
def calcular_tiempos_inicio():
    tiempos_inicio = []
    tiempo_acumulado = 0
    
    for i, duracion in enumerate(duraciones_audios):
        tiempos_inicio.append(tiempo_acumulado)
        tiempo_acumulado += REPETICIONES_POR_FRASE * duracion
    
    return tiempos_inicio

tiempos_inicio = calcular_tiempos_inicio()

# Función para formatear tiempo
def format_time(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes}:{seconds:02d}"

# Función para encontrar frase activa
def get_active_phrase(current_time):
    active_phrase = -1
    for i, tiempo in enumerate(tiempos_inicio):
        if current_time >= tiempo:
            active_phrase = i
        else:
            break
    return active_phrase

# Inicializar session state
if 'current_time' not in st.session_state:
    st.session_state.current_time = 0
if 'active_phrase' not in st.session_state:
    st.session_state.active_phrase = -1
if 'show_script' not in st.session_state:
    st.session_state.show_script = False
if 'user_notes' not in st.session_state:
    st.session_state.user_notes = ""

# Título principal
st.markdown('<div class="audio-player">', unsafe_allow_html=True)
st.title("🎵 Reproductor de Exposición")
st.markdown("### IA, prevención de fraude y trabajo en Fintech: una perspectiva socio-ética")
st.markdown('</div>', unsafe_allow_html=True)

# Reproductor de audio principal
st.markdown('<div class="audio-player">', unsafe_allow_html=True)
st.markdown("### 🎧 Audio Principal")

# Nota sobre el archivo de audio
st.info("📁 Para usar esta aplicación, necesitas subir tu archivo 'audio_exposicion.mp3' aquí abajo:")

# Subida de archivo de audio
audio_file = st.file_uploader("Sube tu archivo de audio", type=['mp3', 'wav', 'ogg'])

if audio_file is not None:
    # Mostrar reproductor de audio
    st.audio(audio_file, format='audio/mp3')
    
    # Controles de tiempo simulados (ya que no podemos obtener el tiempo real del reproductor)
    col1, col2 = st.columns([3, 1])
    with col1:
        current_time = st.slider("Tiempo actual (segundos)", 0, int(sum(duraciones_audios) * REPETICIONES_POR_FRASE), st.session_state.current_time)
    with col2:
        st.metric("Duración total", format_time(sum(duraciones_audios) * REPETICIONES_POR_FRASE))
    
    # Actualizar tiempo actual
    if current_time != st.session_state.current_time:
        st.session_state.current_time = current_time
        st.session_state.active_phrase = get_active_phrase(current_time)

st.markdown('</div>', unsafe_allow_html=True)

# Navegación por frases
st.markdown('<div class="phrase-container">', unsafe_allow_html=True)
st.markdown("### 🎯 Navegación por Frases")

# Crear botones para cada frase
cols = st.columns(3)
for i, texto in enumerate(textos_exposicion):
    col_idx = i % 3
    with cols[col_idx]:
        if st.session_state.active_phrase == i:
            button_style = "🔴"  # Indicador de frase activa
        else:
            button_style = "▶️"
        
        if st.button(f"{button_style} {i+1}. {texto[:30]}{'...' if len(texto) > 30 else ''}", key=f"phrase_{i}"):
            st.session_state.current_time = tiempos_inicio[i]
            st.session_state.active_phrase = i
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Layout de dos columnas para notas y guión
col1, col2 = st.columns(2)

# Notas del usuario
with col1:
    st.markdown('<div class="phrase-container">', unsafe_allow_html=True)
    st.markdown("### 📝 Notas del Usuario")
    
    user_notes = st.text_area(
        "Escribe tus notas aquí...", 
        value=st.session_state.user_notes,
        height=200,
        key="notes_area"
    )
    
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🗑️ Limpiar Texto"):
            st.session_state.user_notes = ""
            st.rerun()
    
    # Grabación de audio (simulada)
    st.markdown('<div class="recording-section">', unsafe_allow_html=True)
    st.markdown("#### 🎤 Grabación de Audio")
    st.info("🚧 Funcionalidad de grabación no disponible en Streamlit Cloud. Usa la versión local para grabar audio.")
    
    col_rec1, col_rec2, col_rec3 = st.columns(3)
    with col_rec1:
        st.button("🎤 Grabar", disabled=True)
    with col_rec2:
        st.button("▶️ Reproducir", disabled=True)
    with col_rec3:
        st.button("🗑️ Descartar", disabled=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Guión de la exposición
with col2:
    st.markdown('<div class="phrase-container">', unsafe_allow_html=True)
    st.markdown("### 📄 Guión de la Exposición")
    
    if st.button("👁️ Mostrar/Ocultar Guión"):
        st.session_state.show_script = not st.session_state.show_script
        st.rerun()
    
    if st.session_state.show_script:
        st.markdown('<div class="script-container">', unsafe_allow_html=True)
        
        for i, texto in enumerate(textos_exposicion):
            if i == st.session_state.active_phrase:
                class_name = "current"
                icon = "🔵"
            elif i < st.session_state.active_phrase:
                class_name = "highlight"
                icon = "✅"
            else:
                class_name = ""
                icon = "⚪"
            
            st.markdown(f"""
            <div class="phrase-text {class_name}">
                {icon} {i+1}. {texto}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Sidebar con información y controles
with st.sidebar:
    st.markdown("## 📊 Información del Audio")
    
    # Mostrar información de la frase actual
    if st.session_state.active_phrase >= 0:
        current_phrase = st.session_state.active_phrase
        st.success(f"**Frase Activa:** {current_phrase + 1}")
        st.write(f"**Texto:** {textos_exposicion[current_phrase]}")
        st.write(f"**Tiempo de inicio:** {format_time(tiempos_inicio[current_phrase])}")
        st.write(f"**Duración individual:** {duraciones_audios[current_phrase]}s")
        st.write(f"**Duración total (x5):** {duraciones_audios[current_phrase] * 5}s")
    else:
        st.info("No hay frase activa")
    
    st.markdown("---")
    
    # Estadísticas
    st.markdown("## 📈 Estadísticas")
    st.metric("Total de frases", len(textos_exposicion))
    st.metric("Duración total", format_time(sum(duraciones_audios) * REPETICIONES_POR_FRASE))
    st.metric("Repeticiones por frase", REPETICIONES_POR_FRASE)
    
    st.markdown("---")
    
    # Tabla de tiempos
    if st.checkbox("📋 Mostrar tabla de tiempos"):
        df_tiempos = pd.DataFrame({
            'Frase': range(1, len(textos_exposicion) + 1),
            'Inicio': [format_time(t) for t in tiempos_inicio],
            'Duración': [f"{d}s" for d in duraciones_audios],
            'Total': [f"{d*5}s" for d in duraciones_audios]
        })
        st.dataframe(df_tiempos, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #a0a0a0; margin: 20px;">
    <p>📱 Aplicación creada con Streamlit para el análisis de exposiciones académicas</p>
    <p>🎓 Tema: IA, prevención de fraude y trabajo en Fintech</p>
</div>
""", unsafe_allow_html=True)
