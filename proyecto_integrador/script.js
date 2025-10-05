// Textos de la exposición extraídos del guión
const textos_exposicion = ['El procesamiento de datos con', 'enfoque a Ciencias de Datos', 'es una parte fundamental del', 'flujo de trabajo de los', 'científicos de datos, ya que', 'garantiza que los datos estén', 'listos para ser analizados, modelados', 'y utilizados para tomar decisiones', 'basadas en evidencia Procesamiento de', 'datos El procesamiento de datos', 'en Ciencia de Datos es', 'el conjunto de técnicas y', 'pasos que permiten convertir datos', 'crudos (muchas veces incompletos, desorganizados', 'o sucios) en datos estructurados', 'y listos para análisis, visualización', 'y modelado predictivo. Fases del', 'procesamiento de datos: 1.Recolección de', 'datos •Orígenes: APIs, sensores IoT,', 'bases de datos, web scraping,', 'encuestas, archivos CSV/Excel, etc. •Herramientas', 'comunes: requests, pandas, beautifulsoup, SQL,', 'etc. 2.Limpieza de datos (Data', 'Cleaning) •Eliminar duplicados •Corregir errores', '•Tratar valores nulos o faltantes', '(NaN ) •Normalizar formatos (fechas,', 'unidades, etc.) •Herramientas: pandas, numpy,', 'OpenRefine 3.Transformación de datos (Data', 'Wrangling o Munging) •Convertir datos', 'categóricos a numéricos (One-hot encoding,', 'Label encoding) •Normalización o estandarización', '•Agrupar, unir o dividir datasets', '•Creación de nuevas variables •Herramientas:', 'pandas, sklearn.preprocessing 4.Almacenamiento y gestión', '•Bases de datos SQL (PostgreSQL,', 'MySQL) o NoSQL (MongoDB) •Data', 'lakes, warehouses •Herramientas: SQLAlchemy, MongoDB,', 'BigQuery, Azure, AWS Procesamiento de', 'datos 5.Visualización exploratoria (EDA -', 'Exploratory Data Analysis) •Detectar patrones,', 'tendencias, anomalías •Graficar distribuciones, correlaciones', '•Herramientas: matplotlib, seaborn, plotly, Tableau', '6.Modelado y análisis predictivo (Machine', 'Learning) •Aplicación de algoritmos para', 'clasificar, predecir o agrupar datos', '•Evaluación del rendimiento del modelo', '•Herramientas: scikit-learn, XGBoost, TensorFlow, PyTorch', 'Procesamiento de datos Fases del', 'procesamiento de datos Objetivo final', 'en Ciencia de Datos •', 'El procesamiento de datos permite', 'que los modelos y análisis', 'se basen en datos confiables', 'y útiles, aumentando la precisión', 'y calidad de las decisiones', 'o predicciones. Procesamiento de datos', 'Fases del procesamiento de datos', 'Ejemplos Procesamiento de datos Fases', 'del procesamiento de datos import', 'pandas as pd # Cargar', "datos df = pd.read_csv('datos.csv') #", 'Ver primeras filas print(df.head()) #', 'Eliminar duplicados df = df.drop_duplicates()', "# Rellenar valores nulos df['edad']", "= df['edad'].fillna(df['edad'].mean()) # Convertir columna", "categórica a numérica df['genero'] =", "df['genero'].map({'M': 0, 'F': 1}) #", 'Mostrar estadística descriptiva print(df.describe()) Ejemplo', 'rápido en Python (limpieza +', 'análisis básico) Objetivo Proyecto: Análisis', 'de Ventas en una Tienda', 'Online Explorar y procesar datos', 'de ventas para: •Conocer los', 'productos más vendidos •Identificar el', 'comportamiento de los clientes •Detectar', 'tendencias por categoría, día y', 'región •Limpieza de datos •Transformaciones', '•Análisis exploratorio (EDA) •Visualizaciones básicas', 'Procesamiento de datos Fases del', 'procesamiento de datos Generación del', 'Dataset import pandas as pd', 'import numpy as np import', 'random from datetime import datetime,', 'timedelta # --- Simular datos', '--- np.random.seed(42) n = 1000', '# número de órdenes product_names', "= ['Laptop', 'Headphones', 'Smartphone', 'Monitor',", "'Keyboard', 'Mouse'] categories = ['Electronics',", "'Accessories'] regions = ['North', 'South',", "'East', 'West'] data = {", "'order_id': range(1, n+1), 'product_name': np.random.choice(product_names,", "n), 'price': np.random.uniform(20, 1000, n).round(2),", "'quantity': np.random.randint(1, 5, n), 'customer_id':", "np.random.randint(1000, 1100, n), 'region': np.random.choice(regions,", "n), 'order_date': [datetime(2024, 1, 1)", '+ timedelta(days=random.randint(0, 90)) for _', 'in range(n)] } df =', 'pd.DataFrame(data) # Categoría según producto', "df['category'] = df['product_name'].apply(lambda x: 'Electronics'", "if x in ['Laptop', 'Smartphone',", "'Monitor'] else 'Accessories') # Agregar", "product_id df['product_id'] = df.groupby('product_name').ngroup() Procesamiento", 'de datos Fases del procesamiento', 'de datos # Reordenar columnas', "df = df[['order_id', 'product_id', 'product_name',", "'category', 'price', 'quantity', 'customer_id', 'region',", "'order_date']] print(df.head()) Limpieza de datos", '# Verificar tipos de datos', 'print(df.dtypes) # Buscar valores nulos', 'print(df.isnull().sum()) # Eliminar duplicados si', 'hay df = df.drop_duplicates() #', 'Asegurar tipo datetime en la', "columna de fecha df['order_date'] =", "pd.to_datetime(df['order_date']) Transformaciones Útiles Agregamos una", 'columna con el total de', 'cada orden (precio * cantidad).', "df['total'] = df['price'] * df['quantity']", 'También podemos extraer información útil', 'como el mes o día', 'de la semana para análisis', "de tendencias: df['month'] = df['order_date'].dt.month", "df['weekday'] = df['order_date'].dt.day_name() Análisis Exploratorio", '(EDA) Productos más vendidos top_products', "= df.groupby('product_name')['quantity'].sum().sort_values(ascending=False) print(top_products) Ingresos por", "categoría revenue_by_category = df.groupby('category')['total'].sum().sort_values(ascending=False) print(revenue_by_category)", 'Análisis Exploratorio (EDA) Ventas por', "región sales_by_region = df.groupby('region')['total'].sum() print(sales_by_region)", 'Ingresos por mes monthly_revenue =', "df.groupby('month')['total'].sum() print(monthly_revenue) Procesamiento de datosTendencias", 'Procesamiento de datos 1. Automatización', 'del Aprendizaje Automático (AutoML) La', 'automatización de procesos de machine', 'learning está ganando protagonismo, permitiendo', 'que sistemas seleccionen modelos, ajusten', 'hiperparámetros y realicen ingeniería de', 'características de manera autónoma. Esto', 'facilita que equipos con menos', 'experiencia técnica implementen soluciones de', 'IA de forma eficiente. Procesamiento', 'de datos 2. Analítica Aumentada', 'La combinación de inteligencia artificial', 'y procesamiento de lenguaje natural', 'está simplificando el análisis de', 'datos, permitiendo que tanto usuarios', 'técnicos como no técnicos interactúen', 'con la información de manera', 'más efectiva y tomen decisiones', 'informadas. Procesamiento de datos 3.', 'Ética y Regulación en la', 'IA Con la creciente adopción', 'de la inteligencia artificial, surgen', 'debates sobre su regulación y', 'las implicaciones éticas, especialmente en', 'áreas como derechos de autor,', 'privacidad y sesgos en los', 'datos. Es esencial establecer marcos', 'que aseguren un uso responsable', 'y transparente de estas tecnologías.', 'Procesamiento de datos 4. Computación', 'en el Borde (Edge Computing)', 'La necesidad de procesar datos', 'en tiempo real ha impulsado', 'la adopción de la computación', 'en el borde, permitiendo análisis', 'más rápidos y reduciendo la', 'latencia al procesar datos cerca', 'de su origen. Procesamiento de', 'datos 5. Democratización del Acceso', 'a la IA Generativa La', 'IA generativa se ha vuelto', 'más accesible al público general,', 'permitiendo que personas sin conocimientos', 'técnicos profundos utilicen herramientas como', 'ChatGPT y generadores de imágenes', 'en diversas aplicaciones. Procesamiento de', 'datos Estas tendencias reflejan la', 'evolución constante en el procesamiento', 'de datos y la inteligencia', 'artificial, destacando la importancia de', 'la automatización, la ética, la', 'eficiencia y la accesibilidad en', 'el desarrollo y aplicación de', 'estas tecnologías. Técnico Superior en', 'Ciencia de Datos e Inteligencia', 'Artificial (TSCDIA) El procesamiento del', 'habla (speech processing) con enfoque', 'en ciencia de datos combina', 'técnicas de análisis de señales,', 'aprendizaje automático y lingüística computacional', 'para extraer valor de la', 'voz humana. Procesamiento del habla', '¿Qué es el Procesamiento del', 'Habla? Es el campo que', 'analiza, interpreta y transforma señales', 'de audio de la voz', 'humana en información estructurada que', 'puede ser utilizada por modelos', 'de ciencia de datos. Incluye', 'tareas como: •Reconocimiento automático del', 'habla (ASR) Automatic Speech Recognition', '•Análisis de emociones y tono', '•Conversión de voz a texto', 'y viceversa •Identificación de hablantes', '•Clasificación de intenciones •Mejora y', 'limpieza del audio Flujo típico', 'en un proyecto de ciencia', 'de datos con habla 1.Recolección', 'de audio: llamadas, notas de', 'voz, entrevistas, asistentes virtuales. 2.Preprocesamiento:', 'limpieza, eliminación de ruido, normalización.', '3.Extracción de características: MFCCs, espectrogramas,', 'pitch, energía, etc. 4.Análisis y', 'modelado: • Clasificación (emociones, intenciones)', '• Reconocimiento (voz a texto)', '• Clustering (patrones por hablante', 'o perfil) 5.Evaluación de modelos:', 'WER, F1, AUC, precisión, etc.', '6.Despliegue: dashboards, asistentes, integraciones en', 'apps Técnicas y herramientas clave', 'Categoría Ejemplos / Tecnologías Extracción', 'de características librosa, pyAudioAnalysis, openSMILE,', 'torchaudio Modelado clásico Random Forest,', 'SVM, HMM Deep Learning CNNs,', 'RNNs, Transformers (wav2vec, Whisper) Speech-to-Text', 'Whisper (OpenAI), Google Speech API,', 'Mozilla DeepSpeech Análisis de emociones', 'OpenSMILE + modelos supervisados Limpieza', 'de audio RNNoise, Wave-U-Net, Audacity', 'Aplicaciones con enfoque en ciencia', 'de datos �� E-commerce •Análisis', 'de llamadas a soporte: intención,', 'tono, satisfacción •Mejora de experiencias', 'con asistentes por voz ��', 'Salud •Detección de signos de', 'depresión, Parkinson o Alzheimer a', 'partir del habla •Registro automático', 'de dictado médico �� Educación', '•Evaluación automática de pronunciación •Tutores', 'virtuales personalizados con retroalimentación oral', '�� Finanzas / call centers', '•Monitoreo de calidad en llamadas', '•Alertas por cambios en tono', 'emocional (riesgo de cancelación) Procesamiento', 'del habla Integración con visualizaciones', '•Visualizar espectrogramas y características acústicas', '•Dashboards de: • Emociones predominantes', '• Volumen de llamadas por', 'tema • Conversión de voz', 'a texto con anotaciones semánticas', '➡ Herramientas: Power BI, Streamlit,', 'Plotly Dash, Tableau (con transcripciones)', 'Ejemplos de Procesamiento del Habla', '+ Ciencia de Datos Detección', 'temprana de enfermedades neurodegenerativas Contexto:', 'Análisis de voz de pacientes', 'para detectar señales tempranas de', 'Parkinson, Alzheimer o depresión. Datos:', 'Grabaciones de voz leyendo textos', 'o en conversación libre. Técnicas:', '•Extracción de MFCCs, pitch, jitter,', 'shimmer. •Clasificadores como Random Forest,', 'SVM, o modelos de Deep', 'Learning. •Detección de patrones en', 'la prosodia y fluidez. ¿Qué', 'son los MFCCs? Son una', 'representación numérica y compacta del', 'contenido espectral de un audio,', 'especialmente diseñada para simular cómo', 'el oído humano percibe el', 'sonido. Se usan ampliamente en', 'tareas como: •Reconocimiento de voz', '•Análisis de emociones •Identificación de', 'hablantes •Diagnóstico médico basado en', 'voz Ejemplos de Procesamiento del', 'Habla + Ciencia de Datos', 'Análisis de llamadas en e-commerce', '/ soporte técnico Contexto: Clasificar', 'el estado emocional del cliente', 'durante llamadas a un call', 'center. Técnicas: •Segmentación del audio', 'por turno de hablante. •Extracción', 'de características acústicas (energía, tono,', 'MFCCs). •Clasificación de emociones con', 'modelos supervisados. •Relación con satisfacción', 'del cliente (CSAT) o abandono.', '✅ Valor: Mejora de atención,', 'retención de clientes, priorización de', 'casos críticos. Ejemplos de Procesamiento', 'del Habla + Ciencia de', 'Datos Reconocimiento de intención en', 'asistentes virtuales Contexto: Extraer la', 'intención del usuario a partir', 'de comandos por voz (ej.', '"quiero cancelar mi pedido"). Técnicas:', '•Speech-to-Text con modelos como Whisper,', 'Google Speech API. •Procesamiento del', 'texto con NLP clásico o', 'Transformers. •Entrenamiento de modelos de', 'clasificación de intención. ✅ Valor:', 'Automatización de tareas, soporte 24/7,', 'personalización. ¿Qué es NLP? Es', 'una rama de la inteligencia', 'artificial (IA) que permite a', 'las computadoras entender, interpretar, generar', 'y responder al lenguaje humano.', 'Ejemplos de Procesamiento del Habla', '+ Ciencia de Datos Evaluación', 'oral automática en educación Contexto:', 'Evaluar la pronunciación y fluidez', 'de estudiantes aprendiendo un nuevo', 'idioma. Técnicas: •Alineación de texto', 'y voz (forced alignment). •Detección', 'de errores fonéticos, ritmo y', 'entonación. •Comparación con modelos de', 'referencia nativos. ✅ Valor: Evaluación', 'más justa y constante, feedback', 'inmediato al alumno. Ejemplos de', 'Procesamiento del Habla + Ciencia', 'de Datos Reconocimiento de canciones', 'o artistas por voz Contexto:', 'Apps como Shazam, identificación de', 'música o estilo a partir', 'del canto o tarareo. Técnicas:', '•Representación espectral (mel-espectrogramas, chroma, MFCCs).', '•Matching con base de datos', 'acústica usando fingerprinting. •Reducción dimensional', '+ clasificación. ✅ Valor: Experiencias', 'interactivas, marketing personalizado. Ejemplos de', 'Procesamiento del Habla + Ciencia', 'de Datos Autenticación biométrica por', 'voz (Speaker ID/Verification) Contexto: Confirmar', 'identidad del usuario a partir', 'de una frase hablada. Técnicas:', '• Embeddings de voz (x-vectors,', 'i-vectors). • Modelos tipo Siamese', 'networks, Triplet loss. • Detección', 'de spoofing con redes anti-fraude.', '✅ Valor: Seguridad en acceso', 'a sistemas sensibles sin contraseña.', 'Ejemplos de Procesamiento del Habla', '+ Ciencia de Datos Herramientas', 'comunes usadas en estos ejemplos', 'Categoría Herramientas Extracción de audio', 'librosa, openSMILE, praat, torchaudio Speech-to-Text', 'OpenAI Whisper, Google Speech API,', 'DeepSpeech Modelado scikit-learn, PyTorch, TensorFlow,', 'HuggingFace Visualización Matplotlib, Seaborn, Streamlit,', 'Dash Ejemplos de Procesamiento del', 'Habla en el ámbito de', 'la Salud Procesamiento del habla', 'Detección temprana de Parkinson Problema:', 'Identificar síntomas motores tempranos como', 'la rigidez vocal. Técnicas: •Extracción', 'de características vocales: jitter, shimmer,', 'HNR, MFCCs. •Modelos de clasificación:', 'SVM, Random Forest, XGBoost. •Datasets', 'como UCI Parkinson’s Dataset. ✅', 'Valor: Diagnóstico no invasivo, seguimiento', 'a distancia. Procesamiento del habla', 'Evaluación de trastornos del habla', '(afasia, disartria) Problema: Evaluar objetivamente', 'el deterioro del habla tras', 'un ACV o ELA. Técnicas:', '•Análisis de fluidez, pausas, duración', 'silábica, prosodia. •Detección automática de', 'errores fonéticos. •Modelos de regresión', 'o clasificación por severidad. ✅', 'Valor: Apoyo a fonoaudiólogos, rehabilitación', 'personalizada. Detección de depresión a', 'partir de la voz Problema:', 'Evaluar el estado emocional y', 'la energía del paciente. Técnicas:', '•Extracción de MFCCs, pitch, velocidad', 'de habla, entonación. •Modelos supervisados', '(Logistic Regression, Deep Learning). •Evaluación', 'en contextos reales (ej. llamadas', 'de seguimiento). ✅ Valor: Cribado', 'temprano, seguimiento de pacientes de', 'salud mental. Detección de depresión', 'a partir de la voz', 'Problema: Evaluar el estado emocional', 'y la energía del paciente.', 'Técnicas: •Extracción de MFCCs, pitch,', 'velocidad de habla, entonación. •Modelos', 'supervisados (Logistic Regression, Deep Learning).', '•Evaluación en contextos reales (ej.', 'llamadas de seguimiento). ✅ Valor:', 'Cribado temprano, seguimiento de pacientes', 'de salud mental. Detección de', 'Alzheimer por patrones de habla', 'espontánea Problema: Identificar deterioro cognitivo', 'mediante análisis semántico y fonológico.', 'Técnicas: •Análisis combinado de voz', '+ texto transcrito. •Detección de', 'pausas, repetición de palabras, desorganización.', '•Modelos NLP + características acústicas.', '✅ Valor: Detección temprana con', 'solo unos minutos de grabación.', 'Monitoreo de desarrollo del lenguaje', 'en niños Problema: Evaluar si', 'el desarrollo del lenguaje está', 'dentro del rango esperado. Técnicas:', '•Análisis de duración de sílabas,', 'diversidad léxica, fonemas. •Comparación con', 'perfiles estándar por edad. •Detección', 'de dislalias o retraso del', 'habla. ✅ Valor: Intervención temprana,', 'soporte a fonoaudiología. Técnicas y', 'herramientas más comunes Categoría Herramientas', 'utilizadas Extracción de características openSMILE,', 'librosa, praat, torchaudio Modelos ML/IA', 'scikit-learn, XGBoost, TensorFlow, PyTorch Evaluación', 'clínica Escalas clínicas + métricas', 'de modelo (AUC, Recall) Datasets', 'frecuentes UCI Parkinson, AVEC, DementiaBank,', 'Coswara, DAIC-WOZ Detección de Parkinson', 'mediante voz Ejemplos de Procesamiento', 'del Habla en Call Centers', 'Análisis de emociones en llamadas', 'Objetivo: Identificar el estado emocional', 'del cliente (enojado, frustrado, calmado).', 'Técnicas: •Extracción de características acústicas:', 'pitch, energía, MFCCs, tempo. •Modelos', 'supervisados (Random Forest, XGBoost) o', 'redes neuronales. •Clasificación de emociones', 'a nivel de turno, segmento', 'o llamada. ✅ Valor: Detectar', 'llamadas críticas en tiempo real,', 'escalar a un supervisor, priorizar', 'feedback. Reconocimiento automático del habla', '(ASR) Objetivo: Convertir voz en', 'texto para análisis posterior. Técnicas:', '•Speech-to-Text con Whisper (OpenAI), Google', 'Speech API, DeepSpeech. •Preprocesamiento: eliminación', 'de ruido, diarización (quién habla', 'cuándo). •Segmentación por agente/cliente. ✅', 'Valor: Transcripciones automáticas, reducción de', 'costos de auditoría, input para', 'NLP. Análisis de intención del', 'cliente Objetivo: Detectar qué desea', 'el cliente (cancelar, reclamar, pagar).', 'Técnicas: •Transcripción + clasificación de', 'intención (NLP). •Fine-tuning de modelos', 'tipo BERT o DistilBERT. •Detección', 'de palabras clave o patrones', 'semánticos. ✅ Valor: Derivación automática', 'a la solución adecuada, mejora', 'en tiempos de respuesta. Dashboards', 'de métricas de calidad y', 'sentimiento Objetivo: Visualizar tendencias por', 'emoción, agente, región o campaña.', 'Técnicas: •Integración de modelos de', 'emoción + speech-to-text. •Visualización en', 'Power BI, Tableau, Dash, Metabase.', '•Detección de "palabras detonantes" o', 'términos negativos. ✅ Valor: Mejora', 'del desempeño de agentes, auditorías', 'más eficientes, alertas tempranas. Análisis', 'de cumplimiento y guión Objetivo:', 'Validar si el agente siguió', 'el protocolo o leyó los', 'disclaimers obligatorios. Técnicas: •Alineación semántica', 'de texto vs. guión esperado.', '•Similitud textual (TF-IDF, cosine similarity)', 'o modelos de similitud semántica.', '•Alarmas por omisiones. ✅ Valor:', 'Reducción de riesgos regulatorios, aseguramiento', 'de calidad. Identificación del hablante', '(Speaker diarization + ID) Objetivo:', 'Distinguir automáticamente agente y cliente.', 'Técnicas: • Diarización con herramientas', 'como pyannote.audio o webrtcvad. •', 'En proyectos más avanzados: identificación', 'biométrica de hablantes. ✅ Valor:', 'Análisis independiente de comportamiento del', 'agente y del cliente. Procesamiento', 'del habla Herramientas comunes en', 'este tipo de proyectos Categoría', 'Herramientas recomendadas ASR (voz a', 'texto) Whisper, Google Speech-to-Text, AWS', 'Transcribe, DeepSpeech Procesamiento de audio', 'librosa, pyAudioAnalysis, torchaudio, openSMILE Emociones/tono', 'Praat, pyworld, openSMILE + modelos', 'sklearn/pytorch NLP posterior spaCy, HuggingFace,', 'BERT, NLTK Visualización Power BI,', 'Tableau, Plotly Dash, Grafana Flujos', 'automáticos Airflow, Zapier, Rasa (NLP', 'conversacional) Análisis de Emociones en', 'Llamadas de Call Center Ejemplos', 'de Procesamiento del Habla en', 'Educación Evaluación automática de la', 'pronunciación Problema: ¿Cómo dar retroalimentación', 'a un estudiante que está', 'aprendiendo un idioma sin requerir', 'un evaluador humano? Solución: •El', 'estudiante habla una frase (por', 'ejemplo en inglés). •Se extraen', 'características fonéticas y se comparan', 'con un modelo nativo. •Se', 'generan puntuaciones de precisión fonética,', 'ritmo, entonación. �� Técnicas: •MFCCs,', 'forced alignment, dynamic time warping.', '•Modelos supervisados entrenados con grabaciones', 'de hablantes nativos. ✅ Ejemplo', 'real: Duolingo aplica modelos de', 'voz para retroalimentación en ejercicios', 'orales. Reconocimiento de lectura en', 'voz alta Problema: ¿El estudiante', 'leyó el texto completo correctamente?', 'Solución: •Se transcribe la lectura', 'usando ASR (voz a texto).', '•Se compara el texto leído', 'con el texto esperado. •Se', 'identifican errores de omisión, pronunciación', 'o repeticiones. �� Técnicas: •Google', 'Speech-to-Text, Whisper, análisis de errores', 'fonéticos. •Métricas como WER (Word', 'Error Rate). ✅ Valor: Apoyo', 'a docentes para revisar ejercicios', 'orales masivamente. Seguimiento del desarrollo', 'del lenguaje en niños Problema:', '¿Un niño está adquiriendo el', 'lenguaje de forma típica para', 'su edad? Solución: •Se graban', 'interacciones verbales (por ejemplo en', 'el aula). •Se extraen métricas', 'como duración media de frases,', 'riqueza léxica, claridad fonética. •Se', 'comparan con modelos de desarrollo', 'infantil. �� Herramientas: openSMILE, librosa,', 'praat, embeddings de voz +', 'NLP. ✅ Valor: Identificación temprana', 'de dislalias, dislexia o TEA', '(trastorno del espectro autista). Dashboards', 'para monitoreo de habilidades orales', 'Problema: ¿Cómo monitorear el progreso', 'de decenas de estudiantes en', 'habilidades de expresión oral? Solución:', '•Se analiza el audio de', 'cada estudiante (pronunciación, fluidez, emociones).', '•Se agrupan métricas por alumno,', 'fecha, tipo de actividad. •Se', 'visualiza en un dashboard (ej.', 'Power BI, Streamlit). �� Herramientas:', 'librosa + sklearn + Streamlit', '/ Tableau. ✅ Valor: Visibilidad', 'para el docente + feedback', 'personalizado. Asistentes de práctica oral', 'por voz (EdTech) Problema: ¿Cómo', 'puede un estudiante practicar hablar', 'fuera del aula? Solución: •Apps', 'o plataformas que escuchan la', 'voz del estudiante, evalúan su', 'respuesta, y le dan feedback.', '•Por ejemplo: tutor oral de', 'inglés que corrige en tiempo', 'real. �� Herramientas: •NLP +', 'TTS + ASR + scoring', 'automático •Frameworks como Rasa o', 'Dialogflow + modelos de pronunciación', '✅ Ejemplo: Apps como Elsa', 'Speak, Google Read Along. Herramientas', 'útiles para estos proyectos Categoría', 'Herramientas comunes Procesamiento de voz', 'librosa, openSMILE, praat, torchaudio Voz', 'a texto (ASR) Whisper, Google', 'Speech-to-Text, Azure, DeepSpeech Evaluación fonética', 'Montreal Forced Aligner, Prosodylab-Aligner Visualización', 'educativa Streamlit, Power BI, Dash,', 'Grafana Análisis de Pronunciación Simulada', 'en Educación Ejemplos de Procesamiento', 'del Habla en e-commerce Asistentes', 'virtuales por voz (Voice Commerce)', 'Problema: ¿Cómo permitir que los', 'clientes compren, consulten o devuelvan', 'productos usando solo su voz?', 'Solución: •Uso de asistentes como', 'Alexa, Google Assistant o bots', 'propios. •Reconocimiento de voz →', 'detección de intención → respuesta', 'automática. •Conversaciones estructuradas como flujos', 'de tareas. �� Técnicas: •ASR', '(Whisper, Google STT) •NLP (BERT,', 'Rasa, Dialogflow) •Clasificación de intención', '+ búsqueda de productos ✅', 'Valor: Canales de compra manos', 'libres, experiencias inclusivas, fidelización. Análisis', 'de llamadas post-venta o reclamos', 'Problema: ¿Qué piensan realmente los', 'clientes después de comprar? Solución:', '•Transcripción de llamadas + análisis', 'de sentimiento/emoción. •Detección de temas', 'recurrentes (ej. devoluciones, entrega tardía).', '•Identificación de clientes insatisfechos. ��', 'Técnicas: •Voz a texto +', 'análisis de emociones (OpenSMILE, librosa)', '•Topic modeling (LDA) o clasificación', 'temática •Dashboards de insights ✅', 'Valor: Mejora continua del servicio', 'y productos, retención de clientes.', 'Evaluación de calidad de atención', 'telefónica Problema: ¿Los agentes siguen', 'el guion? ¿Tienen buena entonación', 'y empatía? Solución: •Análisis de', 'las conversaciones con métricas acústicas.', '•Comparación con plantillas ideales. •Evaluación', 'automática por batch. �� Técnicas:', '•Similaridad semántica (TF-IDF, BERT embeddings)', '•Extracción de MFCCs, tono, tempo,', 'energía •Modelos de scoring por', 'claridad, empatía, cumplimiento ✅ Valor:', 'Auditoría eficiente de calidad, mejora', 'de entrenamiento de agentes. Recomendaciones', 'de productos por voz Problema:', '¿Cómo recomendar productos en una', 'conversación con lenguaje natural? Solución:', '•Extraer intención y atributos de', 'la voz ("quiero unas zapatillas', 'negras para correr"). •Enlazar con', 'motor de recomendación o búsqueda', 'vectorial. •Responder con una selección', 'personalizada. �� Herramientas: •ASR +', 'NLP + motor de búsqueda', 'semántica (ej. Elasticsearch, FAISS) ✅', 'Valor: Incremento de conversiones, personalización', 'en tiempo real. Automatización de', 'devoluciones y seguimiento por voz', 'Problema: ¿Cómo facilitar procesos post-compra', 'desde un canal de voz?', 'Solución: •Bot de voz que', 'entienda solicitudes como “Quiero devolver', 'mi pedido” o “Dónde está', 'mi paquete”. •Enlace con sistema', 'logístico y CRM. �� Herramientas:', '•Whisper, Rasa, Dialogflow + integración', 'con API de órdenes ✅', 'Valor: Reducción de carga operativa,', 'experiencia fluida del cliente. Herramientas', 'clave Categoría Herramientas útiles Voz', 'a texto (ASR) Whisper, Google', 'STT, Amazon Transcribe Procesamiento acústico', 'librosa, openSMILE, pyAudioAnalysis NLP +', 'intención spaCy, BERT, Rasa, Dialogflow,', 'LangChain Análisis emocional Praat, openSMILE,', 'DeepMoji Visualización Power BI, Streamlit,', 'Tableau Análisis de Emociones en', 'Llamadas de Post-Venta (E Commerce)', 'Tendencias Actuales del Procesamiento del', 'Habla en Ciencia de Datos', 'Uso de modelos preentrenados (Foundation', 'Models de voz) •Modelos como', 'Whisper (OpenAI), Wav2Vec 2.0 (Meta),', 'HuBERT, SpeechBrain permiten: • Transcripción', 'multilingüe • Representaciones acústicas (embeddings)', '• Transferencia de aprendizaje para', 'tareas personalizadas ✅ Impacto: Acelera', 'el desarrollo con pocos datos', 'específicos, adaptable a cualquier dominio.', 'Reconocimiento de emociones y estado', 'afectivo •Análisis no solo de', 'lo que se dice, sino', 'cómo se dice. •Clasificación de', 'tono emocional: enojo, alegría, tristeza,', 'neutral, estrés, ironía. �� Técnicas:', 'MFCCs + redes neuronales, openSMILE,', 'audio transformers. ✅ Aplicaciones: salud', 'mental, atención al cliente, análisis', 'de rendimiento académico. Fusión de', 'voz + texto + video', '(multimodalidad) •Sistemas más robustos combinan:', '• Audio (tono, timbre) •', 'Texto transcrito (contenido semántico) •', 'Imagen/video (expresión facial, gestos) ✅', 'Aplicaciones: tutorías virtuales, reclutamiento, robótica', 'afectiva.'];

