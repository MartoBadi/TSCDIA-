def recomendar_atuendo(analisis):
    genero = analisis.get("genero", "desconocido")
    color_ojos = analisis.get("color_ojos", "desconocido")
    forma_cara = analisis.get("forma_cara", "desconocido")
    peinado = analisis.get("peinado", "desconocido")

    if genero == "desconocido":
        return "No se pudo determinar el género para sugerir atuendo."

    if genero == "Hombre":
        sugerencia = f"Camiseta azul (resalta ojos {color_ojos}), pantalón beige, zapatos marrones. Forma de cara {forma_cara}, peinado {peinado}."
    else:
        sugerencia = f"Blusa blanca (resalta ojos {color_ojos}), pantalón negro, zapatos nude. Forma de cara {forma_cara}, peinado {peinado}."

    return sugerencia
