# RESUMEN PARA EL PARCIAL - TSCDIA
### Práctica Profesional IV - Año 2025
### Docente: Magister Hugo Damian Planiscig

---

Hola, ¿cómo están?  
Les comparto qué hacer foco para el parcial.  
Cualquier cosa me avisan.  
Saludos.

---

## **UNIDAD 1 - Procesamiento de Datos**

### **Fases del Procesamiento de Datos**

1. **Recolección de datos**
   - Orígenes: APIs, sensores IoT, bases de datos, web scraping, encuestas, archivos CSV/Excel
   - Herramientas: requests, pandas, beautifulsoup, SQL

2. **Limpieza de datos (Data Cleaning)**
   - Eliminar duplicados
   - Corregir errores
   - Tratar valores nulos o faltantes (NaN)
   - Normalizar formatos (fechas, unidades, etc.)
   - Herramientas: pandas, numpy, OpenRefine

3. **Transformación de datos (Data Wrangling o Munging)**
   - Convertir datos categóricos a numéricos (One-hot encoding, Label encoding)
   - Normalización o estandarización
   - Agrupar, unir o dividir datasets
   - Creación de nuevas variables
   - Herramientas: pandas, sklearn.preprocessing

4. **Almacenamiento y gestión**
   - Bases de datos SQL (PostgreSQL, MySQL) o NoSQL (MongoDB)
   - Data lakes, warehouses
   - Herramientas: SQLAlchemy, MongoDB, BigQuery, Azure, AWS

5. **Visualización exploratoria (EDA - Exploratory Data Analysis)**
   - Detectar patrones, tendencias, anomalías
   - Graficar distribuciones, correlaciones
   - Herramientas: matplotlib, seaborn, plotly, Tableau

6. **Modelado y análisis predictivo (Machine Learning)**
   - Aplicación de algoritmos para clasificar, predecir o agrupar datos
   - Evaluación del rendimiento del modelo
   - Herramientas: scikit-learn, XGBoost, TensorFlow, PyTorch

### **Objetivo Final en Ciencia de Datos**

El procesamiento de datos permite que los modelos y análisis se basen en datos confiables y útiles, aumentando la precisión y calidad de las decisiones o predicciones.

---

## **UNIDAD 2 - Procesamiento del Habla**

### **¿Qué es el Procesamiento del Habla?**

Es el campo que analiza, interpreta y transforma señales de audio de la voz humana en información estructurada que puede ser utilizada por modelos de ciencia de datos.

**Incluye tareas como:**
- Reconocimiento automático del habla (ASR - Automatic Speech Recognition)
- Análisis de emociones y tono
- Conversión de voz a texto y viceversa
- Identificación de hablantes
- Clasificación de intenciones
- Mejora y limpieza del audio

### **Flujo Típico en un Proyecto de Ciencia de Datos con Habla**

1. **Recolección de audio**: llamadas, notas de voz, entrevistas, asistentes virtuales
2. **Preprocesamiento**: limpieza, eliminación de ruido, normalización
3. **Extracción de características**: MFCCs, espectrogramas, pitch, energía, etc.
4. **Análisis y modelado**:
   - Clasificación (emociones, intenciones)
   - Reconocimiento (voz a texto)
   - Clustering (patrones por hablante o perfil)
5. **Evaluación de modelos**: WER, F1, AUC, precisión, etc.
6. **Despliegue**: dashboards, asistentes, integraciones en apps

### **3 Técnicas y Herramientas Clave (elegir al menos 3)**

#### **Categoría: Extracción de Características**
- **librosa**: biblioteca Python para análisis de audio
- **openSMILE**: extracción de características acústicas avanzadas
- **torchaudio**: procesamiento de audio con PyTorch

#### **Categoría: Speech-to-Text**
- **Whisper (OpenAI)**: modelo de reconocimiento de voz multilingüe
- **Google Speech API**: servicio cloud de transcripción
- **Mozilla DeepSpeech**: modelo de código abierto para STT

#### **Categoría: Modelado**
- **CNNs, RNNs, Transformers**: redes neuronales para análisis de audio
- **wav2vec**: modelo preentrenado para representaciones de audio
- **Random Forest, SVM, HMM**: modelos clásicos para clasificación