// Duraciones exactas de cada audio individual (en segundos)
const duracionesAudios = [2712, 2544, 2592, 2136, 2952, 2640, 3600, 3072, 3336, 2904, 2208, 2472, 3000, 5016, 3192, 3456, 3144, 4680, 5040, 3312, 6672, 6816, 4776, 4992, 2928, 4656, 5592, 5184, 3840, 4296, 4800, 3672, 4104, 7392, 4896, 5472, 7848, 4944, 5016, 4680, 6384, 6000, 5160, 3936, 4032, 3072, 7752, 2976, 3408, 1872, 2952, 2280, 2688, 3240, 2376, 3552, 2928, 3360, 3000, 2976, 9264, 5472, 6456, 4512, 8976, 4992, 8976, 6864, 3408, 4992, 2112, 3144, 2928, 3912, 3864, 3408, 5016, 5280, 2976, 3288, 3072, 3048, 3456, 3984, 6816, 4224, 5712, 4968, 5208, 3120, 14448, 9672, 10248, 12312, 8496, 8856, 3744, 6768, 10920, 3984, 4968, 13536, 2880, 3528, 9336, 6600, 6696, 3192, 6792, 7896, 6384, 2712, 5904, 10200, 2088, 3696, 8496, 3504, 1920, 2424, 10248, 11568, 4776, 16464, 19680, 4200, 15000, 3960, 12480, 4056, 5088, 3360, 4248, 3864, 3456, 3624, 2664, 4008, 3744, 3288, 3672, 3072, 2808, 3720, 3360, 2352, 3072, 3672, 2232, 2616, 3720, 2664, 4104, 2520, 2472, 3816, 2832, 3120, 3840, 2928, 2856, 2592, 2664, 3192, 2544, 3024, 2952, 3960, 2184, 2520, 3048, 3432, 3912, 3408, 3720, 3048, 3336, 2472, 4104, 3912, 2856, 2712, 3504, 2904, 5616, 4080, 2568, 2832, 4416, 2136, 3288, 2424, 2112, 4128, 1680, 3168, 2736, 2904, 4488, 5232, 2736, 2496, 4104, 3960, 2928, 2280, 3576, 3480, 6648, 4872, 7920, 5520, 5712, 3336, 3480, 4416, 5952, 6792, 2904, 4392, 5616, 3936, 4416, 8400, 4344, 3672, 4152, 4464, 3120, 3216, 3696, 4656, 1992, 3384, 3816, 3816, 2496, 4392, 4512, 2520, 2808, 2424, 5112, 3456, 4608, 4248, 2016, 2760, 3168, 5544, 4200, 3000, 2856, 4632, 2616, 2952, 4512, 3096, 3144, 4608, 3960, 3384, 3264, 2496, 3288, 3624, 2952, 3720, 2424, 3120, 3864, 4176, 4008, 3000, 2424, 2928, 3960, 2736, 2448, 4608, 3096, 4728, 4656, 4536, 4416, 4368, 3720, 3816, 2232, 3312, 4392, 2760, 3216, 3240, 3504, 3600, 3048, 3672, 4752, 5136, 4248, 2472, 3768, 4536, 2688, 3000, 2976, 3576, 3024, 3120, 4440, 4248, 3096, 3552, 5760, 3144, 3000, 3168, 3192, 2688, 3576, 2496, 3048, 7776, 2568, 4800, 5976, 4776, 3168, 3504, 6432, 2712, 2952, 3240, 3456, 3672, 3168, 4368, 3264, 3000, 2952, 3024, 3720, 5712, 3720, 6240, 5520, 3096, 1752, 2832, 3672, 3816, 4416, 4512, 5976, 6432, 4752, 4824, 3288, 2856, 5952, 2256, 3096, 3936, 4464, 3648, 4512, 5040, 3696, 2328, 2688, 3168, 4776, 4368, 4800, 4416, 5064, 3600, 3648, 1680, 3912, 2328, 5184, 4392, 5088, 4032, 4416, 3912, 3024, 2664, 5256, 3648, 3720, 3384, 4944, 4296, 4728, 2784, 3120, 3336, 2736, 3216, 2904, 4800, 3456, 2760, 5304, 3528, 3912, 4776, 4872, 6936, 3264, 4704, 4896, 6528, 3288, 2400, 2928, 4392, 4608, 5064, 5592, 5328, 4176, 2784, 4680, 3120, 3456, 4008, 4560, 3528, 4680, 5904, 3696, 6096, 5208, 3168, 3648, 3984, 4320, 4632, 4920, 3552, 2688, 6072, 3096, 3144, 2256, 4704, 4272, 3672, 4488, 4032, 4224, 5232, 3768, 4608, 2976, 2544, 2400, 5880, 3144, 5544, 3072, 4272, 4392, 3480, 4104, 4080, 4008, 3480, 4344, 4416, 3840, 3312, 2832, 2952, 4200, 6264, 4152, 7368, 4512, 6840, 4632, 3984, 5400, 4176, 3024, 2688, 3216, 4680, 2160, 2856, 3720, 3192, 3000, 3624, 2400, 3768, 5496, 4080, 3960, 4512, 3840, 3576, 3480, 3432, 3288, 3624, 3456, 2376, 2448, 4080, 3840, 4176, 4176, 4800, 3216, 4128, 2832, 2304, 2712, 3384, 3936, 2808, 2784, 4416, 2880, 5352, 2736, 6168, 3216, 3888, 3024, 3672, 2592, 3696, 2016, 5496, 2688, 3240, 3360, 3984, 3576, 4632, 2400, 3936, 4392, 2880, 3432, 2520, 3264, 2952, 2880, 2520, 4080, 3912, 3864, 3600, 4536, 4176, 3192, 3360, 4824, 4848, 5280, 4992, 4104, 3960, 3312, 2952, 3216, 3240, 3696, 2616, 3696, 3624, 5280, 5016, 4752, 4056, 5904, 5160, 3648, 3408, 5976, 3168, 3576, 3384, 3384, 4488, 5880, 3792, 3168, 4800, 4368, 4896, 3840, 3360, 2928, 3912, 2952, 3888, 3624, 4176, 2952, 5544, 4464, 3528, 5496, 3720, 3960, 2664, 2952, 4008, 3048, 3072, 3072, 3048, 3624, 4704, 2928, 7992, 5112, 3216, 3048, 4488, 1968, 3048, 3840, 3360, 2976, 4008, 4656, 3288, 3864, 3888, 3312, 4848, 5064, 5832, 5376, 4536, 4416, 2880, 3456, 3480, 2280, 4008, 3048, 6456, 4824, 5568, 2856, 5592, 2640, 3936, 3336, 3432, 2328, 3096, 5424, 4440, 4656, 5784, 4368, 3360, 2472, 4776, 2640, 3912, 7200, 6192, 1176];

