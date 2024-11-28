import os
from pydub import AudioSegment
import speech_recognition as sr

# Caminho para o arquivo de áudio
audio_path = "coach.mp3"

try:
    # Carregar o áudio e recortar o primeiro minuto (60.000 ms)
    audio = AudioSegment.from_mp3(audio_path)
    primeiro_minuto = audio[:60000]  # 60 segundos

    # Exportar o áudio recortado como WAV
    wav_path = "primeiro_minuto.wav"
    primeiro_minuto.export(wav_path, format="wav", parameters=["-ar", "16000"])
    print("Primeiro minuto do áudio exportado com sucesso!")

    # Inicializar o reconhecedor
    recognizer = sr.Recognizer()

    # Abrir o áudio no formato WAV
    with sr.AudioFile(wav_path) as source:
        print("Carregando o áudio para reconhecimento...")
        audio_data = recognizer.record(source)

    # Transcrever o áudio
    transcription = recognizer.recognize_google(audio_data, language="pt-BR")
    print("Transcrição bem-sucedida:", transcription)

    # Salvar a transcrição em um arquivo de texto
    with open("transcricao.txt", "w", encoding="utf-8") as file:
        file.write(transcription)
    print("A transcrição foi salva em 'transcricao.txt'.")

except FileNotFoundError:
    print("Erro: O arquivo de áudio não foi encontrado.")
except sr.UnknownValueError:
    print("Desculpe, não consegui entender o áudio.")
except sr.RequestError as e:
    print(f"Erro no serviço de reconhecimento: {e}")
