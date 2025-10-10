# Instrucciones para ejecutar la App Estudio en Windows

## Problema actual
Estás obteniendo el error "Cannot find module 'electron'" porque electron-packager no puede encontrar el módulo de electron.

## Solución paso a paso

### 1. Verificar instalación de Node.js
Abre PowerShell como administrador y ejecuta:
```powershell
node --version
npm --version
```

Si no está instalado, instala Node.js LTS:
```powershell
winget install OpenJS.NodeJS.LTS
```

### 2. Instalar electron-packager globalmente
```powershell
npm install -g electron-packager
```

### 3. Instalar dependencias del proyecto
En el directorio del proyecto (donde está package.json):
```powershell
npm install
```

### 4. Crear el ejecutable de Windows
```powershell
electron-packager . app_estudio --platform=win32 --arch=x64 --out=dist
```

### 5. Ejecutar la aplicación
Para probar primero:
```powershell
npm start
```

Para usar el ejecutable creado:
```powershell
# El ejecutable estará en:
# dist/app_estudio-win32-x64/app_estudio.exe
```

## Comandos alternativos si hay problemas

Si `winget` no funciona, descarga Node.js manualmente desde:
https://nodejs.org/

## Verificación final
Después de seguir estos pasos, deberías poder ejecutar:
```powershell
electron-packager --version
```
Y debería mostrar la versión sin errores.