// Configuración de tiempos (en segundos)
// Cada frase se repite 5 veces en el audio principal
const REPETICIONES_POR_FRASE = 5;

// Calcular los tiempos de inicio de cada frase usando las duraciones reales
const tiemposInicio = [];
let tiempoAcumulado = 0;

for (let i = 0; i < textos_exposicion.length; i++) {
    tiemposInicio.push(tiempoAcumulado);
    // Cada audio se repite 5 veces, así que sumamos 5 veces su duración
    tiempoAcumulado += REPETICIONES_POR_FRASE * duracionesAudios[i];
}

// Variables globales
let audioElement;
let currentActivePhrase = -1;
let isScriptVisible = false;
let updateInterval;

// Variables para grabación de audio
let mediaRecorder;
let recordedChunks = [];
let recordedAudioBlob;
let recordedAudioUrl;
let recordingAudio;
let isRecording = false;
let isPlayingRecording = false;
let recordingTimer;
let recordingStartTime;

// Inicialización cuando se carga la página
document.addEventListener('DOMContentLoaded', function() {
    audioElement = document.getElementById('mainAudio');
    
    // Configurar volumen inicial al 30%
    audioElement.volume = 0.3;
    
    // Crear botones de frases
    createPhraseButtons();
    
    // Crear contenido del guión
    createScriptContent();
    
    // Configurar event listeners
    setupEventListeners();
    
    // Inicializar display de tiempo
    updateTimeDisplay();
});

