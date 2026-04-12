import numpy as np
from app.core.config import RECORDINGS_DIR, SAMPLE_RATE,
from numpy.typing import NDArray
from scipy.io import wavfile
import sounddevice as sd


def salvar_audio(
    audio: NDArray[np.floating], filename: str, sample_rate: int = SAMPLE_RATE
) -> str:
    """Salva o array de áudio em um arquivo WAV."""

    # Constrói o caminho completo para o arquivo de saída, garantindo que a pasta exista
    caminho_completo = RECORDINGS_DIR / "output" / filename
    caminho_completo.parent.mkdir(parents=True, exist_ok=True)

    audio32: NDArray[np.float32] = np.asarray(audio, dtype=np.float32)

    # O astype(np.float32) é essencial para o arquivo WAV entender a amplitude de 0.5
    try:
        wavfile.write(caminho_completo, sample_rate, audio32)
        print(f"Sucesso! Áudio salvo como: {filename}")
    except Exception as e:
        print(f"Erro ao salvar áudio: {e}")

    return str(caminho_completo)
class GravadorAudio:
    """Classe responsável por converter Morse em áudio e salvar como arquivo WAV."""

    def __init__(self, gravando: bool = False, sample_rate: int = SAMPLE_RATE) -> NDArray[np.floating]:
        self.gravando = gravando
        self.sample_rate = sample_rate
        self.frames = []  # Lista para armazenar os frames de áudio durante a gravação
        self.stream = None  # Placeholder para o stream de áudio

    def _callback_audio(
        self, 
        indata: np.ndarray, 
        frames: int, 
        time: dict, 
        status: sd.CallbackFlags
    ) -> None:
        """
        Callback otimizado. 
        indata: Array NumPy (amostras, canais).
        time: Dicionário com timestamps (AdcInputTime, CurrentTime, etc).
        """
        if status:
            print(f"Status do Stream: {status}", flush=True)

        if self.gravando:
            # .copy() pois o buffer 'indata' é volátil
            self.frames.append(indata.copy())
    def iniciar_gravacao(self) -> None:
        '''chame esta funcao para iniciar a gravacao do audio'''
        self.gravando = True
        self.frames = []  # Limpa frames anteriores

        # incia o microfone e o callback de audio
        self.stream = sd.InputStream(
            samplerate=self.sample_rate, 
            channels=1, 
            dtype='float32', 
            callback=self._callback_audio
        )
        self.stream.start()
        return {"status": "gravando", "message": "Gravação iniciada com sucesso!"}
    def parar_gravacao(self):
        """Chame esta função quando o front-end enviar o sinal de FIM."""
        self.gravando = False
        if self.stream:
            self.stream.stop()
            self.stream.close()
        
        # Junta tudo em um único array
        if self.frames:
            # axis=0 para concatenar horizontalmente (amostras) pois cada frame tem duas dimensões (amostras, canais) 
            array_final = np.concatenate(self.frames, axis=0)
            return array_final
        else:
            return np.array([])
    

            
