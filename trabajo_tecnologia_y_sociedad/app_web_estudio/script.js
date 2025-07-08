// Textos de la exposición extraídos del guión
const textos_exposicion = [
    "Buenas tardes, somos Marto, Rocío y Naty",
    "y hoy vamos a presentar",
    "nuestro trabajo titulado",
    "IA, prevención de fraude y trabajo en Fintech: una perspectiva socio-ética",
    "El objetivo principal fue",
    "analizar cómo se aplica la inteligencia artificial",
    "en la detección de fraudes",
    "dentro del ecosistema Fintech",
    "enfocándonos no solo en lo técnico",
    "sino también en los aspectos éticos, laborales y sociales.",
    "Partimos de una hipótesis central",
    "la inteligencia artificial no es neutral",
    "Su diseño, entrenamiento y uso",
    "tienen impactos directos sobre las personas",
    "y la sociedad",
    "Por eso, creemos que su implementación",
    "debe ser crítica, responsable y ética."
];

// Duraciones exactas de cada audio individual (en segundos)
const duracionesAudios = [4.44, 2.112, 2.16, 7.8, 2.376, 4.224, 2.352, 2.688, 2.928, 4.824, 3.0, 3.672, 3.408, 3.384, 1.224, 3.48, 3.96];

// Configuración de tiempos (en segundos)
// Cada frase se repite 5 veces en el audio principal
const REPETICIONES_POR_FRASE = 5;

// Calcular los tiempos de inicio de cada frase usando las duraciones reales
const tiemposInicio = [];
let tiempoAcumulado = 0;

for (let i = 0; i < textos_exposicion.length; i++) {
    tiemposInicio.push(tiempoAcumulado);
    // Cada audio se repite 5 veces, así que sumamos 5 veces su duración
    tiempoAcumulado += REPETICIONES_POR_FRASE * duracionesAudios[i];
}

// Variables globales
let audioElement;
let currentActivePhrase = -1;
let isScriptVisible = false;
let updateInterval;

// Variables para grabación de audio
let mediaRecorder;
let recordedChunks = [];
let recordedAudioBlob;
let recordedAudioUrl;
let recordingAudio;
let isRecording = false;
let isPlayingRecording = false;
let recordingTimer;
let recordingStartTime;

// Inicialización cuando se carga la página
document.addEventListener('DOMContentLoaded', function() {
    audioElement = document.getElementById('mainAudio');
    
    // Configurar volumen inicial al 30%
    audioElement.volume = 0.3;
    
    // Crear botones de frases
    createPhraseButtons();
    
    // Crear contenido del guión
    createScriptContent();
    
    // Configurar event listeners
    setupEventListeners();
    
    // Inicializar display de tiempo
    updateTimeDisplay();
});

// Crear botones para cada frase
function createPhraseButtons() {
    const buttonsContainer = document.getElementById('phraseButtons');
    
    textos_exposicion.forEach((texto, index) => {
        const button = document.createElement('button');
        button.className = 'phrase-btn';
        button.textContent = `${index + 1}. ${texto}`;
        button.onclick = () => jumpToPhrase(index);
        button.id = `phrase-btn-${index}`;
        
        buttonsContainer.appendChild(button);
    });
}

// Crear contenido del guión
function createScriptContent() {
    const scriptContainer = document.getElementById('scriptContent');
    
    textos_exposicion.forEach((texto, index) => {
        const textElement = document.createElement('div');
        textElement.className = 'script-text';
        textElement.textContent = `${index + 1}. ${texto}`;
        textElement.id = `script-text-${index}`;
        
        scriptContainer.appendChild(textElement);
    });
}