#### **Categoría: Análisis de Emociones**
- **OpenSMILE + modelos supervisados**: para clasificación emocional
- **Praat**: análisis fonético y prosódico
- **pyworld**: extracción de pitch y características vocales

#### **Categoría: Limpieza de Audio**
- **RNNoise**: reducción de ruido con redes neuronales
- **Wave-U-Net**: separación y limpieza de señales de audio
- **Audacity**: herramienta para edición y limpieza manual

### **Ventajas del Procesamiento del Habla**

1. **Conversión de voz en datos útiles**: Transforma grabaciones en datos estructurados para análisis
2. **Análisis de emociones y estados mentales**: Detecta emociones, estrés, entusiasmo o frustración
3. **Automatización de tareas repetitivas**: Automatiza soporte técnico, encuestas, evaluaciones orales
4. **Ahorro de tiempo y costos**: Procesa grandes volúmenes de voz más rápido que análisis manual
5. **Mejoras en accesibilidad**: Ayuda a personas con discapacidades mediante interfaces de voz
6. **Evaluación personalizada en educación**: Analiza pronunciación, ritmo y claridad con retroalimentación
7. **Generación de insights en tiempo real**: Dashboards que combinan voz, sentimiento e intención
8. **Aplicaciones en seguridad y biometría**: Autenticación y verificación de identidad por voz

---

## **UNIDAD 3 - Procesamiento de Imágenes**

### **¿Qué es?**

El procesamiento de imágenes es una disciplina dentro del campo de la informática y la inteligencia artificial que se ocupa de la adquisición, análisis, manipulación y transformación de imágenes digitales con el fin de extraer información útil.

### **¿Para qué sirve?**

- Automatizar tareas humanas como diagnóstico médico por imágenes, inspección visual industrial o vigilancia en tiempo real
- Detectar patrones complejos o sutiles no perceptibles por el ojo humano
- Enriquecer modelos de ciencia de datos con información visual
- Facilitar la toma de decisiones en tiempo real basada en evidencia visual

### **¿Por qué es importante?**

Es relevante porque habilita a la inteligencia artificial para "ver", comprender y reaccionar frente a entornos visuales. Al procesar imágenes, se pueden construir soluciones automatizadas en sectores como salud, industria, seguridad, agricultura o ciudades inteligentes.

### **Conceptos Fundamentales**

- **Imagen digital**: representación numérica de una imagen bidimensional, compuesta por una matriz de píxeles
- **Píxel**: la unidad mínima de información visual que forma una imagen
- **Resolución**: número de píxeles contenidos en una imagen (definición espacial)
- **Profundidad de color**: cantidad de bits utilizados para representar el color de cada píxel
- **Espacios de color**: RGB, HSV, YCbCr, escala de grises
- **Ruido**: distorsión o variación indeseada en los valores de los píxeles
- **Transformaciones geométricas**: rotación, escalado, traslación

### **Objetivos**

- Transformar imágenes en datos estructurados y procesables
- Automatizar el análisis visual para mejorar la eficiencia
- Extraer características visuales que alimenten modelos predictivos
- Generar información explicativa y visualmente interpretativa
- Mejorar la precisión y confiabilidad en tareas visuales críticas

### **Alcance**

El procesamiento de imágenes impacta múltiples industrias:
- **Salud**: diagnóstico asistido por imágenes, segmentación de tejidos, planificación quirúrgica
- **Agricultura**: monitoreo de cultivos, predicción de rendimientos, detección de plagas
- **Industria**: control de calidad visual, mantenimiento predictivo, inspección robótica
- **Seguridad**: vigilancia automática, reconocimiento de personas y objetos
- **Transporte**: conducción autónoma, análisis de tráfico, visión en drones
- **Educación y cultura**: digitalización de documentos, clasificación de manuscritos

### **Etapas del Procesamiento de Imágenes**

1. **Adquisición**: captura de imágenes mediante sensores, cámaras, drones, escáneres o dispositivos médicos
2. **Preprocesamiento**: limpieza y mejora de la imagen (reducción de ruido, ajuste de contraste, normalización)
3. **Segmentación**: división de la imagen en regiones homogéneas (objetos, tejidos, zonas de interés)
4. **Extracción de características**: generación de vectores numéricos a partir de bordes, texturas, formas o patrones
5. **Modelado y análisis**: clasificación, regresión, agrupamiento o predicción mediante algoritmos de machine learning
6. **Visualización e interpretación**: creación de dashboards, mapas de calor, overlays, visualización 3D

