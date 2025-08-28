# voice_engine.py

import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
for v in voices:
    if "russian" in v.name.lower():
        engine.setProperty('voice', v.id)
        break

def speak(text):
    print("[Бот говорит]:", text)
    engine.say(text)
    engine.runAndWait()