// Crear botones para cada frase
function createPhraseButtons() {
    const buttonsContainer = document.getElementById('phraseButtons');
    
    textos_exposicion.forEach((texto, index) => {
        const button = document.createElement('button');
        button.className = 'phrase-btn';
        button.textContent = `${index + 1}. ${texto}`;
        button.onclick = () => jumpToPhrase(index);
        button.id = `phrase-btn-${index}`;
        
        buttonsContainer.appendChild(button);
    });
}

// Crear contenido del guión
function createScriptContent() {
    const scriptContainer = document.getElementById('scriptContent');
    
    textos_exposicion.forEach((texto, index) => {
        const textElement = document.createElement('div');
        textElement.className = 'script-text';
        textElement.textContent = `${index + 1}. ${texto}`;
        textElement.id = `script-text-${index}`;
        
        scriptContainer.appendChild(textElement);
    });
}

// Configurar todos los event listeners
function setupEventListeners() {
    // Event listeners del audio
    audioElement.addEventListener('timeupdate', updateCurrentPhrase);
    audioElement.addEventListener('loadedmetadata', updateTimeDisplay);
    audioElement.addEventListener('timeupdate', updateTimeDisplay);
    audioElement.addEventListener('play', startUpdateInterval);
    audioElement.addEventListener('pause', stopUpdateInterval);
    audioElement.addEventListener('ended', stopUpdateInterval);
    
    // Event listener para limpiar texto
    document.getElementById('clearTextBtn').addEventListener('click', clearUserText);
    
    // Event listener para mostrar/ocultar guión
    document.getElementById('toggleScriptBtn').addEventListener('click', toggleScript);
    
    // Event listeners para grabación de audio
    document.getElementById('recordBtn').addEventListener('click', toggleRecording);
    document.getElementById('playRecordingBtn').addEventListener('click', togglePlayRecording);
    document.getElementById('discardBtn').addEventListener('click', discardRecording);
}

