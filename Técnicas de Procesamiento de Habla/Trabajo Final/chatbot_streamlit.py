import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from datetime import datetime

# Cargar modelo y tokenizer
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-llm-1.5b-chat")
    model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-llm-1.5b-chat")
    return tokenizer, model

tokenizer, model = load_model()

st.title("Chatbot 24/7 - Asistente Virtual Permanente")
st.write("Simula atención automatizada en cualquier momento del día.")

# Inicializar historial de chat en sesión
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Entrada de usuario
def get_time():
    return datetime.now().strftime("%H:%M")

user_input = st.text_input("Escribe tu consulta:")

if st.button("Enviar") and user_input:
    # Añadir entrada del usuario al historial
    st.session_state.chat_history.append({
        "role": "Usuario",
        "text": user_input,
        "time": get_time()
    })

    # Preparar entrada para DialoGPT
    new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    bot_input_ids = new_user_input_ids
    if len(st.session_state.chat_history) > 1:
        # Concatenar historial (máx 3 turnos)
        previous = st.session_state.chat_history[-3:]
        history_text = "".join([x["text"] + tokenizer.eos_token for x in previous if x["role"] == "Usuario"])
        bot_input_ids = tokenizer.encode(history_text + user_input + tokenizer.eos_token, return_tensors='pt')

    # Generar respuesta
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

    # Añadir respuesta del bot al historial
    st.session_state.chat_history.append({
        "role": "Bot",
        "text": response,
        "time": get_time()
    })

# Mostrar historial de chat
for msg in st.session_state.chat_history:
    if msg["role"] == "Usuario":
        st.markdown(f"**[{msg['time']}] Usuario:** {msg['text']}")
    else:
        st.markdown(f"**[{msg['time']}] Bot:** {msg['text']}")

# Registro simulado de interacciones
st.sidebar.title("Registro de Interacciones")
for i, msg in enumerate(st.session_state.chat_history):
    st.sidebar.write(f"{i+1}. [{msg['time']}] {msg['role']}: {msg['text']}")

st.sidebar.info("Este registro es simulado y solo visible para esta sesión.")
