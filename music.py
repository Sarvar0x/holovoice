# commands/music.py

from youtubesearchpython import VideosSearch
import webbrowser
from voice_engine import speak

def handle_music_command(command):
    try:
        # Удаляем ключевые слова
        query = command.lower().replace("включи музыку", "").replace("включи", "").replace("музыку", "").strip()
        if not query:
            query = "Узбекская музыка"

        speak(f"Ищу {query} на YouTube...")

        search = VideosSearch(query, limit=1)
        result = search.result()

        if result and result.get("result"):
            url = result["result"][0]["link"]
            webbrowser.open(url)
            speak("Воспроизвожу музыку")    
        else:
            speak("Не удалось найти музыку")
    except Exception as e:
        print("❌ Ошибка при поиске:", str(e))
        speak("Произошла ошибка при поиске музыки")
