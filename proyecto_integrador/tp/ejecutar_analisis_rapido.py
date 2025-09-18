#!/usr/bin/env python3
"""
Script de ejecución rápida para el análisis de modelos de series de tiempo
==========================================================================

Este script permite ejecutar rápidamente el análisis completo sin necesidad
de usar Jupyter Notebook.

Uso:
    python ejecutar_analisis_rapido.py

El script:
1. Carga los datos automáticamente
2. Ejecuta todos los modelos
3. Genera el reporte y visualizaciones
4. Muestra los resultados principales en consola
"""

import sys
import os
from time_series_model_testing import TimeSeriesModelTester

def main():
    """
    Ejecuta el análisis completo de modelos de series de tiempo
    """
    print("🚀 ANÁLISIS RÁPIDO DE MODELOS DE SERIES DE TIEMPO")
    print("=" * 60)
    
    # Verificar si existen los datos
    data_dir = "data/"
    orders_file = os.path.join(data_dir, "olist_orders_dataset.csv")
    
    if not os.path.exists(orders_file):
        print(f"❌ Error: No se encontró el archivo {orders_file}")
        print("📋 Asegúrese de que los datos de Olist estén en la ruta correcta:")
        print("   - data/olist_orders_dataset.csv")
        print("   - data/olist_order_payments_dataset.csv")
        return 1
    
    try:
        # Crear instancia del tester
        print("🔧 Inicializando framework de testing...")
        tester = TimeSeriesModelTester()
        
        # Cargar y preparar datos
        print("📂 Cargando datos...")
        df = tester.load_olist_data()
        
        print("⚙️ Preparando serie de tiempo...")
        ts = tester.prepare_time_series(df, 'orders_count')
        
        print("✂️ Dividiendo datos...")
        train, test = tester.split_data(test_size=0.2)
        
        # Ejecutar análisis completo
        print("🧪 Ejecutando pruebas de modelos...")
        print("   (Esto puede tomar varios minutos...)")
        results = tester.run_all_tests()
        
        # Generar resultados
        print("📊 Generando comparación...")
        comparison_df = tester.create_comparison_table()
        
        print("🏆 Identificando mejor modelo...")
        best_model, best_metrics = tester.find_best_model()
        
        # Mostrar resultados principales
        print("\n" + "=" * 60)
        print("📈 RESULTADOS PRINCIPALES")
        print("=" * 60)
        
        if not comparison_df.empty:
            print("\n🏆 TOP 5 MEJORES MODELOS:")
            print("-" * 40)
            top_5 = comparison_df.head(5)
            for i, (_, row) in enumerate(top_5.iterrows(), 1):
                print(f"{i}. {row['Model']}")
                print(f"   RMSE: {row['RMSE']:.4f} | MAE: {row['MAE']:.4f} | MAPE: {row['MAPE']:.2f}% | R²: {row['R²']:.4f}")
        
        if best_model:
            print(f"\n🥇 MEJOR MODELO: {best_model}")
            print("-" * 40)
            for metric, value in best_metrics.items():
                if metric != 'Model' and isinstance(value, (int, float)):
                    if metric == 'MAPE':
                        print(f"   {metric}: {value:.2f}%")
                    else:
                        print(f"   {metric}: {value:.4f}")
        
        # Generar archivos de salida
        print("\n📁 Generando archivos de salida...")
        tester.plot_results("time_series_analysis_results.png")
        report = tester.generate_report("time_series_analysis_report.txt")
        
        # Recomendaciones rápidas
        print("\n" + "=" * 60)
        print("💡 RECOMENDACIONES RÁPIDAS")
        print("=" * 60)
        
        if best_model and best_metrics:
            if best_metrics['R²'] > 0.7:
                print("✅ Excelente ajuste del modelo - Listo para producción")
            elif best_metrics['R²'] > 0.5:
                print("✅ Buen ajuste del modelo - Considerar mejoras adicionales")
            elif best_metrics['R²'] > 0.3:
                print("⚠️ Ajuste moderado - Necesita optimización")
            else:
                print("❌ Ajuste pobre - Considerar variables adicionales o modelos complejos")
            
            if best_metrics['MAPE'] < 10:
                print("✅ Error muy bajo - Predicciones muy confiables")
            elif best_metrics['MAPE'] < 20:
                print("✅ Error bajo - Predicciones confiables")
            elif best_metrics['MAPE'] < 50:
                print("⚠️ Error moderado - Usar con precaución")
            else:
                print("❌ Error alto - Modelo no recomendado para decisiones críticas")
        
        print("\n📋 PRÓXIMOS PASOS:")
        print("1. Revisar el reporte completo: time_series_analysis_report.txt")
        print("2. Analizar las visualizaciones: time_series_analysis_results.png")
        print("3. Considerar re-entrenamiento con más datos")
        print("4. Implementar monitoreo de desempeño")
        
        print("\n" + "=" * 60)
        print("✅ ANÁLISIS COMPLETADO EXITOSAMENTE")
        print("=" * 60)
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error durante el análisis: {str(e)}")
        print("\n🔧 Posibles soluciones:")
        print("1. Verificar que los archivos de datos existan")
        print("2. Instalar dependencias: pip install pandas numpy matplotlib statsmodels scikit-learn")
        print("3. Revisar permisos de escritura en el directorio")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)