### **3 Técnicas (elegir al menos 3)**

1. **Filtros y convoluciones**: detección de bordes, realce, suavizado
2. **Transformaciones geométricas**: rotación, escalado, recorte, warping
3. **Umbralado**: binarización de regiones
4. **Segmentación semántica**: asignación de etiquetas por píxel (ej. U-Net, DeepLab)
5. **Extracción de descriptores**: HOG, SIFT, SURF
6. **Redes neuronales convolucionales (CNN)**: aprendizaje profundo para clasificación y detección
7. **Transfer learning**: reutilización de modelos preentrenados (ResNet, MobileNet, EfficientNet)
8. **Explainable AI (XAI)**: interpretación visual de predicciones mediante Grad-CAM o LIME

### **Dónde se aplica**

- Detección de enfermedades en imágenes médicas: neumonía, cáncer, retinopatía diabética
- Inspección de calidad visual en manufactura: detección de grietas, deformaciones o imperfecciones
- Análisis de imágenes satelitales: clasificación del uso de suelo, detección de deforestación
- Reconocimiento facial: seguridad, autenticación, análisis de emociones
- Clasificación automática de imágenes: buscadores visuales, etiquetado automático
- Reconocimiento de escritura: OCR para textos manuscritos o impresos

### **Ventajas y Desventajas**

#### **Ventajas:**
- Reduce el error humano en tareas visuales
- Alta velocidad y escalabilidad
- Permite el análisis visual en tiempo real
- Mejora la eficiencia operativa y diagnóstica
- Se integra bien con pipelines de ciencia de datos

#### **Desventajas:**
- Costos computacionales elevados
- Dependencia de grandes volúmenes de datos etiquetados
- Complejidad en la interpretación de resultados
- Posible introducción de sesgo si los datos son limitados o poco representativos

### **3 Tecnologías y Herramientas (elegir al menos 3)**

#### **Bibliotecas:**
- **OpenCV**: biblioteca completa para visión computacional
- **Pillow**: manipulación básica de imágenes en Python
- **scikit-image**: algoritmos de procesamiento de imágenes

#### **Frameworks de Deep Learning:**
- **PyTorch**: framework flexible para redes neuronales
- **TensorFlow**: plataforma completa para IA
- **Keras**: API de alto nivel para redes neuronales

#### **Modelos y Arquitecturas:**
- **VGG**: arquitectura clásica de CNN
- **ResNet**: redes residuales profundas
- **U-Net**: segmentación semántica (imágenes médicas)
- **YOLO**: detección de objetos en tiempo real
- **EfficientDet**: detección eficiente de objetos

#### **Herramientas de Anotación:**
- **LabelImg**: anotación de bounding boxes
- **Roboflow**: plataforma completa de gestión de datos de visión
- **VGG Image Annotator**: anotación colaborativa
- **Supervisely**: plataforma enterprise de anotación

#### **Entornos:**
- **Google Colab**: notebooks gratuitos con GPU
- **Jupyter Notebook**: entorno interactivo de desarrollo
- **Kaggle**: plataforma de competiciones y datasets

#### **Visualización:**
- **Streamlit**: creación rápida de apps de ML
- **Dash**: dashboards interactivos
- **Power BI**: visualización empresarial

---

## **UNIDAD 4 - Creación de Modelos**

### **¿Qué es y para qué sirve?**

**¿Qué es?**  
Es la etapa en la que se construyen algoritmos (modelos matemáticos, estadísticos o de machine learning) que aprenden patrones a partir de los datos para hacer predicciones, clasificaciones o descubrir relaciones.

**¿Para qué sirve?**  
Sirve para transformar datos en conocimiento útil que permita:
- **Predecir el futuro**: proyectar ventas, churn, demanda
- **Clasificar situaciones**: diagnóstico médico, filtro de spam
- **Detectar anomalías**: fraudes, fallos de maquinaria
- **Recomendar acciones**: productos, películas, contenido
- **Automatizar decisiones**: aprobaciones de crédito, ajuste de precios
- **Optimizar recursos**: ruteo, asignación de personal, inventarios
- **Descubrir patrones ocultos**: segmentación, tendencias

