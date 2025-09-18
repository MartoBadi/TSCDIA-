# Time Series Model Testing Framework

## 📋 Descripción

Este framework implementa tests completos para determinar qué modelos de series de tiempo se pueden aplicar y seleccionar el que mejor se ajusta a los datos del dataset. 

Desarrollado específicamente para el análisis del dataset de e-commerce brasileño Olist, pero adaptable a cualquier serie de tiempo.

## 🎯 Objetivo

Crear un sistema automatizado que:
- ✅ Evalúe múltiples modelos de series de tiempo
- ✅ Compare su desempeño con métricas estándar
- ✅ Seleccione automáticamente el mejor modelo
- ✅ Genere reportes y visualizaciones detalladas
- ✅ Proporcione recomendaciones para implementación

## 🔧 Modelos Implementados

| Modelo | Descripción | Casos de Uso |
|--------|-------------|--------------|
| **ARIMA** | Modelos autorregresivos integrados | Series con tendencia y patrones autorregresivos |
| **SARIMA** | ARIMA con estacionalidad | Series con patrones estacionales (ej: ventas semanales) |
| **Exponential Smoothing** | Suavizado exponencial (Holt-Winters) | Series con tendencia y/o estacionalidad |
| **Linear Regression** | Regresión lineal temporal | Series con tendencias lineales simples |
| **Moving Averages** | Medias móviles simples y exponenciales | Series relativamente estables |
| **Prophet** | Modelo de Facebook (opcional) | Series complejas con múltiples estacionalidades |

## 📊 Métricas de Evaluación

- **RMSE** (Root Mean Square Error): Error cuadrático medio - menor es mejor
- **MAE** (Mean Absolute Error): Error absoluto medio - menor es mejor  
- **MAPE** (Mean Absolute Percentage Error): Error porcentual - menor es mejor
- **R²** (Coeficiente de determinación): Calidad del ajuste - mayor es mejor
- **AIC/BIC** (Criterios de información): Para selección de modelos - menor es mejor

## 🚀 Instalación

### Requisitos
```bash
# Instalar dependencias principales
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels plotly

# Opcional: Para modelo Prophet
pip install prophet
```

### Verificar instalación
```python
python -c "import pandas, numpy, matplotlib, statsmodels; print('✅ Dependencias instaladas correctamente')"
```

## 📁 Estructura de Archivos

```
TSCDIA-/
├── time_series_model_testing.py      # Framework principal
├── ejecutar_analisis_rapido.py       # Script de ejecución rápida
├── analisis_modelos_series_tiempo.ipynb  # Jupyter Notebook interactivo
├── README_TIME_SERIES.md             # Este archivo
└── proyecto_integrador/tp/data/      # Datos de Olist
    ├── olist_orders_dataset.csv
    ├── olist_order_payments_dataset.csv
    └── (otros archivos CSV)
```

## 🎮 Formas de Uso

### 1. Ejecución Rápida (Recomendado)
```bash
python ejecutar_analisis_rapido.py
```

**Ventajas:**
- ✅ Ejecución automática completa
- ✅ Resultados en consola
- ✅ Genera archivos de salida automáticamente

### 2. Script Completo
```bash
python time_series_model_testing.py
```

### 3. Jupyter Notebook (Interactivo)
```bash
jupyter notebook analisis_modelos_series_tiempo.ipynb
```

**Ventajas:**
- ✅ Exploración paso a paso
- ✅ Visualizaciones interactivas
- ✅ Análisis personalizable

## 📈 Ejemplo de Uso Programático

```python
from time_series_model_testing import TimeSeriesModelTester

# Crear instancia
tester = TimeSeriesModelTester()

# Cargar datos
df = tester.load_olist_data()

# Preparar serie de tiempo
ts = tester.prepare_time_series(df, 'orders_count')

# Dividir datos
train, test = tester.split_data(test_size=0.2)

# Ejecutar todos los tests
results = tester.run_all_tests()

# Encontrar mejor modelo
best_model, metrics = tester.find_best_model()

# Generar reporte
report = tester.generate_report()
```