// Saltar a una frase específica (al inicio de la primera repetición)
function jumpToPhrase(phraseIndex) {
    if (phraseIndex >= 0 && phraseIndex < tiemposInicio.length) {
        // Saltar exactamente al inicio de la primera repetición de la frase
        const targetTime = tiemposInicio[phraseIndex];
        audioElement.currentTime = targetTime;
        
        console.log(`Saltando a la frase ${phraseIndex + 1}: "${textos_exposicion[phraseIndex]}" en el tiempo ${targetTime.toFixed(2)}s`);
        
        // Si el audio no está reproduciéndose, iniciarlo
        if (audioElement.paused) {
            audioElement.play().catch(e => {
                console.log('Error al reproducir audio:', e);
            });
        }
        
        // Actualizar inmediatamente la frase activa
        setTimeout(() => {
            updateCurrentPhrase();
        }, 100); // Pequeño delay para asegurar que el tiempo se haya actualizado
    }
}

// Actualizar la frase activa basada en el tiempo actual
function updateCurrentPhrase() {
    const currentTime = audioElement.currentTime;
    let newActivePhrase = -1;
    
    // Encontrar la frase actual
    for (let i = 0; i < tiemposInicio.length; i++) {
        if (currentTime >= tiemposInicio[i]) {
            newActivePhrase = i;
        } else {
            break;
        }
    }
    
    // Solo actualizar si cambió la frase activa
    if (newActivePhrase !== currentActivePhrase) {
        // Remover clase activa del botón anterior
        if (currentActivePhrase >= 0) {
            const prevButton = document.getElementById(`phrase-btn-${currentActivePhrase}`);
            if (prevButton) {
                prevButton.classList.remove('active');
            }
        }
        
        // Agregar clase activa al botón actual
        if (newActivePhrase >= 0) {
            const currentButton = document.getElementById(`phrase-btn-${newActivePhrase}`);
            if (currentButton) {
                currentButton.classList.add('active');
            }
        }
        
        currentActivePhrase = newActivePhrase;
        
        // Actualizar el guión si está visible
        if (isScriptVisible) {
            updateScriptHighlight();
        }
    }
}

