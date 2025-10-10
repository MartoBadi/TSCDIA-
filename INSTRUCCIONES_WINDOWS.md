# App Estudio - Reproductor de Exposición

Esta aplicación Electron permite estudiar una exposición sobre Ciencia de Datos con sincronización de audio y texto.

## Para ejecutar en Windows:

### Opción 1: Ejecutar directamente (recomendado)
1. Descarga e instala Node.js desde https://nodejs.org/ (versión LTS)
2. Descarga el archivo `app_estudio_para_windows.zip`
3. Extrae el contenido del ZIP en una carpeta
4. Abre una terminal de comandos en esa carpeta
5. Ejecuta: `npm install`
6. Luego ejecuta: `npm start`

### Opción 2: Crear ejecutable portable
Si quieres crear un ejecutable independiente:
1. Sigue los pasos de la Opción 1
2. Instala electron-packager globalmente: `npm install -g electron-packager`
3. Ejecuta: `electron-packager . app_estudio --platform=win32 --arch=x64 --out=dist`
4. El ejecutable estará en la carpeta `dist/`

## Características:
- Reproductor de audio sincronizado con texto
- Navegación por frases
- Grabación de audio
- Interfaz intuitiva para estudio

## Archivos incluidos:
- `proyecto_integrador/main.js` - Proceso principal de Electron
- `proyecto_integrador/script.js` - Lógica del renderer
- `proyecto_integrador/index.html` - Interfaz de usuario
- `proyecto_integrador/styles.css` - Estilos
- `proyecto_integrador/preload.js` - API segura para IPC

## Solución al problema de espacio:
El issue original era que los builds de Electron para Windows requieren mucho espacio en disco. La solución fue crear un ZIP con solo los archivos fuente esenciales, que luego se pueden ejecutar con Node.js instalado.