### **Objetivos**

- Extraer valor predictivo de los datos
- Automatizar decisiones
- Detectar patrones ocultos
- Optimizar procesos
- Reducir riesgos
- Apoyar estrategias de negocio basadas en datos

### **Alcance**

- Desde la formulación del problema hasta el despliegue en producción
- Limitado por calidad y disponibilidad de datos
- Alcance técnico: clasificación, regresión, agrupamiento, recomendación, detección de anomalías
- Alcance ético y legal: privacidad, equidad, transparencia (GDPR, bias reduction)
- Monitoreo continuo: evitar data drift y mantener precisión

### **Tipos Comunes de Modelos**

#### **Modelos Supervisados (con etiquetas conocidas):**
- **Clasificación**: Árboles, Random Forest, SVM, Redes Neuronales
- **Regresión**: Regresión Lineal, Ridge, Lasso

#### **Modelos No Supervisados (sin etiquetas):**
- **Agrupamiento**: K-means, DBSCAN
- **Reducción de dimensionalidad**: PCA, t-SNE

#### **Modelos de Aprendizaje por Refuerzo:**
- Agentes que aprenden a través de recompensas y penalizaciones

### **Herramientas y Librerías Comunes**

#### **Python:**
- **Scikit-learn**: modelos clásicos (regresión, clasificación, clustering)
- **XGBoost**: boosting de árboles, alta performance
- **LightGBM**: boosting rápido para datasets grandes
- **CatBoost**: boosting optimizado para datos categóricos
- **TensorFlow**: deep learning, redes neuronales, visión computacional
- **Keras**: API sencilla sobre TensorFlow
- **PyTorch**: deep learning flexible, usado en investigación

#### **R:**
- caret, randomForest, xgboost

#### **Plataformas:**
- **AWS SageMaker**: plataforma integral para crear, entrenar y desplegar modelos
- **Azure ML**: desarrollo y gobernanza de proyectos de ML
- **Google Vertex AI**: entrenamiento, despliegue y gestión en la nube

### **Buenas Prácticas**

- Separar bien datos de entrenamiento y de prueba
- Evitar overfitting (el modelo memoriza pero no generaliza)
- Usar métricas apropiadas según el problema
- Hacer explicabilidad del modelo (SHAP, LIME)
- Documentar cada etapa del pipeline

### **Fases en la Creación de Modelos**

1. **Entendimiento del problema**: Definir qué se quiere resolver, alinear con objetivos de negocio
2. **Recolección de datos**: Identificar, recolectar y acceder a fuentes relevantes
3. **Preparación de los datos**: Limpieza, transformación, feature engineering
4. **Selección del modelo**: Elegir tipo según el problema
5. **Entrenamiento del modelo**: Ajustar parámetros con datos de entrenamiento
6. **Evaluación del modelo**: Medir desempeño con métricas específicas
7. **Optimización**: Ajustar hiperparámetros, mejorar features
8. **Validación final**: Validación cruzada o set de prueba externo
9. **Implementación/Despliegue**: Integrar en entorno real (API, aplicación)
10. **Monitoreo y mantenimiento**: Vigilar rendimiento y actualizar si hay data drift

### **¿Qué logra la aplicación de IA en la creación de modelos?**

- Reduce tiempos de desarrollo (semanas a horas)
- Disminuye errores humanos (automatiza tareas tediosas)
- Permite crear mejores modelos (más complejos, optimizados)
- Democratiza la ciencia de datos (personas no técnicas pueden construir modelos)
- Hace sostenibles los modelos (detecta y reentrena cuando baja la performance)

### **Mejores Prácticas en Creación de Modelos Aplicando IA**

- **Automatización del modelado (AutoML)**: H2O.ai, Google AutoML, PyCaret
- **Generación de features**: Featuretools, DataRobot
- **Selección automática de modelos**: TPOT, Auto-Sklearn
- **Optimización de hiperparámetros**: Optuna, Hyperopt
- **Análisis y explicabilidad**: SHAP, LIME, EBM
- **Entrenamiento distribuido**: Ray, Horovod
- **Mantenimiento automatizado**: MLOps inteligentes (SageMaker, Azure ML)

