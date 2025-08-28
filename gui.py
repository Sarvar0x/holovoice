# ui/gui.py

import tkinter as tk
from tkinter import messagebox
import threading
import time

from voice_engine import speak
from recognizer import recognize_voice
from commands.web_commands import handle_web_command
from commands.system_commands import handle_system_command
from commands.music import handle_music_command
from commands.gpt_chat import handle_gpt_command

theme = {
    "light": {"bg": "#f8f9fa", "fg": "#212529", "button": "#0EA5E9"},
    "dark": {"bg": "#212529", "fg": "#f8f9fa", "button": "#0EA5E9"}
}
current_theme = "light"
listening = False

def toggle_theme(root, widgets):
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    apply_theme(root, widgets)

def apply_theme(root, widgets):
    th = theme[current_theme]
    root.config(bg=th["bg"])
    for w in widgets:
        if isinstance(w, tk.Label):
            w.config(bg=th["bg"], fg=th["fg"])
        elif isinstance(w, tk.Button):
            w.config(bg=th["button"], fg="white", activebackground="#38bdf8")

def start_listening_loop(output_label):
    global listening
    listening = not listening
    if listening:
        speak("Всегда слушаю")
        output_label.config(text="🎧 Всегда слушаю...")
        threading.Thread(target=listen_forever, args=(output_label,), daemon=True).start()
    else:
        output_label.config(text="🔇 Прослушка отключена")
        speak("Прослушка отключена")

def listen_forever(output_label):
    while listening:
        run_assistant(output_label)
        time.sleep(1)

def run_assistant(output_label):
    command = recognize_voice()
    output_label.config(text=f"Вы сказали: {command}")
    if not command:
        speak("Повторите ещё раз")
        return

    # === Обработка команд ===
    if any(word in command for word in ["ютуб", "google", "поиск"]):
        handle_web_command(command)
    elif any(word in command for word in ["выключи", "открой", "громкость"]):
        handle_system_command(command)
    elif "музыку" in command:
        handle_music_command(command)
    elif "спроси gpt" in command or "спроси чат" in command:
        handle_gpt_command(command)
    else:
        speak("Команда не распознана")

def run_gui():
    root = tk.Tk()
    root.title("HoloVoice")
    root.geometry("400x300")
    root.resizable(False, False)

    title = tk.Label(root, text="🤖 HoloVoice", font=("Arial", 20, "bold"))
    status = tk.Label(root, text="Нажмите кнопку 'Говорить'", font=("Arial", 12))
    btn_speak = tk.Button(root, text="🎤 Говорить", font=("Arial", 12), command=lambda: run_assistant(status))
    btn_loop = tk.Button(root, text="🎧 Всегда слушать", font=("Arial", 12), command=lambda: start_listening_loop(status))
    btn_theme = tk.Button(root, text="🎨 Тема", font=("Arial", 12), command=lambda: toggle_theme(root, [title, status, btn_speak, btn_loop, btn_theme]))

    title.pack(pady=10)
    status.pack(pady=5)
    btn_speak.pack(pady=10)
    btn_loop.pack(pady=10)
    btn_theme.pack(pady=10)

    apply_theme(root, [title, status, btn_speak, btn_loop, btn_theme])
    root.mainloop()
