#!/usr/bin/env python3
"""
Calculadora Básica de Tiempo de Lectura
========================================

Versión simple sin dependencias externas para calcular el tiempo de lectura
de la bibliografía del examen.

Uso: python3 calculadora_simple.py
"""

def calcular_tiempo_lectura():
    """Función principal que calcula el tiempo de lectura"""
    
    print("=" * 70)
    print("CALCULADORA SIMPLE DE TIEMPO DE LECTURA")
    print("=" * 70)
    print()
    
    # Configuración básica
    velocidad_lectura = 180  # palabras por minuto
    
    # Bibliografía con páginas y estimaciones
    bibliografia = [
        {"nombre": "Marco General - DC Nivel Primario", "paginas": 150, "ppm": 300, "dificultad": 1.2},
        {"nombre": "Diseño Curricular 1° Ciclo (pág. 258-279)", "paginas": 22, "ppm": 350, "dificultad": 1.3},
        {"nombre": "Diseño Curricular 2° Ciclo (pág. 438-470)", "paginas": 33, "ppm": 350, "dificultad": 1.3},
        {"nombre": "Orientación Enseñanza 1° Ciclo (pág. 84-88)", "paginas": 5, "ppm": 400, "dificultad": 1.1},
        {"nombre": "Orientación Enseñanza 2° Ciclo (pág. 104-108)", "paginas": 5, "ppm": 400, "dificultad": 1.1},
        {"nombre": "Régimen Académico - Versión Final", "paginas": 50, "ppm": 300, "dificultad": 1.4},
        {"nombre": "Diseño Curricular NES (secciones)", "paginas": 80, "ppm": 320, "dificultad": 1.2},
        {"nombre": "Educación Tecnológica Secundaria", "paginas": 60, "ppm": 280, "dificultad": 1.1},
        {"nombre": "Tecnologías de la Información NES", "paginas": 40, "ppm": 300, "dificultad": 1.1},
        {"nombre": "Estatuto Docente (Cap. III, Art. 6-7)", "paginas": 8, "ppm": 250, "dificultad": 1.5},
        {"nombre": "Reglamento Escolar (arts. específicos)", "paginas": 25, "ppm": 280, "dificultad": 1.4}
    ]
    
    print(f"Velocidad de lectura configurada: {velocidad_lectura} palabras/minuto")
    print()
    print("DESGLOSE POR DOCUMENTO:")
    print("-" * 70)
    
    total_minutos = 0
    total_paginas = 0
    total_palabras = 0
    
    for doc in bibliografia:
        # Calcular palabras y tiempo
        palabras = doc["paginas"] * doc["ppm"]
        palabras_ajustadas = palabras * doc["dificultad"]
        minutos = palabras_ajustadas / velocidad_lectura
        horas = minutos / 60
        
        # Acumular totales
        total_minutos += minutos
        total_paginas += doc["paginas"]
        total_palabras += palabras
        
        # Mostrar resultado
        print(f"📄 {doc['nombre']}")
        print(f"   Páginas: {doc['paginas']}")
        print(f"   Palabras: {palabras:,}")
        print(f"   Tiempo: {horas:.1f} horas ({minutos:.0f} min)")
        print()
    
    total_horas = total_minutos / 60
    dias_8h = total_horas / 8
    dias_4h = total_horas / 4
    dias_2h = total_horas / 2
    
    print("RESUMEN TOTAL:")
    print("-" * 70)
    print(f"📚 Total documentos: {len(bibliografia)}")
    print(f"📄 Total páginas: {total_paginas:,}")
    print(f"📝 Total palabras: {total_palabras:,}")
    print(f"⏱️  Tiempo total: {total_horas:.1f} horas ({total_minutos:.0f} minutos)")
    print(f"📅 Días (8h/día): {dias_8h:.1f} días")
    print(f"📅 Días (4h/día): {dias_4h:.1f} días")
    print(f"📅 Días (2h/día): {dias_2h:.1f} días")
    print()
    
    print("COMPARACIÓN CON OTRAS VELOCIDADES:")
    print("-" * 70)
    velocidades = [120, 150, 180, 200, 250]
    
    for vel in velocidades:
        tiempo_total = sum(doc["paginas"] * doc["ppm"] * doc["dificultad"] / vel for doc in bibliografia)
        horas_total = tiempo_total / 60
        print(f"A {vel:3d} ppm: {horas_total:.1f} horas ({horas_total/8:.1f} días a 8h/día)")
    
    print()
    print("PLAN DE ESTUDIO RECOMENDADO:")
    print("-" * 70)
    print("📅 Día 1-2: Marco General + Diseño Curricular NES")
    print("📅 Día 3:   Diseño Curricular 1° y 2° Ciclo")
    print("📅 Día 4:   Régimen Académico + Documentos Tecnológicos")
    print("📅 Día 5:   Estatuto + Reglamento + Orientaciones")
    print("📅 Día 6-7: Repaso y síntesis")
    print()
    print("CONSEJOS FINALES:")
    print("-" * 70)
    print("• Usa la técnica Pomodoro: 45 min lectura + 15 min descanso")
    print("• Toma notas y haz resúmenes de cada documento")
    print("• Para textos muy técnicos, reduce tu velocidad de lectura")
    print("• Planifica tiempo extra para repasar conceptos difíciles")
    print("• Considera hacer mapas conceptuales para conectar ideas")
    print()
    print("🎯 ¡Buena suerte con tu examen!")
    print("=" * 70)

if __name__ == "__main__":
    calcular_tiempo_lectura()