// Actualizar el resaltado del guión
function updateScriptHighlight() {
    // Remover todas las clases de resaltado
    document.querySelectorAll('.script-text').forEach(element => {
        element.classList.remove('current', 'highlight');
    });
    
    // Resaltar desde el inicio hasta la frase actual
    if (currentActivePhrase >= 0) {
        for (let i = 0; i <= currentActivePhrase; i++) {
            const scriptElement = document.getElementById(`script-text-${i}`);
            if (scriptElement) {
                if (i === currentActivePhrase) {
                    scriptElement.classList.add('current');
                } else {
                    scriptElement.classList.add('highlight');
                }
            }
        }
        
        // Hacer scroll al elemento actual
        const currentScriptElement = document.getElementById(`script-text-${currentActivePhrase}`);
        if (currentScriptElement) {
            currentScriptElement.scrollIntoView({ 
                behavior: 'smooth', 
                block: 'center' 
            });
        }
    }
}

// Actualizar display de tiempo
function updateTimeDisplay() {
    const currentTime = audioElement.currentTime || 0;
    const duration = audioElement.duration || 0;
    
    document.getElementById('currentTime').textContent = formatTime(currentTime);
    document.getElementById('duration').textContent = formatTime(duration);
}

// Formatear tiempo en MM:SS
function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = Math.floor(seconds % 60);
    return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
}

