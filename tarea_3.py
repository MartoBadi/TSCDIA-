"""
1) Desarrollar la progrmación con un menu que me permita:

Influencers (personas) con más seguidores: Nombre, cantidad de seguidores y país de origen.
Los 3 países con más influencers: Nombre y porcentaje de seguidores (respecto al data set).
Cuenta de Marca con más seguidores: Nombre, cantidad de seguidores.
2) Detalles a tener en cuenta:

La tarea es grupal.
El código deberá ser explicado en clase y deberá ejecutarlo para ver su funcionamiento.
Para mostrar los datos utilice los gráficos estadísticos que más convenga.


"""

import pandas as pd
import matplotlib.pyplot as plt

# Función para cargar datos desde un archivo .xlsx
def cargar_datos(archivo):
    return pd.read_excel(archivo, engine='openpyxl')

# Función para mostrar el menú
def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Influencers con más seguidores")
    print("2. Los 3 países con más influencers")
    print("3. Cuenta de Marca con más seguidores")
    print("4. Salir")

# Función para encontrar influencers con más seguidores
def influencers_mas_seguidores(df):
    top_influencers = df.nlargest(10, 'Seguidores(millones)')
    print(top_influencers[['Propietario', 'Seguidores(millones)', 'País']])
    top_influencers.plot(kind='bar', x='Propietario', y='Seguidores(millones)')
    plt.show()

# Función para encontrar los 3 países con más influencers
def paises_mas_influencers(df):
    paises = df['País'].value_counts().nlargest(3)
    total_seguidores = df.groupby('País')['Seguidores(millones)'].sum()
    porcentaje_seguidores = (total_seguidores / total_seguidores.sum()) * 100
    top_paises = porcentaje_seguidores.nlargest(3)
    print(top_paises)
    top_paises.plot(kind='pie', autopct='%1.1f%%')
    plt.show()

# Función para encontrar la cuenta de marca con más seguidores
def cuenta_marca_mas_seguidores(df):
    marcas = df[df['Tipo'] == 'Marca']
    top_marca = marcas.nlargest(1, 'Seguidores(millones)')
    print(top_marca[['Propietario', 'Seguidores(millones)']])
    top_marca.plot(kind='bar', x='Propietario', y='Seguidores(millones)')
    plt.show()

# Función principal
def main():
    archivo = 'Lista_de_Influencer.xlsx'  # Reemplaza con la ruta de tu archivo .xlsx
    df = cargar_datos(archivo)
    
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        
        if opcion == '1':
            influencers_mas_seguidores(df)
        elif opcion == '2':
            paises_mas_influencers(df)
        elif opcion == '3':
            cuenta_marca_mas_seguidores(df)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()