// Configurar todos los event listeners
function setupEventListeners() {
    // Event listeners del audio
    audioElement.addEventListener('timeupdate', updateCurrentPhrase);
    audioElement.addEventListener('loadedmetadata', updateTimeDisplay);
    audioElement.addEventListener('timeupdate', updateTimeDisplay);
    audioElement.addEventListener('play', startUpdateInterval);
    audioElement.addEventListener('pause', stopUpdateInterval);
    audioElement.addEventListener('ended', stopUpdateInterval);
    
    // Event listener para limpiar texto
    document.getElementById('clearTextBtn').addEventListener('click', clearUserText);
    
    // Event listener para mostrar/ocultar guión
    document.getElementById('toggleScriptBtn').addEventListener('click', toggleScript);
    
    // Event listeners para grabación de audio
    document.getElementById('recordBtn').addEventListener('click', toggleRecording);
    document.getElementById('playRecordingBtn').addEventListener('click', togglePlayRecording);
    document.getElementById('discardBtn').addEventListener('click', discardRecording);
}

// Saltar a una frase específica (al inicio de la primera repetición)
function jumpToPhrase(phraseIndex) {
    if (phraseIndex >= 0 && phraseIndex < tiemposInicio.length) {
        // Saltar exactamente al inicio de la primera repetición de la frase
        const targetTime = tiemposInicio[phraseIndex];
        audioElement.currentTime = targetTime;
        
        console.log(`Saltando a la frase ${phraseIndex + 1}: "${textos_exposicion[phraseIndex]}" en el tiempo ${targetTime.toFixed(2)}s`);
        
        // Si el audio no está reproduciéndose, iniciarlo
        if (audioElement.paused) {
            audioElement.play().catch(e => {
                console.log('Error al reproducir audio:', e);
            });
        }
        
        // Actualizar inmediatamente la frase activa
        setTimeout(() => {
            updateCurrentPhrase();
        }, 100); // Pequeño delay para asegurar que el tiempo se haya actualizado
    }
}

// Actualizar la frase activa basada en el tiempo actual
function updateCurrentPhrase() {
    const currentTime = audioElement.currentTime;
    let newActivePhrase = -1;
    
    // Encontrar la frase actual
    for (let i = 0; i < tiemposInicio.length; i++) {
        if (currentTime >= tiemposInicio[i]) {
            newActivePhrase = i;
        } else {
            break;
        }
    }
    
    // Solo actualizar si cambió la frase activa
    if (newActivePhrase !== currentActivePhrase) {
        // Remover clase activa del botón anterior
        if (currentActivePhrase >= 0) {
            const prevButton = document.getElementById(`phrase-btn-${currentActivePhrase}`);
            if (prevButton) {
                prevButton.classList.remove('active');
            }
        }
        
        // Agregar clase activa al botón actual
        if (newActivePhrase >= 0) {
            const currentButton = document.getElementById(`phrase-btn-${newActivePhrase}`);
            if (currentButton) {
                currentButton.classList.add('active');
            }
        }
        
        currentActivePhrase = newActivePhrase;
        
        // Actualizar el guión si está visible
        if (isScriptVisible) {
            updateScriptHighlight();
        }
    }
}

// Actualizar el resaltado del guión
function updateScriptHighlight() {
    // Remover todas las clases de resaltado
    document.querySelectorAll('.script-text').forEach(element => {
        element.classList.remove('current', 'highlight');
    });
    
    // Resaltar desde el inicio hasta la frase actual
    if (currentActivePhrase >= 0) {
        for (let i = 0; i <= currentActivePhrase; i++) {
            const scriptElement = document.getElementById(`script-text-${i}`);
            if (scriptElement) {
                if (i === currentActivePhrase) {
                    scriptElement.classList.add('current');
                } else {
                    scriptElement.classList.add('highlight');
                }
            }
        }
        
        // Hacer scroll al elemento actual
        const currentScriptElement = document.getElementById(`script-text-${currentActivePhrase}`);
        if (currentScriptElement) {
            currentScriptElement.scrollIntoView({ 
                behavior: 'smooth', 
                block: 'center' 
            });
        }
    }
}

