import streamlit as st
import io
from moviepy.audio.AudioClip import concatenate_audioclips
from moviepy.audio.io.AudioFileClip import AudioFileClip
from IPython.display import Audio
from gtts import gTTS
import os

teoria = """
de recomendación y plataformas de redes sociales donde la
velocidad y el volumen son críticos.
Requieren una
gobernanza de datos estricta para evitar el "Data Swamp syndrome" (datos caóticos y sin contexto).
Ejemplos: MongoDB, Redis, Neo4j, Cassandra.
2.2.3 Bases de Datos Distribuidas
Almacenan y gestionan información a través de
múltiples nodos de una red para ofrecer escalabilidad y resiliencia. Pueden ser tanto relacionales como NoSQL en su implementación subyacente.
Ventajas:
Alta Disponibilidad: Si un nodo falla, el sistema continúa operando sin interrupción (tolerancia a fallos).
Latencia Reducida: Permiten la distribución geográfica de los datos, mejorando el rendimiento para usuarios finales globalmente.
Escalabilidad Extrema: Capacidad para gestionar un aumento masivo de la demanda y del volumen de datos.
Desventajas:
Complejidad Operacional: Requieren un conocimiento técnico especializado para su implementación y mantenimiento.
Teorema CAP: Presentan dificultades inherentes para garantizar simultáneamente Consistencia, Disponibilidad y Tolerancia a la Partición.
Restricciones/Consideraciones:
Su uso se justifica en sistemas críticos que requieren resiliencia y baja latencia constante.
La gestión de la sincronización entre nodos es el principal desafío técnico y de rendimiento.
Ejemplos: Google Spanner, Amazon Aurora, Apache Cassandra.
2.2.4 Bases de Datos en la Nube (Cloud)
Son bases de datos
gestionadas y alojadas por proveedores de servicios en la nube (AWS, Azure, GCP). El modelo puede ser IaaS, PaaS o SaaS.
Ventajas:
Elasticidad y Escalabilidad: Los recursos de cómputo y almacenamiento se escalan dinámicamente según la demanda, optimizando los costos operativos.
Mantenimiento Externalizado: El proveedor se encarga de las tareas de administración, parches de seguridad y backups, reduciendo la carga operativa interna.
Innovación Acelerada: Acceso inmediato a servicios avanzados integrados (Machine Learning, IoT, Big Data).
Desventajas:
Dependencia del Proveedor (Vendor Lock-in): La migración de grandes volúmenes de datos a otro proveedor o a un entorno local puede ser compleja y costosa.
Costo a Largo Plazo: Aunque el costo inicial es bajo (conversión de CAPEX a OPEX), los costos pueden dispararse si los recursos no se gestionan y optimizan adecuadamente.
Restricciones/Consideraciones:
La
seguridad y el cumplimiento normativo son una responsabilidad compartida entre el proveedor y el cliente.
Son el motor del
Lakehouse y las arquitecturas modernas, facilitando el despliegue multi-cloud.
Ejemplos: Amazon RDS, Azure SQL Database, Google Cloud Firestore.

2.3 De las Bases de Datos Relacionales a los Ecosistemas Distribuidos
Durante décadas, las bases de datos relacionales —con sólidos principios ACID— fueron el paradigma dominante por su confiabilidad y consistencia. No obstante, el crecimiento exponencial en volumen, variedad y velocidad de los datos ha revelado sus limitaciones estructurales, especialmente al trabajar con datos semiestructurados, streams en tiempo real o requerimientos de escalabilidad horizontal.
La transición hacia ecosistemas distribuidos se articula en torno a tres fuerzas:
●       Escalabilidad horizontal: la capacidad para gestionar grandes volúmenes de información en múltiples servidores simultáneamente.

●       Variedad de datos: la inclusión de datos estructurados, semiestructurados y no estructurados.
●       Analítica en tiempo real: la necesidad de obtener insights rápidos, reducir latencias y reaccionar dinámicamente ante eventos.
2.4 Paradigmas de Almacenamiento y Procesamiento
La evolución arquitectónica puede conceptualizarse en tres generaciones:
●       Primera Generación (1980-2000): Sistemas OLTP optimizados para transacciones con garantías ACID completas [10].
●       Segunda Generación (2000-2015): Separación de cargas transaccionales y analíticas mediante Data Warehouses, implementando procesos ETL y modelado dimensional.
●       Tercera Generación (2015-presente): Despliegue de arquitecturas distribuidas, almacenamiento desacoplado, capacidad de procesamiento paralelo masivo, aparición del modelo Lakehouse como mezcla de lo mejor de Data Lakes y Data Warehouses. [11].
"""

