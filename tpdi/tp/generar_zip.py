import shutil

# Ruta de la carpeta que quieres comprimir
carpeta_a_comprimir = "C:\\TSCDIA-\\tpdi\\tp"

# Ruta y nombre del archivo ZIP que se generará
archivo_zip = "C:\\TSCDIA-\\tpdi\\tp\\tp.zip"

# Comprimir la carpeta
shutil.make_archive(archivo_zip.replace('.zip', ''), 'zip', carpeta_a_comprimir)

print(f"Carpeta comprimida como {archivo_zip}")