// Actualizar display de tiempo
function updateTimeDisplay() {
    const currentTime = audioElement.currentTime || 0;
    const duration = audioElement.duration || 0;
    
    document.getElementById('currentTime').textContent = formatTime(currentTime);
    document.getElementById('duration').textContent = formatTime(duration);
}

// Formatear tiempo en MM:SS
function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = Math.floor(seconds % 60);
    return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
}

// Limpiar texto del usuario
function clearUserText() {
    const userTextArea = document.getElementById('userText');
    userTextArea.value = '';
    userTextArea.focus();
}

// Mostrar/ocultar guión
function toggleScript() {
    const scriptContent = document.getElementById('scriptContent');
    const toggleButton = document.getElementById('toggleScriptBtn');
    
    isScriptVisible = !isScriptVisible;
    
    if (isScriptVisible) {
        scriptContent.classList.remove('hidden');
        toggleButton.textContent = 'Ocultar Guión';
        updateScriptHighlight();
    } else {
        scriptContent.classList.add('hidden');
        toggleButton.textContent = 'Mostrar Guión';
    }
}

// Iniciar intervalo de actualización
function startUpdateInterval() {
    if (updateInterval) {
        clearInterval(updateInterval);
    }
    
    updateInterval = setInterval(() => {
        updateCurrentPhrase();
        updateTimeDisplay();
    }, 100); // Actualizar cada 100ms para mayor precisión
}

// Detener intervalo de actualización
function stopUpdateInterval() {
    if (updateInterval) {
        clearInterval(updateInterval);
        updateInterval = null;
    }
}

// Función para calibrar los tiempos manualmente si es necesario
function calibrateTimings() {
    // Esta función puede usarse para ajustar los tiempos manualmente
    // basándose en la duración real del audio
    console.log('Duración total del audio:', audioElement.duration);
    console.log('Tiempos calculados:', tiemposInicio);
    console.log('Duraciones individuales:', duracionesAudios);
    
    // Calcular duración total esperada
    const duracionTotalEsperada = duracionesAudios.reduce((total, duracion) => total + (duracion * REPETICIONES_POR_FRASE), 0);
    console.log('Duración total esperada:', duracionTotalEsperada, 'segundos');
    
    // Mostrar tabla de tiempos para cada frase
    console.table(textos_exposicion.map((texto, index) => ({
        frase: index + 1,
        texto: texto.substring(0, 50) + (texto.length > 50 ? '...' : ''),
        inicio: tiemposInicio[index].toFixed(2) + 's',
        duracionIndividual: duracionesAudios[index] + 's',
        duracionTotal: (duracionesAudios[index] * REPETICIONES_POR_FRASE).toFixed(2) + 's'
    })));
}

// Función de utilidad para debugging
function debugCurrentTime() {
    console.log('Tiempo actual:', audioElement.currentTime);
    console.log('Frase activa:', currentActivePhrase);
    console.log('Texto actual:', currentActivePhrase >= 0 ? textos_exposicion[currentActivePhrase] : 'Ninguna');
}

// Exportar funciones para uso en consola si es necesario
window.debugAudio = {
    calibrateTimings,
    debugCurrentTime,
    jumpToPhrase,
    tiemposInicio,
    textos_exposicion,
    duracionesAudios,
    REPETICIONES_POR_FRASE
};

// ============ FUNCIONES DE GRABACIÓN DE AUDIO ============

// Iniciar/detener grabación
async function toggleRecording() {
    if (!isRecording) {
        await startRecording();
    } else {
        stopRecording();
    }
}

