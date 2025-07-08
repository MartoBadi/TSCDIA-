# 🎵 Reproductor de Exposición - Streamlit

Una aplicación web interactiva para el análisis de exposiciones académicas, específicamente diseñada para el tema "IA, prevención de fraude y trabajo en Fintech: una perspectiva socio-ética".

## 🚀 Características

- **Reproductor de audio principal** con controles de navegación
- **Navegación por frases** con botones interactivos
- **Sincronización automática** del texto con el audio
- **Área de notas** para que el usuario escriba observaciones
- **Visualización del guión** con resaltado de la frase actual
- **Tema oscuro** moderno y profesional
- **Estadísticas detalladas** en la barra lateral

## 📋 Funcionalidades

### 🎧 Audio Principal
- Sube tu archivo `audio_exposicion.mp3`
- Control de tiempo con slider
- Indicador de duración total

### 🎯 Navegación por Frases
- 17 botones correspondientes a cada frase del guión
- Indicador visual de la frase activa (🔴)
- Salto directo a cualquier frase

### 📝 Notas del Usuario
- Área de texto para escribir observaciones
- Botón para limpiar el texto
- Funcionalidad de grabación (solo en versión local)

### 📄 Guión Interactivo
- Mostrar/ocultar el guión completo
- Resaltado de la frase actual (🔵)
- Frases anteriores marcadas (✅)

## 🔧 Instalación Local

1. Clona o descarga los archivos
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```

## 🌐 Despliegue en Streamlit Cloud

### Pasos para subir a streamlit.io:

1. **Crea un repositorio en GitHub** con estos archivos:
   - `app.py`
   - `requirements.txt`
   - `README.md`

2. **Ve a [streamlit.io](https://streamlit.io)**
   - Inicia sesión con tu cuenta de GitHub
   - Haz clic en "New app"

3. **Configuración del despliegue:**
   - Repository: Tu repositorio de GitHub
   - Branch: main (o la rama que prefieras)
   - Main file path: `app.py`
   - App URL: Elige una URL personalizada

4. **Haz clic en "Deploy"**
   - Streamlit instalará automáticamente las dependencias
   - En unos minutos tendrás tu aplicación online

## 📁 Estructura de Archivos

```
app_web_estudio/
│
├── app.py                 # Aplicación principal de Streamlit
├── requirements.txt       # Dependencias de Python
├── README.md             # Este archivo
├── index.html            # Versión HTML original
├── script.js             # JavaScript original
└── styles.css            # Estilos CSS originales
```

## 🎵 Uso de la Aplicación

1. **Sube tu archivo de audio** en el área designada
2. **Usa el slider** para navegar por el tiempo
3. **Haz clic en los botones de frases** para saltar a secciones específicas
4. **Activa el guión** para ver la sincronización de texto
5. **Toma notas** en el área de texto

## 🔧 Configuración

### Datos del Audio
- **Frases totales:** 17
- **Repeticiones por frase:** 5
- **Duraciones exactas** configuradas para cada frase
- **Tiempo total calculado** automáticamente

### Personalización
- Modifica `textos_exposicion` para cambiar los textos
- Ajusta `duraciones_audios` para diferentes duraciones
- Cambia `REPETICIONES_POR_FRASE` según tu audio

## 🎨 Tema Visual

- **Tema oscuro** con gradientes azul-gris
- **Colores de acento** para diferentes estados
- **Tipografía clara** y legible
- **Responsivo** para diferentes tamaños de pantalla

## 📊 Estadísticas

La aplicación muestra:
- Total de frases
- Duración total del audio
- Repeticiones por frase
- Tabla detallada de tiempos

## 🚧 Limitaciones en Streamlit Cloud

- **Grabación de audio:** No disponible en Streamlit Cloud (solo local)
- **Sincronización automática:** Requiere control manual con slider
- **Archivos de audio:** Deben subirse cada vez (no se guardan)

## 🔗 Enlaces Útiles

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Cloud](https://streamlit.io/cloud)
- [GitHub Repository](https://github.com/tu-usuario/tu-repo)

---

**Desarrollado para el análisis de exposiciones académicas sobre IA y Fintech** 🎓