## 📊 Archivos de Salida

Después de la ejecución, se generan automáticamente:

| Archivo | Descripción |
|---------|-------------|
| `time_series_analysis_results.png` | Visualizaciones completas de resultados |
| `time_series_analysis_report.txt` | Reporte detallado con recomendaciones |

### Ejemplo de Visualizaciones

El archivo PNG incluye:
1. **Serie temporal original** con división train/test
2. **Comparación de predicciones** de todos los modelos
3. **Métricas de error** por modelo
4. **R² Score** comparativo

## 🏆 Interpretación de Resultados

### Tabla de Métricas de Ejemplo:
```
Modelo                 RMSE    MAE     MAPE    R²
EMA_0.5               73.02   58.81   50.00   -0.001
SARIMA(1,1,1)(1,1,1,7) 84.92   68.84   45.36   -0.354
Linear_Regression     104.17   85.14   81.94   -1.038
```

### Interpretación:
- **Mejor modelo**: EMA_0.5 (menor RMSE)
- **MAPE**: 50% indica error moderado
- **R²**: Negativo indica ajuste pobre (común en datos volátiles)

## 🎯 Casos de Uso Reales

### 1. E-commerce
- Predicción de ventas diarias
- Planificación de inventario
- Análisis de estacionalidad

### 2. Finanzas
- Predicción de flujo de caja
- Análisis de tendencias de mercado
- Gestión de riesgos

### 3. Operaciones
- Predicción de demanda
- Optimización de recursos
- Planificación de capacidad

## 🔧 Personalización

### Cambiar Dataset
```python
# Para usar datos personalizados
tester = TimeSeriesModelTester(data_path="mi_dataset.csv")

# Preparar con columna específica
ts = tester.prepare_time_series(df, 'mi_columna_temporal')
```

### Ajustar Parámetros
```python
# Cambiar proporción de prueba
train, test = tester.split_data(test_size=0.3)

# Ajustar estacionalidad
results = tester.run_all_tests(seasonal_period=30)  # Para datos mensuales
```

### Modelos Específicos
```python
# Probar solo ARIMA
arima_result = tester.test_arima_model(max_p=5, max_d=2, max_q=5)

# Probar solo Prophet
prophet_result = tester.test_prophet_model()
```

## 🐛 Solución de Problemas

### Error: "No module named 'pandas'"
```bash
pip install pandas numpy matplotlib statsmodels scikit-learn
```

### Error: "No se encontró el archivo"
Verificar que los datos estén en:
```
proyecto_integrador/tp/data/olist_orders_dataset.csv
```

### Error: "Prophet no está disponible"
```bash
pip install prophet
```

### Warnings de statsmodels
Son normales - indican optimizaciones automáticas del algoritmo.

## 📊 Datos de Ejemplo

El framework funciona con el dataset Olist que incluye:
- **612 observaciones diarias** (2016-2018)
- **Número de órdenes por día**
- **Ingresos por día** (opcional)
- **Patrones estacionales semanales**

## 🔄 Próximos Desarrollos

- [ ] Integración con MLflow para tracking
- [ ] Modelos de Deep Learning (LSTM, GRU)
- [ ] Validación cruzada temporal
- [ ] Dashboard interactivo con Streamlit
- [ ] API REST para predicciones en tiempo real

## 🤝 Contribuciones

Para contribuir al proyecto:
1. Fork el repositorio
2. Crear branch para feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push al branch (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## 📜 Licencia

Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.

## 📞 Soporte

Para preguntas o problemas:
- Crear un issue en GitHub
- Revisar la documentación en el código
- Consultar ejemplos en el Jupyter Notebook

---

**Desarrollado para TSCDIA - Tecnicatura Superior en Ciencia de Datos e IA**

🎓 *"Aplicando ciencia de datos para resolver problemas reales"*