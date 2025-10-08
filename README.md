# TSCDIA-
Repositorio con mis trabajos de la Tecnicatura Superior en Ciencia de Datos e IA del IFTS 18.

## 📱 Aplicación de Estudio (Electron App)

Esta es una aplicación de escritorio para estudiar, construida con Electron.

### 🚀 Instalación y Ejecución en Desarrollo

1. **Instalar dependencias:**
   ```bash
   npm install
   ```

2. **Ejecutar en modo desarrollo:**
   ```bash
   npm start
   ```

### 📦 Crear Ejecutables

**Nota Importante:** Es recomendable compilar en el mismo sistema operativo donde se va a ejecutar la aplicación. Por ejemplo:
- Si usas Windows, compila con `npm run pack:win` en Windows
- Si usas Linux, compila con `npm run pack:linux` en Linux
- Si usas macOS, compila con `npm run pack:mac` en macOS

#### Para Windows
```bash
npm run pack:win
```
El ejecutable se generará en: `dist/app_estudio-win32-x64/app_estudio.exe`

#### Para Linux
```bash
npm run pack:linux
```
El ejecutable se generará en: `dist/app_estudio-linux-x64/app_estudio`

#### Para macOS
```bash
npm run pack:mac
```
La aplicación se generará en: `dist/app_estudio-darwin-x64/app_estudio.app`

#### Para todas las plataformas
```bash
npm run pack:all
```

**Advertencia sobre compilación cruzada:** Si intentas compilar para Windows desde Linux/macOS o viceversa, podrías encontrar errores relacionados con Wine u otras herramientas. En ese caso, compila desde el sistema operativo objetivo.

### 💻 Cómo Usar el Ejecutable

#### En Windows:
1. Ve a la carpeta `dist/app_estudio-win32-x64/`
2. Ejecuta `app_estudio.exe`

#### En Linux:
1. Ve a la carpeta `dist/app_estudio-linux-x64/`
2. Dale permisos de ejecución (si es necesario):
   ```bash
   chmod +x app_estudio
   ```
3. Ejecuta:
   ```bash
   ./app_estudio
   ```

#### En macOS:
1. Ve a la carpeta `dist/app_estudio-darwin-x64/`
2. Abre `app_estudio.app`

### ⚠️ Nota Importante

**No intentes cambiar la extensión de los ejecutables manualmente.** Cada sistema operativo tiene su propio formato:
- Windows: `.exe`
- Linux: sin extensión (pero es un binario ELF)
- macOS: `.app` (en realidad es una carpeta)

Si construiste la aplicación para la plataforma equivocada, simplemente ejecuta el comando de empaquetado correcto para tu sistema operativo.

### 🔧 Solución de Problemas

**Problema:** El ejecutable de Linux no funciona en Windows
- **Solución:** Los ejecutables de Linux solo funcionan en Linux. Usa `npm run pack:win` para crear uno para Windows.

**Problema:** "El ejecutable no tiene extensión"
- **Solución:** Los ejecutables de Linux no tienen extensión `.exe`. No intentes agregar una. Si necesitas Windows, reconstruye con `npm run pack:win`.

**Problema:** El ejecutable no inicia
- **Solución:** 
  - Verifica que estés usando el ejecutable correcto para tu sistema operativo
  - En Linux, asegúrate de que el archivo tenga permisos de ejecución: `chmod +x app_estudio`
  - Si construiste desde Windows para Linux (o viceversa), es normal que no funcione en tu sistema

### 📁 Estructura del Proyecto

```
TSCDIA-/
├── index.js                 # Punto de entrada de Electron
├── package.json             # Configuración del proyecto
├── proyecto_integrador/     # Código de la aplicación
│   ├── index.html
│   ├── script.js
│   └── main.js
└── dist/                    # Carpeta de distribución (ejecutables)
    ├── app_estudio-win32-x64/
    ├── app_estudio-linux-x64/
    └── app_estudio-darwin-x64/
```