// Limpiar texto del usuario
function clearUserText() {
    const userTextArea = document.getElementById('userText');
    userTextArea.value = '';
    userTextArea.focus();
}

// Mostrar/ocultar guión
function toggleScript() {
    const scriptContent = document.getElementById('scriptContent');
    const toggleButton = document.getElementById('toggleScriptBtn');
    
    isScriptVisible = !isScriptVisible;
    
    if (isScriptVisible) {
        scriptContent.classList.remove('hidden');
        toggleButton.textContent = 'Ocultar Guión';
        updateScriptHighlight();
    } else {
        scriptContent.classList.add('hidden');
        toggleButton.textContent = 'Mostrar Guión';
    }
}

// Iniciar intervalo de actualización
function startUpdateInterval() {
    if (updateInterval) {
        clearInterval(updateInterval);
    }
    
    updateInterval = setInterval(() => {
        updateCurrentPhrase();
        updateTimeDisplay();
    }, 100); // Actualizar cada 100ms para mayor precisión
}

// Detener intervalo de actualización
function stopUpdateInterval() {
    if (updateInterval) {
        clearInterval(updateInterval);
        updateInterval = null;
    }
}

// Función para calibrar los tiempos manualmente si es necesario
function calibrateTimings() {
    // Esta función puede usarse para ajustar los tiempos manualmente
    // basándose en la duración real del audio
    console.log('Duración total del audio:', audioElement.duration);
    console.log('Tiempos calculados:', tiemposInicio);
    console.log('Duraciones individuales:', duracionesAudios);
    
    // Calcular duración total esperada
    const duracionTotalEsperada = duracionesAudios.reduce((total, duracion) => total + (duracion * REPETICIONES_POR_FRASE), 0);
    console.log('Duración total esperada:', duracionTotalEsperada, 'segundos');
    
    // Mostrar tabla de tiempos para cada frase
    console.table(textos_exposicion.map((texto, index) => ({
        frase: index + 1,
        texto: texto.substring(0, 50) + (texto.length > 50 ? '...' : ''),
        inicio: tiemposInicio[index].toFixed(2) + 's',
        duracionIndividual: duracionesAudios[index] + 's',
        duracionTotal: (duracionesAudios[index] * REPETICIONES_POR_FRASE).toFixed(2) + 's'
    })));
}

