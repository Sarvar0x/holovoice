# recognizer.py

import speech_recognition as sr
from voice_engine import speak

def recognize_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Ожидание речи...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=7)
            command = r.recognize_google(audio, language="ru-RU").lower()
            print("🔎 Распознано:", command)
            return command
        except sr.WaitTimeoutError:
            print("⌛ Время ожидания вышло.")
            return ""
        except sr.UnknownValueError:
            speak("Я не понял, повторите")
            return ""
        except sr.RequestError:
            speak("Ошибка соединения")
            return ""