def split_string_by_words(text, num_words=5):
  """
  Splits a string into segments of a specified number of words.

  Args:
    text: The input string.
    num_words: The number of words per segment.

  Returns:
    A list of string segments.
  """
  words = text.split()
  segments = []
  for i in range(0, len(words), num_words):
    segment = ' '.join(words[i:i + num_words])
    segments.append(segment)
  return segments

# Example usage:
segments = split_string_by_words(teoria)

# Generate and save short audio files if they don't exist
short_audio_paths = [f"frase_{i}.mp3" for i in range(len(segments))]

for i, frase in enumerate(segments):
    if not os.path.exists(f"frase_{i}.mp3"):
        tts = gTTS(text=frase, lang='es')
        tts.save(f"frase_{i}.mp3")

# Load short audio files
short_audios = []
for i, short_audio_path in enumerate(short_audio_paths):
    try:
        short_audio = AudioSegment.from_file(short_audio_path)
        short_audios.append(short_audio)
    except Exception as e:
        print(f"Error loading short audio {i} from {short_audio_path}: {e}")
        short_audios.append(None)

# Generate and save the long audio file if it doesn't exist
long_audio_path = "audio_todas_clases.mp3"
if not os.path.exists(long_audio_path):
    # List to store repeated audio clips
    clips = []

    # Load and repeat each audio file 5 times
    for archivo in short_audio_paths:
        try:
            audio = AudioFileClip(archivo)
            audio_repetido = concatenate_audioclips([audio] * 5)  # Repeat 5 times
            clips.append(audio_repetido)
        except Exception as e:
            print(f"Error al procesar el archivo {archivo}: {e}")

    # Concatenate all repeated clips
    audio_concatenado = concatenate_audioclips(clips)

    # Save the concatenated audio to an output file
    audio_concatenado.write_audiofile(long_audio_path)

# Load the long audio into an AudioSegment object
try:
    long_audio = AudioSegment.from_file(long_audio_path)
except Exception as e:
    print(f"Error loading long audio: {e}")
    long_audio = None


# Initialize session state for audio start time
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0

def find_audio_position(long_audio, short_audio):
  """
  Finds the start time in milliseconds of the first occurrence of the short audio
  within the long audio.

  Args:
    long_audio: The AudioSegment of the long audio.
    short_audio: The AudioSegment of the short audio.

  Returns:
    The start time in milliseconds if found, -1 otherwise.
  """
  if long_audio is None or short_audio is None:
      return -1
  # Use find_matches to find occurrences, tolerance can be adjusted
  matches = long_audio.find_matches(short_audio, chunk_size=1000, tolerance=5)
  if matches:
    # find_matches returns a list of tuples (start_ms, end_ms)
    return matches[0][0]
  else:
    return -1

def jump_to_audio(index):
    """
    Callback function for button click. Finds the position of the short audio
    and updates the session state.
    """
    if short_audios and 0 <= index < len(short_audios) and long_audio:
        position_ms = find_audio_position(long_audio, short_audios[index])
        if position_ms != -1:
            st.session_state.start_time = position_ms / 1000.0  # Convert ms to seconds
        else:
            st.warning(f"Audio {index+1} not found in the long audio.")
    else:
        st.error(f"Could not process jump for Audio {index+1}.")

# Set the title of the Streamlit application
st.title("Audio Player with Jump Points")

# Display a header for the audio player section
st.header("Long Audio Player")

# Use streamlit.audio() to create an audio player for the long_audio
# Convert the AudioSegment to bytes for Streamlit
if long_audio:
    long_audio_bytes = long_audio.export(format="mp3").read()
    # Use the start_time from session state
    st.audio(long_audio_bytes, format="audio/mp3", start_time=st.session_state.start_time)
else:
    st.error("Could not load the long audio file.")

# Create a section or container for the buttons
st.header("Jump to Specific Sections")

# Iterate through the short_audios list and create a button for each short audio
if short_audios:
    for i, short_audio in enumerate(short_audios):
        if short_audio:
            # Add a unique key and the on_click callback
            st.button(f"Jump to Audio {i+1}", key=f"jump_button_{i}", on_click=jump_to_audio, args=(i,))
        else:
            st.write(f"Audio {i+1} could not be loaded.")
