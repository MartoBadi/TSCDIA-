const { contextBridge, ipcRenderer } = require('electron');

// Exponer APIs seguras al proceso de renderizado
contextBridge.exposeInMainWorld('electronAPI', {
    getTextosExposicion: () => ipcRenderer.invoke('get-textos-exposicion'),
    getDuracionesAudios: () => ipcRenderer.invoke('get-duraciones-audios'),
    getTiemposInicio: () => ipcRenderer.invoke('get-tiempos-inicio'),
    getRepeticionesPorFrase: () => ipcRenderer.invoke('get-repeticiones-por-frase')
});