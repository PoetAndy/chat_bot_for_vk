# Документация WriteSonic API: https://docs.writesonic.com/reference/introduction
# Нейронка для генерации ответов WriteSonic: https://writesonic.com/

import requests
import json
import os  # работа с файловой системой

from dotenv import load_dotenv  # для загрузки информации из .env-файла

class GenMessage:
    # Конструкция для запроса на генерацию ответа
    payload = {
        "enable_google_results": "False",
        "enable_memory": True,
        "input_text": "Some question",
        "history_data": [
            {
                "is_sent": True,
                "message": ""
            },
            {
                "is_sent": False,
                "message": ""
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": ""
    }

    def __init__(self):
        """
        Инициализация генератора
        """
        # загрузка информации из .env-файла
        load_dotenv()

    def generate_message(self, promt):
        url = os.getenv("WRITE_SONIC_URL") # Получаем URL из .env файла

        self.payload["input_text"] = promt  # Записываем вопрос пользователя в конструкцию
        self.headers["X-API-KEY"] = os.getenv("X_API_KEY")  # Записываем API из .env файла в конструкцию

        response = requests.post(url, json=self.payload, headers=self.headers) # запрос на генрацию ответа

        try:
            message = json.loads(response.text) # Получили словарь с ключевыми словами "message", "image_urls"
        except json.decoder.JSONDecodeError:
            return "Ошибка: неправильный формат ответа сервера"

        self.payload["history_data"][0]["message"] = promt  # Запись в пользовательский контекст
        self.payload["history_data"][1]["message"] = message["message"]  # Запись в сгенеренный контекст

        # Возвращаем готовый ответ
        return message["message"]