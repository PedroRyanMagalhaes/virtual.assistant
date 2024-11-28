import os
from pydub import AudioSegment
import speech_recognition as sr

# Caminho para o arquivo de áudio
audio_path = "gravar02.mp3"

# Converter MP3 para WAV
audio = AudioSegment.from_mp3(audio_path)
wav_path = "convertido_audio.wav"
audio.export(wav_path, format="wav")

# Inicializar o reconhecedor
recognizer = sr.Recognizer()

# Abrir o áudio no formato WAV
with sr.AudioFile(wav_path) as source:
    audio_data = recognizer.record(source)

# Transcrever o áudio
try:
    transcription = recognizer.recognize_google(audio_data, language="pt-BR")
    print("Transcrição:", transcription)

    # Salvar a transcrição em um arquivo de texto
    with open("transcricao.txt", "w", encoding="utf-8") as file:
        file.write(transcription)
    print("A transcrição foi salva em 'transcricao.txt'.")

except sr.UnknownValueError:
    print("Desculpe, não consegui entender o áudio.")
except sr.RequestError as e:
    print(f"Erro no serviço de reconhecimento: {e}")
