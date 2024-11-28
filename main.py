import os
from pydub import AudioSegment
import speech_recognition as sr



# Caminho absoluto
audio_path = os.path.join(os.getcwd(), "gravar01.mp3")
print(audio_path)  # Verifique o caminho do arquivo no terminal para ter certeza


# Verificar se o arquivo de áudio existe
if not os.path.exists(audio_path):
    print(f"Erro: O arquivo {audio_path} não foi encontrado.")
    exit()

# Converter MP3 para WAV
try:
    print("Convertendo o arquivo MP3 para WAV...")
    audio = AudioSegment.from_mp3(audio_path)
    wav_path = "convertido_audio.wav"
    
    # Excluir arquivo WAV existente para evitar problemas
    if os.path.exists(wav_path):
        os.remove(wav_path)
    
    audio.export(wav_path, format="wav")
    print("Conversão concluída!")
except Exception as e:
    print(f"Erro ao converter o arquivo MP3 para WAV: {e}")
    exit()

# Inicializar o reconhecedor de fala
recognizer = sr.Recognizer()

# Abrir o arquivo de áudio no formato WAV
try:
    print("Carregando o áudio para transcrição...")
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)

    # Transcrever o áudio
    print("Transcrevendo o áudio...")
    transcription = recognizer.recognize_google(audio_data, language="pt-BR")
    print("Transcrição:", transcription)
except sr.UnknownValueError:
    print("Desculpe, não consegui entender o áudio.")
except sr.RequestError as e:
    print(f"Erro no serviço de reconhecimento: {e}")
except Exception as e:
    print(f"Erro durante a transcrição: {e}")