### **Diferencias entre Modelado Tradicional vs Modelado con IA**

#### **Modelado Tradicional:**
- Modelos clásicos (regresión, árboles, SVM, clustering)
- Feature engineering manual
- Mayor interpretabilidad
- Menor costo computacional
- Validación sistemática (validación cruzada, grid search)
- Base sólida para técnicas avanzadas

#### **Modelado con IA:**
- Automatización con AutoML
- Feature engineering automático
- Modelos más complejos (deep learning)
- Optimización inteligente de hiperparámetros
- Explicabilidad con XAI (SHAP, LIME)
- Entrenamiento distribuido
- Monitoreo y actualización automatizada

---

## **UNIDAD 5 - Post Procesamiento**

### **¿Qué es el Post Procesamiento en Ciencia de Datos?**

Es el conjunto de actividades que se realizan después de haber descubierto patrones, modelos o estructuras en un proceso de minería de datos o machine learning. Su objetivo es:
- Mejorar, interpretar, validar o integrar los resultados
- Prepararlos para su comunicación, explotación o acción inmediata

### **Objetivos del Post Procesamiento**

- **Interpretación**: Traducir hallazgos en conclusiones útiles para el negocio o el usuario final
- **Validación**: Asegurar que las estructuras descubiertas sean correctas, robustas y útiles
- **Optimización**: Mejorar la calidad de los modelos o patrones obtenidos
- **Acción y Automatización**: Integrar los resultados a flujos automáticos o sistemas productivos

### **Componentes Principales**

1. **Estructuras Descubiertas**: Modelos, patrones, reglas, segmentos de clientes, series de tendencias
2. **Visualización**: Representación gráfica para facilitar la comprensión (Tableau, Power BI, Matplotlib, Plotly)
3. **Actualización en Línea**: Modificación dinámica del modelo con nuevos datos en tiempo real (MLOps, Apache Kafka, AWS Sagemaker, TensorFlow Serving)

### **Flujo General del Post Procesamiento**

1. Recolección de Resultados (Modelos/Patrones)
2. Evaluación de Resultados
3. Validación y Optimización (Posible Reentrenamiento)
4. Visualización de Resultados para Interpretación
5. Generación de Reportes, Dashboards o Alarmas
6. Integración en sistemas productivos o plataformas
7. Actualización en Línea y Monitoreo Continuo

---

## **UNIDAD 6 - Elaboración de Informes y Responsabilidad**

### **Objetivos de la Elaboración de Informes**

- Comunicar resultados de manera clara y comprensible a diversos públicos
- Garantizar la trazabilidad y reproducibilidad de los procesos de análisis
- Evaluar el impacto ético, social y legal de los hallazgos
- Fomentar la transparencia y confianza en modelos automatizados
- Orientar la acción y toma de decisiones basadas en datos dentro de un marco responsable

### **Componentes Fundamentales de un Informe Responsable**

1. **Resumen Ejecutivo**: Síntesis orientada a tomadores de decisiones no técnicos
2. **Descripción del Problema y Contexto**: Enfoque en impacto social, legal, económico o ético
3. **Metodología**: Transparencia en los métodos, modelos y métricas utilizados
4. **Origen y Calidad de los Datos**: Documentación de fuentes, posibles sesgos, privacidad y legalidad
5. **Resultados**: Visualizaciones claras, interpretación honesta, cuantificación de incertidumbre
6. **Limitaciones y Sesgos**: Reconocimiento explícito de los límites del análisis
7. **Impacto Legal y Ético**: Evaluación de consecuencias potenciales
8. **Recomendaciones**: Acciones sugeridas desde perspectiva técnica, ética y social

### **Responsabilidad Legal y Social**

#### **Aspectos Legales:**
- Cumplimiento de leyes de privacidad de datos (GDPR, LGPD, HIPAA)
- Consentimiento informado para uso de datos personales
- Protección ante uso indebido de algoritmos en decisiones automatizadas
- Registro y documentación legal de decisiones algorítmicas

