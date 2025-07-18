#!/usr/bin/env python3
"""
Calculadora de Tiempo de Lectura para Bibliografía de Examen
============================================================

Este script calcula el tiempo necesario para leer toda la bibliografía
especificada para un examen, basándose en velocidades de lectura promedio
y estimaciones de palabras por página.

Autor: Calculadora automática para TSCDIA
Fecha: 2024
"""

import math
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Document:
    """Representa un documento con su información de lectura"""
    name: str
    pages: int
    words_per_page: int = 250  # Promedio para documentos académicos
    difficulty_multiplier: float = 1.0  # Factor de dificultad (1.0 = normal)
    
    def get_total_words(self) -> int:
        """Calcula el total de palabras en el documento"""
        return self.pages * self.words_per_page


class ReadingTimeCalculator:
    """Calculadora de tiempo de lectura para documentos académicos"""
    
    def __init__(self, words_per_minute: int = 200):
        """
        Inicializa la calculadora
        
        Args:
            words_per_minute: Velocidad de lectura en palabras por minuto
                            - 200-250: Promedio para adultos
                            - 150-200: Lectura académica/técnica
                            - 100-150: Lectura muy técnica/difícil
        """
        self.words_per_minute = words_per_minute
        self.documents = []
    
    def add_document(self, document: Document):
        """Agrega un documento a la lista de lectura"""
        self.documents.append(document)
    
    def calculate_reading_time(self, document: Document) -> Dict[str, float]:
        """
        Calcula el tiempo de lectura para un documento específico
        
        Returns:
            Dict con tiempo en minutos, horas y información adicional
        """
        total_words = document.get_total_words()
        adjusted_words = total_words * document.difficulty_multiplier
        minutes = adjusted_words / self.words_per_minute
        hours = minutes / 60
        
        return {
            'minutes': minutes,
            'hours': hours,
            'words': total_words,
            'adjusted_words': adjusted_words,
            'pages': document.pages
        }
    
    def calculate_total_time(self) -> Dict[str, any]:
        """Calcula el tiempo total de lectura para todos los documentos"""
        total_minutes = 0
        total_words = 0
        total_pages = 0
        document_details = []
        
        for doc in self.documents:
            time_info = self.calculate_reading_time(doc)
            total_minutes += time_info['minutes']
            total_words += time_info['words']
            total_pages += time_info['pages']
            
            document_details.append({
                'name': doc.name,
                'pages': doc.pages,
                'time_hours': time_info['hours'],
                'time_minutes': time_info['minutes'],
                'words': time_info['words']
            })
        
        total_hours = total_minutes / 60
        total_days = total_hours / 8  # 8 horas de estudio por día
        
        return {
            'total_minutes': total_minutes,
            'total_hours': total_hours,
            'total_days': total_days,
            'total_words': total_words,
            'total_pages': total_pages,
            'document_details': document_details,
            'reading_speed': self.words_per_minute
        }
    
    def print_detailed_report(self):
        """Imprime un reporte detallado del tiempo de lectura"""
        if not self.documents:
            print("No hay documentos agregados para calcular.")
            return
        
        results = self.calculate_total_time()
        
        print("=" * 80)
        print("CALCULADORA DE TIEMPO DE LECTURA - BIBLIOGRAFÍA DE EXAMEN")
        print("=" * 80)
        print(f"Velocidad de lectura configurada: {self.words_per_minute} palabras/minuto")
        print()
        
        print("DESGLOSE POR DOCUMENTO:")
        print("-" * 80)
        
        for doc_info in results['document_details']:
            print(f"📄 {doc_info['name']}")
            print(f"   Páginas: {doc_info['pages']}")
            print(f"   Palabras estimadas: {doc_info['words']:,}")
            print(f"   Tiempo de lectura: {doc_info['time_hours']:.1f} horas ({doc_info['time_minutes']:.0f} minutos)")
            print()
        
        print("RESUMEN TOTAL:")
        print("-" * 80)
        print(f"📚 Total de documentos: {len(self.documents)}")
        print(f"📄 Total de páginas: {results['total_pages']:,}")
        print(f"📝 Total de palabras estimadas: {results['total_words']:,}")
        print(f"⏱️  Tiempo total de lectura: {results['total_hours']:.1f} horas")
        print(f"📅 Días de estudio (8h/día): {results['total_days']:.1f} días")
        print(f"📅 Días de estudio (4h/día): {results['total_days'] * 2:.1f} días")
        print(f"📅 Días de estudio (2h/día): {results['total_days'] * 4:.1f} días")
        print()
        
        print("RECOMENDACIONES:")
        print("-" * 80)
        print("• Para lectura académica intensiva, considera reducir la velocidad a 150-180 ppm")
        print("• Agrega tiempo extra para tomar notas y repasar conceptos importantes")
        print("• Planifica descansos regulares cada 45-60 minutos de lectura")
        print("• Considera hacer resúmenes de cada documento para facilitar el repaso")
        print("=" * 80)