// Iniciar grabación
async function startRecording() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        
        recordedChunks = [];
        mediaRecorder = new MediaRecorder(stream);
        
        mediaRecorder.ondataavailable = function(event) {
            if (event.data.size > 0) {
                recordedChunks.push(event.data);
            }
        };
        
        mediaRecorder.onstop = function() {
            recordedAudioBlob = new Blob(recordedChunks, { type: 'audio/webm' });
            recordedAudioUrl = URL.createObjectURL(recordedAudioBlob);
            
            // Crear elemento de audio para reproducir
            if (recordingAudio) {
                recordingAudio.pause();
                recordingAudio = null;
            }
            
            recordingAudio = new Audio(recordedAudioUrl);
            recordingAudio.addEventListener('ended', () => {
                updatePlayButton(false);
            });
            
            // Habilitar botones
            document.getElementById('playRecordingBtn').disabled = false;
            document.getElementById('discardBtn').disabled = false;
        };
        
        mediaRecorder.start();
        isRecording = true;
        recordingStartTime = Date.now();
        
        // Actualizar UI
        updateRecordingUI();
        startRecordingTimer();
        
    } catch (error) {
        console.error('Error al acceder al micrófono:', error);
        updateStatus('Error al acceder al micrófono');
    }
}

// Detener grabación
function stopRecording() {
    if (mediaRecorder && isRecording) {
        mediaRecorder.stop();
        
        // Detener el stream
        if (mediaRecorder.stream) {
            mediaRecorder.stream.getTracks().forEach(track => track.stop());
        }
        
        isRecording = false;
        stopRecordingTimer();
        updateRecordingUI();
        updateStatus('Grabación completada');
    }
}

// Reproducir/pausar grabación
function togglePlayRecording() {
    if (!recordingAudio) return;
    
    if (!isPlayingRecording) {
        recordingAudio.play();
        isPlayingRecording = true;
        updatePlayButton(true);
    } else {
        recordingAudio.pause();
        isPlayingRecording = false;
        updatePlayButton(false);
    }
}

// Descartar grabación
function discardRecording() {
    if (recordingAudio) {
        recordingAudio.pause();
        recordingAudio = null;
    }
    
    if (recordedAudioUrl) {
        URL.revokeObjectURL(recordedAudioUrl);
        recordedAudioUrl = null;
    }
    
    recordedAudioBlob = null;
    recordedChunks = [];
    isPlayingRecording = false;
    
    // Actualizar UI
    document.getElementById('playRecordingBtn').disabled = true;
    document.getElementById('discardBtn').disabled = true;
    updatePlayButton(false);
    updateStatus('Listo para grabar');
    updateRecordingTime('0:00');
}

// Actualizar UI de grabación
function updateRecordingUI() {
    const recordBtn = document.getElementById('recordBtn');
    
    if (isRecording) {
        recordBtn.textContent = '⏹️ Detener';
        recordBtn.classList.add('recording');
        updateStatus('Grabando...');
    } else {
        recordBtn.textContent = '🎤 Grabar';
        recordBtn.classList.remove('recording');
    }
}

// Actualizar botón de reproducir
function updatePlayButton(isPlaying) {
    const playBtn = document.getElementById('playRecordingBtn');
    
    if (isPlaying) {
        playBtn.textContent = '⏸️ Pausar';
    } else {
        playBtn.textContent = '▶️ Reproducir';
    }
}

// Actualizar estado de grabación
function updateStatus(status) {
    document.getElementById('recordingStatus').textContent = status;
}

// Actualizar tiempo de grabación
function updateRecordingTime(time) {
    document.getElementById('recordingTime').textContent = time;
}

// Iniciar temporizador de grabación
function startRecordingTimer() {
    recordingTimer = setInterval(() => {
        const elapsed = Math.floor((Date.now() - recordingStartTime) / 1000);
        const minutes = Math.floor(elapsed / 60);
        const seconds = elapsed % 60;
        updateRecordingTime(`${minutes}:${seconds.toString().padStart(2, '0')}`);
    }, 1000);
}

// Detener temporizador de grabación
function stopRecordingTimer() {
    if (recordingTimer) {
        clearInterval(recordingTimer);
        recordingTimer = null;
    }
}