#### **Aspectos Sociales:**
- Evitar la discriminación algorítmica (por raza, género, edad)
- Promover equidad y justicia social mediante uso responsable de la IA
- Incluir voces diversas en el análisis e interpretación
- Evaluar impacto en poblaciones vulnerables

### **Buenas Prácticas en la Comunicación**

- **Lenguaje claro y accesible**: Evitar jergas técnicas innecesarias
- **Visualización ética de datos**: No distorsionar percepciones con gráficas engañosas
- **Narrativa basada en evidencia**: Relato estructurado que respalde decisiones
- **Inclusión de audiencias diversas**: Comunicación adaptada a sectores afectados
- **Disponibilidad abierta y responsable**: Publicación bajo licencias abiertas con salvaguardas

### **Ventajas y Desventajas**

#### **Ventajas:**
- Transparencia para la toma de decisiones
- Confianza pública en el uso de IA
- Cumplimiento normativo y regulatorio
- Mitigación de sesgos y discriminación algorítmica
- Inclusión social y accesibilidad
- Mejora continua del modelo y su aceptación

#### **Desventajas/Riesgos:**
- Riesgo de malinterpretación
- Falta de explicabilidad en modelos complejos
- Sobrecarga documental
- Falta de estándares universales
- Exposición de vulnerabilidades
- Riesgo reputacional si se comunican errores sin cuidado

### **Mejores Prácticas Recomendadas**

#### **Contenido del Informe:**
- Incluir resumen ejecutivo claro y orientado a no técnicos
- Documentar fuentes de datos, criterios de limpieza y posibles sesgos
- Explicar metodología del modelo con detalle suficiente

#### **Enfoque Legal y Ético:**
- Confirmar cumplimiento de normativas (GDPR, HIPAA)
- Documentar consentimiento informado y derechos de los titulares de datos
- Incluir sección de impacto legal y ético con evaluación de riesgos

#### **Claridad y Adaptabilidad:**
- Usar lenguaje sencillo para públicos generales
- Incluir visualizaciones comprensibles
- Traducir informes a idiomas o formatos accesibles

#### **Transparencia y Explicabilidad:**
- Aplicar técnicas XAI (SHAP, LIME) y visualizarlas
- Publicar "model cards" y "data sheets"
- Indicar cómo se interpretan los resultados y su margen de error

#### **Participación y Responsabilidad Social:**
- Incluir representantes de comunidades afectadas en la validación
- Comunicar públicamente resultados si impactan a la ciudadanía
- Crear canales de retroalimentación

### **Alcance de la Responsabilidad Legal**

**Objetivo:** Asegurar cumplimiento de leyes que protejan derechos individuales y colectivos

**Ámbitos clave:**
- Protección de Datos Personales (GDPR, CCPA, LGPD, HIPAA)
- Transparencia Algorítmica en decisiones automatizadas
- Responsabilidad Civil y Penal ante errores o sesgos
- Auditoría y Trazabilidad (documentación de cambios)

### **Alcance de la Responsabilidad Social**

**Objetivo:** Garantizar que los proyectos de IA no perpetúen injusticias sociales

**Ámbitos clave:**
- Impacto en Grupos Vulnerables (métricas de equidad)
- Acceso Equitativo a la Información (multiformato, idiomas)
- Responsabilidad Institucional (asumir consecuencias no deseadas)
- Participación Pública y Ciudadana (canales de consulta)

### **Alcance de la Responsabilidad Ética**

**Objetivo:** Asegurar que el uso de IA respete principios morales fundamentales

**Ámbitos clave:**
- Transparencia y Explicabilidad Ética
- Justicia y No Discriminación
- Autonomía y Consentimiento Informado
- Beneficencia y No Maleficencia
- Rendición de Cuentas Ética

---

## **RESUMEN VISUAL DE RESPONSABILIDADES**

| Tipo de Responsabilidad | Alcance |
|------------------------|---------|
| **Legal** | Protección de datos, decisiones automatizadas, derechos individuales, cumplimiento normativo |
| **Social** | Inclusión, equidad, impacto comunitario, accesibilidad y participación pública |
| **Ética** | Justicia, transparencia moral, consentimiento, reducción de daño y rendición de cuentas |

---

**¡Éxitos en el parcial!**