def create_exam_bibliography_calculator():
    """Crea la calculadora con la bibliografía específica del examen"""
    
    # Configurar velocidad de lectura académica
    calculator = ReadingTimeCalculator(words_per_minute=180)  # Velocidad para textos académicos
    
    # Agregar documentos según la bibliografía especificada
    documents = [
        # Marco general - PDF completo (estimando ~150 páginas)
        Document(
            name="Marco General - DC Nivel Primario",
            pages=150,
            words_per_page=300,  # Documentos oficiales suelen ser más densos
            difficulty_multiplier=1.2  # Texto técnico-administrativo
        ),
        
        # Diseño curricular primer ciclo (páginas 258-279)
        Document(
            name="Diseño Curricular Primer Ciclo (pág. 258-279)",
            pages=22,  # 279 - 258 + 1
            words_per_page=350,
            difficulty_multiplier=1.3  # Contenido curricular específico
        ),
        
        # Diseño curricular segundo ciclo (páginas 438-470)
        Document(
            name="Diseño Curricular Segundo Ciclo (pág. 438-470)",
            pages=33,  # 470 - 438 + 1
            words_per_page=350,
            difficulty_multiplier=1.3
        ),
        
        # Orientación para la enseñanza primer ciclo (páginas 84-88)
        Document(
            name="Orientación Enseñanza y Evaluación 1° Ciclo (pág. 84-88)",
            pages=5,  # 88 - 84 + 1
            words_per_page=400,
            difficulty_multiplier=1.1
        ),
        
        # Orientación para la enseñanza segundo ciclo (páginas 104-108)
        Document(
            name="Orientación Enseñanza y Evaluación 2° Ciclo (pág. 104-108)",
            pages=5,  # 108 - 104 + 1
            words_per_page=400,
            difficulty_multiplier=1.1
        ),
        
        # Régimen Académico (estimando documento completo)
        Document(
            name="Régimen Académico - Versión Final",
            pages=50,  # Estimación para documento completo
            words_per_page=300,
            difficulty_multiplier=1.4  # Texto legal/reglamentario
        ),
        
        # Diseño curricular NES (estimando secciones relevantes)
        Document(
            name="Diseño Curricular NES (secciones relevantes)",
            pages=80,  # Estimación de secciones relevantes
            words_per_page=320,
            difficulty_multiplier=1.2
        ),
        
        # Educación Tecnológica Secundaria (estimando documentos)
        Document(
            name="Documentos Educación Tecnológica Secundaria",
            pages=60,  # Estimación
            words_per_page=280,
            difficulty_multiplier=1.1
        ),
        
        # Tecnología de la Información NES (estimando documentos)
        Document(
            name="Documentos Tecnologías de la Información NES",
            pages=40,  # Estimación
            words_per_page=300,
            difficulty_multiplier=1.1
        ),
        
        # Estatuto docente (artículos específicos)
        Document(
            name="Estatuto Docente (Capítulo III, Art. 6 y 7)",
            pages=8,  # Estimación para artículos específicos
            words_per_page=250,
            difficulty_multiplier=1.5  # Texto legal
        ),
        
        # Reglamento escolar (artículos específicos)
        Document(
            name="Reglamento Escolar (artículos específicos)",
            pages=25,  # Estimación para todos los artículos mencionados
            words_per_page=280,
            difficulty_multiplier=1.4  # Texto reglamentario
        )
    ]
    
    # Agregar todos los documentos a la calculadora
    for doc in documents:
        calculator.add_document(doc)
    
    return calculator


def main():
    """Función principal que ejecuta la calculadora"""
    print("Iniciando cálculo de tiempo de lectura para bibliografía de examen...")
    print()
    
    # Crear calculadora con la bibliografía específica
    calculator = create_exam_bibliography_calculator()
    
    # Mostrar reporte detallado
    calculator.print_detailed_report()
    
    # Mostrar opciones de velocidad alternativas
    print("\n" + "=" * 80)
    print("COMPARACIÓN CON DIFERENTES VELOCIDADES DE LECTURA:")
    print("=" * 80)
    
    speeds = [150, 200, 250]
    for speed in speeds:
        calc_temp = ReadingTimeCalculator(words_per_minute=speed)
        for doc in calculator.documents:
            calc_temp.add_document(doc)
        
        results = calc_temp.calculate_total_time()
        print(f"A {speed} ppm: {results['total_hours']:.1f} horas ({results['total_days']:.1f} días a 8h/día)")
    
    print("\n🎯 ¡Buena suerte con tu examen!")


if __name__ == "__main__":
    main()