# commands/system_commands.py

import os
import pyautogui
from voice_engine import speak

def handle_system_command(command):
    if "выключи компьютер" in command:
        speak("Выключаю компьютер")
        os.system("shutdown /s /t 1")
    
    elif "перезагрузи компьютер" in command:
        speak("Перезагружаю")
        os.system("shutdown /r /t 1")
    
    elif "открой загрузки" in command:
        speak("Открываю папку загрузок")
        downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        os.startfile(downloads)
    
    elif "открой документы" in command:
        speak("Открываю документы")
        docs = os.path.join(os.path.expanduser("~"), "Documents")
        os.startfile(docs)

    elif "громкость вверх" in command:
        pyautogui.press("volumeup")
        speak("Громкость увеличена")

    elif "громкость вниз" in command:
        pyautogui.press("volumedown")
        speak("Громкость уменьшена")

    elif "громкость отключи" in command:
        pyautogui.press("volumemute")
        speak("Громкость отключена")

    else:
        speak("Системная команда не распознана")
