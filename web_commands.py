# commands/web_commands.py

import webbrowser
from voice_engine import speak

def handle_web_command(command):
    if "ютуб" in command:
        speak("Открываю YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "гугл" in command or "google" in command:
        speak("Открываю Google")
        webbrowser.open("https://www.google.com")
    elif "поиск" in command:
        query = command.replace("поиск", "").strip()
        url = f"https://www.google.com/search?q={query}"
        speak(f"Ищу {query}")
        webbrowser.open(url)
    else:
        speak("Не удалось обработать интернет-команду")