// Función de utilidad para debugging
function debugCurrentTime() {
    console.log('Tiempo actual:', audioElement.currentTime);
    console.log('Frase activa:', currentActivePhrase);
    console.log('Texto actual:', currentActivePhrase >= 0 ? textos_exposicion[currentActivePhrase] : 'Ninguna');
}

// Exportar funciones para uso en consola si es necesario
window.debugAudio = {
    calibrateTimings,
    debugCurrentTime,
    jumpToPhrase,
    tiemposInicio,
    textos_exposicion,
    duracionesAudios,
    REPETICIONES_POR_FRASE
};

// ============ FUNCIONES DE GRABACIÓN DE AUDIO ============

// Iniciar/detener grabación
async function toggleRecording() {
    if (!isRecording) {
        await startRecording();
    } else {
        stopRecording();
    }
}

// Iniciar grabación
async function startRecording() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        
        recordedChunks = [];
        mediaRecorder = new MediaRecorder(stream);
        
        mediaRecorder.ondataavailable = function(event) {
            if (event.data.size > 0) {
                recordedChunks.push(event.data);
            }
        };
        
        mediaRecorder.onstop = function() {
            recordedAudioBlob = new Blob(recordedChunks, { type: 'audio/webm' });
            recordedAudioUrl = URL.createObjectURL(recordedAudioBlob);
            
            // Crear elemento de audio para reproducir
            if (recordingAudio) {
                recordingAudio.pause();
                recordingAudio = null;
            }
            
            recordingAudio = new Audio(recordedAudioUrl);
            recordingAudio.addEventListener('ended', () => {
                updatePlayButton(false);
            });
            
            // Habilitar botones
            document.getElementById('playRecordingBtn').disabled = false;
            document.getElementById('discardBtn').disabled = false;
        };
        
        mediaRecorder.start();
        isRecording = true;
        recordingStartTime = Date.now();
        
        // Actualizar UI
        updateRecordingUI();
        startRecordingTimer();
        
    } catch (error) {
        console.error('Error al acceder al micrófono:', error);
        updateStatus('Error al acceder al micrófono');
    }
}

// Detener grabación
function stopRecording() {
    if (mediaRecorder && isRecording) {
        mediaRecorder.stop();
        
        // Detener el stream
        if (mediaRecorder.stream) {
            mediaRecorder.stream.getTracks().forEach(track => track.stop());
        }
        
        isRecording = false;
        stopRecordingTimer();
        updateRecordingUI();
        updateStatus('Grabación completada');
    }
}

// Reproducir/pausar grabación
function togglePlayRecording() {
    if (!recordingAudio) return;
    
    if (!isPlayingRecording) {
        recordingAudio.play();
        isPlayingRecording = true;
        updatePlayButton(true);
    } else {
        recordingAudio.pause();
        isPlayingRecording = false;
        updatePlayButton(false);
    }
}

// Descartar grabación
function discardRecording() {
    if (recordingAudio) {
        recordingAudio.pause();
        recordingAudio = null;
    }
    
    if (recordedAudioUrl) {
        URL.revokeObjectURL(recordedAudioUrl);
        recordedAudioUrl = null;
    }
    
    recordedAudioBlob = null;
    recordedChunks = [];
    isPlayingRecording = false;
    
    // Actualizar UI
    document.getElementById('playRecordingBtn').disabled = true;
    document.getElementById('discardBtn').disabled = true;
    updatePlayButton(false);
    updateStatus('Listo para grabar');
    updateRecordingTime('0:00');
}

// Actualizar UI de grabación
function updateRecordingUI() {
    const recordBtn = document.getElementById('recordBtn');
    
    if (isRecording) {
        recordBtn.textContent = '⏹️ Detener';
        recordBtn.classList.add('recording');
        updateStatus('Grabando...');
    } else {
        recordBtn.textContent = '🎤 Grabar';
        recordBtn.classList.remove('recording');
    }
}

// Actualizar botón de reproducir
function updatePlayButton(isPlaying) {
    const playBtn = document.getElementById('playRecordingBtn');
    
    if (isPlaying) {
        playBtn.textContent = '⏸️ Pausar';
    } else {
        playBtn.textContent = '▶️ Reproducir';
    }
}

// Actualizar estado de grabación
function updateStatus(status) {
    document.getElementById('recordingStatus').textContent = status;
}

// Actualizar tiempo de grabación
function updateRecordingTime(time) {
    document.getElementById('recordingTime').textContent = time;
}

// Iniciar temporizador de grabación
function startRecordingTimer() {
    recordingTimer = setInterval(() => {
        const elapsed = Math.floor((Date.now() - recordingStartTime) / 1000);
        const minutes = Math.floor(elapsed / 60);
        const seconds = elapsed % 60;
        updateRecordingTime(`${minutes}:${seconds.toString().padStart(2, '0')}`);
    }, 1000);
}

// Detener temporizador de grabación
function stopRecordingTimer() {
    if (recordingTimer) {
        clearInterval(recordingTimer);
        recordingTimer = null;
    }
}
