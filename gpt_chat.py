# commands/gpt_chat.py

import openai
from config import OPENAI_API_KEY
from voice_engine import speak

openai.api_key = OPENAI_API_KEY

def handle_gpt_command(command):
    # Убираем ключевые слова
    prompt = command.lower()
    prompt = prompt.replace("спроси gpt", "").replace("спроси чат", "").strip()

    if not prompt:
        speak("Вопрос не распознан")
        return

    speak("Обращаюсь к ChatGPT")
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
            max_tokens=150
        )

        answer = response.choices[0].message.content.strip()
        print("Ответ GPT:", answer)
        speak(answer)

    except Exception as e:
        print("Ошибка GPT:", e)
        speak("Ошибка при обращении к GPT")
