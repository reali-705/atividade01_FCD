import numpy as np
from scipy.io import wavfile
import config 

def morse_para_audio(
    morse: str, 
    freq_ponto: int = config.FREQUENCIA_PONTO,
    freq_traco: int = config.FREQUENCIA_TRACO,
    duracao_ponto: float = config.DURACAO_PONTO,
    duracao_traco: float = config.DURACAO_TRACO,
    pausa_digito: float = config.PAUSA_ESPACO_DIGITO_MORSE,
    pausa_letra: float = config.PAUSA_ESPACO_LETRA,
    pausa_palavra: float = config.PAUSA_ESPACO_PALAVRA,
    sample_rate: int = config.SAMPLE_RATE
) -> np.ndarray:
    """
    Converte Morse em áudio usando as definições do config.py como padrão.
    """
    
    # 1: Construção do domínio do tempo
    t_ponto = np.linspace(0, duracao_ponto, int(sample_rate * duracao_ponto), endpoint=False)
    t_traco = np.linspace(0, duracao_traco, int(sample_rate * duracao_traco), endpoint=False)
    
    # 2: Geração dos sons para ponto e traço
    som_ponto = config.AMPLITUDE * np.sin(2 * np.pi * freq_ponto * t_ponto)
    som_traco = config.AMPLITUDE * np.sin(2 * np.pi * freq_traco * t_traco)

    # 3: Construção do domínio do tempo para os silêncios
    num_amostras_digito = int(pausa_digito * sample_rate)
    num_amostras_letra = int(pausa_letra * sample_rate)
    num_amostras_palavra = int(pausa_palavra * sample_rate)

    # 4: Geração de silêncios
    silencio_digito = np.zeros(num_amostras_digito)
    silencio_letra = np.zeros(num_amostras_letra)
    silencio_palavra = np.zeros(num_amostras_palavra)

    # 5: Buffer e Loop
    audio_final = []

    for simbolo in morse:
        match simbolo:
            case '.':
                audio_final.append(som_ponto)
                audio_final.append(silencio_digito)
            case '-':
                audio_final.append(som_traco)
                audio_final.append(silencio_digito)
            case ' ':
                audio_final.append(silencio_letra)
            case '/':
                audio_final.append(silencio_palavra)
            case _: 
                print(f"Aviso: Símbolo inválido ignorado: '{simbolo}'")
        
    # Prevenção de erro: se a string for vazia, retorna array vazio
    if len(audio_final) == 0:
        return np.array([])
        
    return np.concatenate(audio_final)

def salvar_audio(audio: np.ndarray, filename: str, sample_rate: int = config.SAMPLE_RATE):
    """Salva o array de áudio em um arquivo WAV."""
    
    # O astype(np.float32) é essencial para o arquivo WAV entender a amplitude de 0.5
    wavfile.write(filename, sample_rate, audio.astype(np.float32))
    print(f"Sucesso! Áudio salvo como: {filename}")

