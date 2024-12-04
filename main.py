import os
from pydub import AudioSegment
import speech_recognition as sr

audio_path = "coach.mp3"
try:
  
    audio = AudioSegment.from_mp3(audio_path)
    primeiro_minuto = audio[:60000]  # 60 segundos

    wav_path = "primeiro_minuto.wav"
    primeiro_minuto.export(wav_path, format="wav", parameters=["-ar", "16000"])
    print("Primeiro minuto do áudio exportado com sucesso!")

    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_path) as source:
        print("Carregando o áudio para reconhecimento...")
        audio_data = recognizer.record(source)

    transcription = recognizer.recognize_google(audio_data, language="pt-BR")
    print("Transcrição bem-sucedida:", transcription)

    with open("transcricao.txt", "w", encoding="utf-8") as file:
        file.write(transcription)
    print("A transcrição foi salva em 'transcricao.txt'.")
    
#erros
except FileNotFoundError:
    print("Erro: O arquivo de áudio não foi encontrado.")
except sr.UnknownValueError:
    print("Desculpe, não consegui entender o áudio.")
except sr.RequestError as e:
    print(f"Erro no serviço de reconhecimento: {e}")
