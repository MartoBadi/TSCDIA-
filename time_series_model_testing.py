#!/usr/bin/env python3
"""
Time Series Model Testing Framework
===================================

Este script implementa un marco de pruebas completo para modelos de series de tiempo.
Analiza diferentes modelos y selecciona el que mejor se ajusta a los datos del dataset.

Modelos implementados:
- ARIMA/SARIMA
- Exponential Smoothing (Holt-Winters)
- Linear Regression con tendencia
- Moving Averages (Simple y Exponential)
- Prophet (si está disponible)

Métricas de evaluación:
- RMSE (Root Mean Square Error)
- MAE (Mean Absolute Error)
- MAPE (Mean Absolute Percentage Error)
- AIC (Akaike Information Criterion)
- BIC (Bayesian Information Criterion)

Autor: Sistema de evaluación automática de modelos de series de tiempo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any
import os
import sys

# Configuración de visualización
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
warnings.filterwarnings('ignore')

# Importaciones de modelos de series de tiempo
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox

from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

# Intentar importar Prophet si está disponible
try:
    from prophet import Prophet
    PROPHET_AVAILABLE = True
except ImportError:
    PROPHET_AVAILABLE = False
    print("Prophet no está disponible. Instalar con: pip install prophet")


class TimeSeriesModelTester:
    """
    Clase principal para testing de modelos de series de tiempo
    """
    
    def __init__(self, data_path: str = None):
        """
        Inicializa el tester de modelos de series de tiempo
        
        Args:
            data_path: Ruta al archivo de datos (opcional)
        """
        self.data_path = data_path
        self.ts_data = None
        self.train_data = None
        self.test_data = None
        self.results = {}
        self.best_model = None
        self.metrics_df = None
        
    def load_olist_data(self, data_dir: str = "proyecto_integrador/tp/data/") -> pd.DataFrame:
        """
        Carga y prepara los datos de Olist para análisis de series de tiempo
        
        Args:
            data_dir: Directorio con los datos de Olist
            
        Returns:
            DataFrame con series de tiempo agregada
        """
        print("Cargando datos de Olist...")
        
        # Cargar datos de órdenes
        orders_path = os.path.join(data_dir, "olist_orders_dataset.csv")
        payments_path = os.path.join(data_dir, "olist_order_payments_dataset.csv")
        
        if not os.path.exists(orders_path):
            raise FileNotFoundError(f"No se encontró el archivo: {orders_path}")
            
        orders = pd.read_csv(orders_path)
        
        # Convertir timestamps a datetime
        orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
        
        # Filtrar órdenes entregadas
        delivered_orders = orders[orders['order_status'] == 'delivered'].copy()
        
        # Crear serie de tiempo diaria de número de órdenes
        daily_orders = delivered_orders.groupby(
            delivered_orders['order_purchase_timestamp'].dt.date
        ).size().reset_index()
        
        daily_orders.columns = ['date', 'orders_count']
        daily_orders['date'] = pd.to_datetime(daily_orders['date'])
        daily_orders = daily_orders.set_index('date').sort_index()
        
        # Si hay datos de pagos, agregar valor total diario
        if os.path.exists(payments_path):
            payments = pd.read_csv(payments_path)
            
            # Unir órdenes con pagos
            order_payments = delivered_orders.merge(payments, on='order_id', how='left')
            
            # Crear serie de tiempo de ingresos diarios
            daily_revenue = order_payments.groupby(
                order_payments['order_purchase_timestamp'].dt.date
            )['payment_value'].sum().reset_index()
            
            daily_revenue.columns = ['date', 'revenue']
            daily_revenue['date'] = pd.to_datetime(daily_revenue['date'])
            daily_revenue = daily_revenue.set_index('date').sort_index()
            
            # Combinar órdenes y ingresos
            daily_orders = daily_orders.join(daily_revenue, how='outer').fillna(0)
        
        print(f"Datos cargados: {len(daily_orders)} observaciones diarias")
        print(f"Período: {daily_orders.index.min()} a {daily_orders.index.max()}")
        
        return daily_orders
    
    def prepare_time_series(self, df: pd.DataFrame, target_column: str = 'orders_count') -> pd.Series:
        """
        Prepara la serie de tiempo para análisis
        
        Args:
            df: DataFrame con datos
            target_column: Columna objetivo para análisis
            
        Returns:
            Serie de tiempo preparada
        """
        if target_column not in df.columns:
            raise ValueError(f"Columna '{target_column}' no encontrada en el DataFrame")
        
        ts = df[target_column].copy()
        
        # Rellenar valores faltantes con interpolación lineal
        ts = ts.interpolate(method='linear')
        
        # Eliminar outliers extremos (fuera de 3 desviaciones estándar)
        mean_val = ts.mean()
        std_val = ts.std()
        ts = ts.clip(lower=mean_val - 3*std_val, upper=mean_val + 3*std_val)
        
        self.ts_data = ts
        print(f"Serie de tiempo preparada: {len(ts)} observaciones")
        
        return ts
    
    def split_data(self, test_size: float = 0.2) -> Tuple[pd.Series, pd.Series]:
        """
        Divide los datos en entrenamiento y prueba
        
        Args:
            test_size: Proporción de datos para prueba
            
        Returns:
            Tupla con datos de entrenamiento y prueba
        """
        if self.ts_data is None:
            raise ValueError("Primero debe preparar la serie de tiempo")
        
        split_point = int(len(self.ts_data) * (1 - test_size))
        
        self.train_data = self.ts_data[:split_point]
        self.test_data = self.ts_data[split_point:]
        
        print(f"Datos divididos: {len(self.train_data)} entrenamiento, {len(self.test_data)} prueba")
        
        return self.train_data, self.test_data
    
    def calculate_metrics(self, y_true: pd.Series, y_pred: pd.Series, model_name: str = "") -> Dict[str, float]:
        """
        Calcula métricas de evaluación para el modelo
        
        Args:
            y_true: Valores reales
            y_pred: Valores predichos
            model_name: Nombre del modelo
            
        Returns:
            Diccionario con métricas
        """
        # Asegurar que las series tengan el mismo índice
        common_index = y_true.index.intersection(y_pred.index)
        y_true_aligned = y_true.loc[common_index]
        y_pred_aligned = y_pred.loc[common_index]
        
        # Remover cualquier NaN restante
        mask = ~(np.isnan(y_true_aligned) | np.isnan(y_pred_aligned) | np.isinf(y_true_aligned) | np.isinf(y_pred_aligned))
        y_true_clean = y_true_aligned[mask]
        y_pred_clean = y_pred_aligned[mask]
        
        if len(y_true_clean) == 0:
            return {
                'RMSE': np.inf,
                'MAE': np.inf,
                'MAPE': np.inf,
                'R²': -np.inf,
                'Model': model_name
            }
        
        rmse = np.sqrt(mean_squared_error(y_true_clean, y_pred_clean))
        mae = mean_absolute_error(y_true_clean, y_pred_clean)
        
        # MAPE - Manejar divisiones por cero
        y_true_nonzero = np.where(np.abs(y_true_clean) > 0.01, y_true_clean, 0.01)
        mape = np.mean(np.abs((y_true_clean - y_pred_clean) / y_true_nonzero)) * 100
        
        # R² score
        ss_res = np.sum((y_true_clean - y_pred_clean) ** 2)
        ss_tot = np.sum((y_true_clean - np.mean(y_true_clean)) ** 2)
        r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
        
        metrics = {
            'RMSE': rmse,
            'MAE': mae,
            'MAPE': mape,
            'R²': r2,
            'Model': model_name
        }
        
        return metrics
    
    def test_arima_model(self, max_p: int = 3, max_d: int = 2, max_q: int = 3) -> Dict[str, Any]:
        """
        Prueba modelos ARIMA con diferentes parámetros
        
        Args:
            max_p: Máximo orden AR
            max_d: Máximo orden de diferenciación
            max_q: Máximo orden MA
            
        Returns:
            Resultados del mejor modelo ARIMA
        """
        print("Probando modelos ARIMA...")
        
        best_aic = np.inf
        best_params = None
        best_model = None
        
        # Grid search para encontrar mejores parámetros
        for p in range(max_p + 1):
            for d in range(max_d + 1):
                for q in range(max_q + 1):
                    try:
                        model = ARIMA(self.train_data, order=(p, d, q))
                        fitted_model = model.fit()
                        
                        if fitted_model.aic < best_aic:
                            best_aic = fitted_model.aic
                            best_params = (p, d, q)
                            best_model = fitted_model
                            
                    except Exception as e:
                        continue
        
        if best_model is None:
            return {'error': 'No se pudo ajustar ningún modelo ARIMA'}
        
        # Generar predicciones
        forecast = best_model.forecast(steps=len(self.test_data))
        # Manejar NaN values en forecast
        if isinstance(forecast, np.ndarray):
            forecast = pd.Series(forecast, index=self.test_data.index)
        else:
            forecast = pd.Series(forecast, index=self.test_data.index)
        
        # Rellenar NaN con el último valor conocido
        forecast = forecast.ffill().fillna(self.train_data.iloc[-1])
        forecast_series = forecast
        
        # Calcular métricas
        metrics = self.calculate_metrics(self.test_data, forecast_series, f"ARIMA{best_params}")
        metrics['AIC'] = best_aic
        metrics['BIC'] = best_model.bic
        
        return {
            'model': best_model,
            'params': best_params,
            'forecast': forecast_series,
            'metrics': metrics
        }
    
    def test_sarima_model(self, seasonal_period: int = 7) -> Dict[str, Any]:
        """
        Prueba modelo SARIMA con estacionalidad
        
        Args:
            seasonal_period: Período estacional (ej: 7 para datos diarios con estacionalidad semanal)
            
        Returns:
            Resultados del modelo SARIMA
        """
        print("Probando modelo SARIMA...")
        
        try:
            # Parámetros simples para SARIMA
            model = SARIMAX(self.train_data, 
                           order=(1, 1, 1), 
                           seasonal_order=(1, 1, 1, seasonal_period))
            fitted_model = model.fit(disp=False)
            
            # Generar predicciones
            forecast = fitted_model.forecast(steps=len(self.test_data))
            # Manejar NaN values
            if isinstance(forecast, np.ndarray):
                forecast_series = pd.Series(forecast, index=self.test_data.index)
            else:
                forecast_series = pd.Series(forecast, index=self.test_data.index)
            
            # Rellenar NaN con el último valor conocido
            forecast_series = forecast_series.ffill().fillna(self.train_data.iloc[-1])
            
            # Calcular métricas
            metrics = self.calculate_metrics(self.test_data, forecast_series, "SARIMA(1,1,1)(1,1,1,7)")
            metrics['AIC'] = fitted_model.aic
            metrics['BIC'] = fitted_model.bic
            
            return {
                'model': fitted_model,
                'forecast': forecast_series,
                'metrics': metrics
            }
            
        except Exception as e:
            return {'error': f'Error en SARIMA: {str(e)}'}
    
    def test_exponential_smoothing(self) -> Dict[str, Any]:
        """
        Prueba modelos de suavizado exponencial (Holt-Winters)
        
        Returns:
            Resultados del modelo de suavizado exponencial
        """
        print("Probando Exponential Smoothing...")
        
        try:
            # Probar diferentes configuraciones
            best_aic = np.inf
            best_model = None
            best_config = None
            
            configs = [
                {'trend': None, 'seasonal': None},
                {'trend': 'add', 'seasonal': None},
                {'trend': 'add', 'seasonal': 'add', 'seasonal_periods': 7},
                {'trend': 'mul', 'seasonal': 'mul', 'seasonal_periods': 7}
            ]
            
            for config in configs:
                try:
                    model = ExponentialSmoothing(self.train_data, **config)
                    fitted_model = model.fit()
                    
                    if fitted_model.aic < best_aic:
                        best_aic = fitted_model.aic
                        best_model = fitted_model
                        best_config = config
                        
                except Exception:
                    continue
            
            if best_model is None:
                return {'error': 'No se pudo ajustar modelo de suavizado exponencial'}
            
            # Generar predicciones
            forecast = best_model.forecast(steps=len(self.test_data))
            # Manejar NaN values
            if isinstance(forecast, np.ndarray):
                forecast_series = pd.Series(forecast, index=self.test_data.index)
            else:
                forecast_series = pd.Series(forecast, index=self.test_data.index)
            
            # Rellenar NaN con el último valor conocido
            forecast_series = forecast_series.ffill().fillna(self.train_data.iloc[-1])
            
            # Calcular métricas
            metrics = self.calculate_metrics(self.test_data, forecast_series, f"Exp_Smoothing_{best_config}")
            metrics['AIC'] = best_aic
            
            return {
                'model': best_model,
                'config': best_config,
                'forecast': forecast_series,
                'metrics': metrics
            }
            
        except Exception as e:
            return {'error': f'Error en Exponential Smoothing: {str(e)}'}
    
    def test_linear_regression(self) -> Dict[str, Any]:
        """
        Prueba regresión lineal simple con tendencia temporal
        
        Returns:
            Resultados del modelo de regresión lineal
        """
        print("Probando Linear Regression...")
        
        try:
            # Crear features temporales
            train_index = np.arange(len(self.train_data)).reshape(-1, 1)
            test_index = np.arange(len(self.train_data), len(self.train_data) + len(self.test_data)).reshape(-1, 1)
            
            # Entrenar modelo
            model = LinearRegression()
            model.fit(train_index, self.train_data.values)
            
            # Generar predicciones
            predictions = model.predict(test_index)
            forecast_series = pd.Series(predictions, index=self.test_data.index)
            
            # Calcular métricas
            metrics = self.calculate_metrics(self.test_data, forecast_series, "Linear_Regression")
            
            return {
                'model': model,
                'forecast': forecast_series,
                'metrics': metrics
            }
            
        except Exception as e:
            return {'error': f'Error en Linear Regression: {str(e)}'}
    
    def test_moving_averages(self) -> Dict[str, Any]:
        """
        Prueba diferentes tipos de medias móviles
        
        Returns:
            Resultados de los modelos de media móvil
        """
        print("Probando Moving Averages...")
        
        results = {}
        
        # Simple Moving Average
        for window in [7, 14, 30]:
            try:
                # Usar los últimos 'window' valores del entrenamiento para predecir
                last_values = self.train_data.tail(window)
                prediction = last_values.mean()
                
                # Extender la predicción para todo el período de prueba
                forecast_series = pd.Series([prediction] * len(self.test_data), index=self.test_data.index)
                
                metrics = self.calculate_metrics(self.test_data, forecast_series, f"SMA_{window}")
                
                results[f'SMA_{window}'] = {
                    'window': window,
                    'forecast': forecast_series,
                    'metrics': metrics
                }
                
            except Exception as e:
                continue
        
        # Exponential Moving Average
        for alpha in [0.1, 0.3, 0.5]:
            try:
                ema_values = self.train_data.ewm(alpha=alpha).mean()
                prediction = ema_values.iloc[-1]
                
                forecast_series = pd.Series([prediction] * len(self.test_data), index=self.test_data.index)
                
                metrics = self.calculate_metrics(self.test_data, forecast_series, f"EMA_{alpha}")
                
                results[f'EMA_{alpha}'] = {
                    'alpha': alpha,
                    'forecast': forecast_series,
                    'metrics': metrics
                }
                
            except Exception as e:
                continue
        
        return results
    
    def test_prophet_model(self) -> Dict[str, Any]:
        """
        Prueba modelo Prophet de Facebook (si está disponible)
        
        Returns:
            Resultados del modelo Prophet
        """
        if not PROPHET_AVAILABLE:
            return {'error': 'Prophet no está disponible'}
        
        print("Probando Prophet...")
        
        try:
            # Preparar datos para Prophet
            train_df = pd.DataFrame({
                'ds': self.train_data.index,
                'y': self.train_data.values
            })
            
            # Entrenar modelo
            model = Prophet(daily_seasonality=True, weekly_seasonality=True, yearly_seasonality=True)
            model.fit(train_df)
            
            # Crear dataframe para predicciones
            future_df = pd.DataFrame({
                'ds': self.test_data.index
            })
            
            # Generar predicciones
            forecast = model.predict(future_df)
            forecast_series = pd.Series(forecast['yhat'].values, index=self.test_data.index)
            
            # Calcular métricas
            metrics = self.calculate_metrics(self.test_data, forecast_series, "Prophet")
            
            return {
                'model': model,
                'forecast': forecast_series,
                'forecast_df': forecast,
                'metrics': metrics
            }
            
        except Exception as e:
            return {'error': f'Error en Prophet: {str(e)}'}
    
    def run_all_tests(self, seasonal_period: int = 7) -> Dict[str, Any]:
        """
        Ejecuta todas las pruebas de modelos
        
        Args:
            seasonal_period: Período estacional para modelos que lo requieren
            
        Returns:
            Diccionario con todos los resultados
        """
        print("=" * 50)
        print("INICIANDO PRUEBAS DE MODELOS DE SERIES DE TIEMPO")
        print("=" * 50)
        
        results = {}
        
        # Probar cada modelo
        results['ARIMA'] = self.test_arima_model()
        results['SARIMA'] = self.test_sarima_model(seasonal_period)
        results['ExponentialSmoothing'] = self.test_exponential_smoothing()
        results['LinearRegression'] = self.test_linear_regression()
        results['MovingAverages'] = self.test_moving_averages()
        results['Prophet'] = self.test_prophet_model()
        
        self.results = results
        return results
    
    def create_comparison_table(self) -> pd.DataFrame:
        """
        Crea tabla comparativa de métricas de todos los modelos
        
        Returns:
            DataFrame con comparación de métricas
        """
        if not self.results:
            raise ValueError("Primero debe ejecutar las pruebas de modelos")
        
        metrics_list = []
        
        for model_type, result in self.results.items():
            if 'error' in result:
                continue
                
            if model_type == 'MovingAverages':
                # Manejar múltiples variantes de media móvil
                for variant, variant_result in result.items():
                    if 'metrics' in variant_result:
                        metrics_list.append(variant_result['metrics'])
            else:
                if 'metrics' in result:
                    metrics_list.append(result['metrics'])
        
        if not metrics_list:
            return pd.DataFrame()
        
        df = pd.DataFrame(metrics_list)
        df = df.sort_values('RMSE')  # Ordenar por RMSE (menor es mejor)
        
        self.metrics_df = df
        return df
    
    def find_best_model(self) -> Tuple[str, Dict[str, float]]:
        """
        Encuentra el mejor modelo basado en múltiples métricas
        
        Returns:
            Tupla con nombre del mejor modelo y sus métricas
        """
        if self.metrics_df is None:
            self.create_comparison_table()
        
        if self.metrics_df.empty:
            return None, None
        
        # Ranking basado en múltiples métricas (menor es mejor para RMSE, MAE, MAPE)
        # Mayor es mejor para R²
        
        # Normalizar métricas para ranking
        df_norm = self.metrics_df.copy()
        
        # Para RMSE, MAE, MAPE: menor es mejor (ranking inverso)
        for col in ['RMSE', 'MAE', 'MAPE']:
            if col in df_norm.columns:
                df_norm[f'{col}_rank'] = df_norm[col].rank()
        
        # Para R²: mayor es mejor
        if 'R²' in df_norm.columns:
            df_norm['R²_rank'] = df_norm['R²'].rank(ascending=False)
        
        # Calcular ranking promedio
        rank_cols = [col for col in df_norm.columns if col.endswith('_rank')]
        df_norm['avg_rank'] = df_norm[rank_cols].mean(axis=1)
        
        # Mejor modelo es el que tiene menor ranking promedio
        best_idx = df_norm['avg_rank'].idxmin()
        best_model_name = df_norm.loc[best_idx, 'Model']
        best_metrics = self.metrics_df.loc[best_idx].to_dict()
        
        self.best_model = best_model_name
        
        return best_model_name, best_metrics
    
    def plot_results(self, save_path: str = None) -> None:
        """
        Crea visualizaciones de los resultados
        
        Args:
            save_path: Ruta para guardar las gráficas (opcional)
        """
        if not self.results:
            raise ValueError("Primero debe ejecutar las pruebas de modelos")
        
        # Configurar el plot
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Resultados de Modelos de Series de Tiempo', fontsize=16, fontweight='bold')
        
        # 1. Serie de tiempo original con división train/test
        ax1 = axes[0, 0]
        ax1.plot(self.train_data.index, self.train_data.values, label='Entrenamiento', color='blue', alpha=0.7)
        ax1.plot(self.test_data.index, self.test_data.values, label='Prueba (Real)', color='red', alpha=0.7)
        ax1.axvline(x=self.test_data.index[0], color='black', linestyle='--', alpha=0.5, label='División Train/Test')
        ax1.set_title('Serie de Tiempo - Datos Originales')
        ax1.set_xlabel('Fecha')
        ax1.set_ylabel('Valores')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Comparación de predicciones
        ax2 = axes[0, 1]
        ax2.plot(self.test_data.index, self.test_data.values, label='Real', color='red', linewidth=2)
        
        colors = ['blue', 'green', 'orange', 'purple', 'brown']
        color_idx = 0
        
        for model_type, result in self.results.items():
            if 'error' in result or 'forecast' not in result:
                continue
                
            if model_type == 'MovingAverages':
                # Mostrar solo el mejor MA
                best_ma = None
                best_rmse = np.inf
                for variant, variant_result in result.items():
                    if 'metrics' in variant_result and variant_result['metrics']['RMSE'] < best_rmse:
                        best_rmse = variant_result['metrics']['RMSE']
                        best_ma = variant_result
                
                if best_ma:
                    ax2.plot(best_ma['forecast'].index, best_ma['forecast'].values, 
                            label=f"Best MA (RMSE: {best_rmse:.2f})", 
                            color=colors[color_idx % len(colors)], alpha=0.7)
                    color_idx += 1
            else:
                forecast = result['forecast']
                rmse = result['metrics']['RMSE']
                ax2.plot(forecast.index, forecast.values, 
                        label=f"{model_type} (RMSE: {rmse:.2f})", 
                        color=colors[color_idx % len(colors)], alpha=0.7)
                color_idx += 1
        
        ax2.set_title('Comparación de Predicciones')
        ax2.set_xlabel('Fecha')
        ax2.set_ylabel('Valores')
        ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax2.grid(True, alpha=0.3)
        
        # 3. Comparación de métricas
        ax3 = axes[1, 0]
        if self.metrics_df is not None and not self.metrics_df.empty:
            metrics_plot = self.metrics_df.set_index('Model')[['RMSE', 'MAE', 'MAPE']].head(8)
            metrics_plot.plot(kind='bar', ax=ax3, width=0.8)
            ax3.set_title('Comparación de Métricas de Error')
            ax3.set_xlabel('Modelos')
            ax3.set_ylabel('Valor de Métrica')
            ax3.legend()
            ax3.tick_params(axis='x', rotation=45)
            ax3.grid(True, alpha=0.3)
        
        # 4. R² Score comparison
        ax4 = axes[1, 1]
        if self.metrics_df is not None and not self.metrics_df.empty:
            r2_data = self.metrics_df.set_index('Model')['R²'].head(8)
            colors_r2 = plt.cm.viridis(np.linspace(0, 1, len(r2_data)))
            bars = ax4.bar(range(len(r2_data)), r2_data.values, color=colors_r2)
            ax4.set_title('R² Score por Modelo')
            ax4.set_xlabel('Modelos')
            ax4.set_ylabel('R² Score')
            ax4.set_xticks(range(len(r2_data)))
            ax4.set_xticklabels(r2_data.index, rotation=45)
            ax4.grid(True, alpha=0.3)
            
            # Añadir valores en las barras
            for bar, value in zip(bars, r2_data.values):
                ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
                        f'{value:.3f}', ha='center', va='bottom')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Gráficas guardadas en: {save_path}")
        
        plt.show()
    
    def generate_report(self, save_path: str = None) -> str:
        """
        Genera un reporte completo de los resultados
        
        Args:
            save_path: Ruta para guardar el reporte (opcional)
            
        Returns:
            String con el reporte completo
        """
        if not self.results:
            raise ValueError("Primero debe ejecutar las pruebas de modelos")
        
        report = []
        report.append("=" * 80)
        report.append("REPORTE DE EVALUACIÓN DE MODELOS DE SERIES DE TIEMPO")
        report.append("=" * 80)
        report.append(f"Fecha de análisis: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Información del dataset
        report.append("INFORMACIÓN DEL DATASET:")
        report.append("-" * 40)
        report.append(f"Total de observaciones: {len(self.ts_data)}")
        report.append(f"Período de entrenamiento: {self.train_data.index[0]} a {self.train_data.index[-1]} ({len(self.train_data)} observaciones)")
        report.append(f"Período de prueba: {self.test_data.index[0]} a {self.test_data.index[-1]} ({len(self.test_data)} observaciones)")
        report.append(f"Valor promedio: {self.ts_data.mean():.2f}")
        report.append(f"Desviación estándar: {self.ts_data.std():.2f}")
        report.append("")
        
        # Mejor modelo
        best_model, best_metrics = self.find_best_model()
        if best_model:
            report.append("MEJOR MODELO IDENTIFICADO:")
            report.append("-" * 40)
            report.append(f"Modelo: {best_model}")
            report.append("Métricas del mejor modelo:")
            for metric, value in best_metrics.items():
                if metric != 'Model':
                    if isinstance(value, (int, float)):
                        report.append(f"  {metric}: {value:.4f}")
                    else:
                        report.append(f"  {metric}: {value}")
            report.append("")
        
        # Tabla comparativa
        if self.metrics_df is not None and not self.metrics_df.empty:
            report.append("COMPARACIÓN COMPLETA DE MODELOS:")
            report.append("-" * 40)
            report.append(self.metrics_df.to_string(index=False, float_format='%.4f'))
            report.append("")
        
        # Resumen de cada modelo
        report.append("DETALLES POR MODELO:")
        report.append("-" * 40)
        
        for model_type, result in self.results.items():
            report.append(f"\n{model_type.upper()}:")
            if 'error' in result:
                report.append(f"  ❌ Error: {result['error']}")
            else:
                if model_type == 'MovingAverages':
                    for variant, variant_result in result.items():
                        if 'metrics' in variant_result:
                            metrics = variant_result['metrics']
                            report.append(f"  ✅ {variant}: RMSE={metrics['RMSE']:.4f}, MAE={metrics['MAE']:.4f}, R²={metrics['R²']:.4f}")
                else:
                    if 'metrics' in result:
                        metrics = result['metrics']
                        report.append(f"  ✅ RMSE: {metrics['RMSE']:.4f}")
                        report.append(f"     MAE: {metrics['MAE']:.4f}")
                        report.append(f"     MAPE: {metrics['MAPE']:.2f}%")
                        report.append(f"     R²: {metrics['R²']:.4f}")
                        if 'AIC' in metrics:
                            report.append(f"     AIC: {metrics['AIC']:.2f}")
                        if 'BIC' in metrics:
                            report.append(f"     BIC: {metrics['BIC']:.2f}")
        
        # Recomendaciones
        report.append("\n" + "=" * 40)
        report.append("RECOMENDACIONES:")
        report.append("=" * 40)
        
        if best_model:
            report.append(f"1. Se recomienda usar el modelo {best_model} para predicciones futuras.")
            
            # Recomendaciones específicas por tipo de modelo
            if 'ARIMA' in best_model:
                report.append("2. ARIMA es efectivo para series con patrones autorregresivos.")
                report.append("3. Monitorear residuales para validar supuestos del modelo.")
            elif 'SARIMA' in best_model:
                report.append("2. SARIMA captura bien la estacionalidad en los datos.")
                report.append("3. Considerar ajustar parámetros estacionales si cambian los patrones.")
            elif 'Prophet' in best_model:
                report.append("2. Prophet es robusto para datos con múltiples estacionalidades.")
                report.append("3. Puede manejar días festivos y eventos especiales.")
            elif 'Exp_Smoothing' in best_model:
                report.append("2. Suavizado exponencial es bueno para tendencias y estacionalidad.")
                report.append("3. Actualizar parámetros regularmente con nuevos datos.")
            
            # Recomendaciones generales
            report.append("4. Validar predicciones con datos reales periódicamente.")
            report.append("5. Considerar re-entrenar el modelo con nuevos datos cada mes.")
            report.append("6. Monitorear cambios en patrones del negocio que puedan afectar las predicciones.")
        
        report_text = "\n".join(report)
        
        if save_path:
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(report_text)
            print(f"Reporte guardado en: {save_path}")
        
        return report_text


def main():
    """
    Función principal para ejecutar el análisis completo
    """
    print("Iniciando análisis de modelos de series de tiempo...")
    
    # Crear instancia del tester
    tester = TimeSeriesModelTester()
    
    try:
        # Cargar datos de Olist
        df = tester.load_olist_data()
        
        # Preparar serie de tiempo (usar número de órdenes)
        ts = tester.prepare_time_series(df, 'orders_count')
        
        # Dividir datos
        train, test = tester.split_data(test_size=0.2)
        
        # Ejecutar todas las pruebas
        results = tester.run_all_tests()
        
        # Crear tabla comparativa
        comparison_df = tester.create_comparison_table()
        print("\nTABLA COMPARATIVA DE MODELOS:")
        print("=" * 50)
        print(comparison_df.to_string(index=False, float_format='%.4f'))
        
        # Encontrar mejor modelo
        best_model, best_metrics = tester.find_best_model()
        if best_model:
            print(f"\n🏆 MEJOR MODELO: {best_model}")
            print("Métricas del mejor modelo:")
            for metric, value in best_metrics.items():
                if metric != 'Model' and isinstance(value, (int, float)):
                    print(f"  {metric}: {value:.4f}")
        
        # Generar visualizaciones
        tester.plot_results("time_series_analysis_results.png")
        
        # Generar reporte completo
        report = tester.generate_report("time_series_analysis_report.txt")
        
        print("\n" + "=" * 50)
        print("ANÁLISIS COMPLETADO EXITOSAMENTE")
        print("=" * 50)
        print("Archivos generados:")
        print("- time_series_analysis_results.png (visualizaciones)")
        print("- time_series_analysis_report.txt (reporte completo)")
        
    except Exception as e:
        print(f"Error durante el análisis: {str(e)}")
        print("Asegúrese de que los datos de Olist estén disponibles en 'proyecto_integrador/tp/data/'")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())