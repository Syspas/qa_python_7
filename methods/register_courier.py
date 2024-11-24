import requests
import random
import string
# Импорт констант из модуля config
from config import BASE_URL, COURIERS_URL

class CourierMethods:
    COURIER_API = f"{BASE_URL}{COURIERS_URL}"

    @staticmethod
    def generate_random_string(length: int) -> str:
        """
        Генерирует случайную строку из букв нижнего регистра заданной длины.
        :param length: Длина строки.
        :return: Случайная строка.
        """
        return ''.join(random.choices(string.ascii_lowercase, k=length))

    @classmethod
    def register_new_courier_and_return_login_password(cls):
        """
        Регистрирует нового курьера и возвращает логин, пароль и имя курьера.
        Если регистрация не удалась, возвращает пустой список.
        :return: Список [логин, пароль, имя] или пустой список.
        """
        # Генерация данных курьера
        login = cls.generate_random_string(10)
        password = cls.generate_random_string(10)
        first_name = cls.generate_random_string(10)

        # Формируем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        try:
            # Отправляем POST-запрос
            response = requests.post(cls.COURIER_API, json=payload)

            # Успешная регистрация
            if response.status_code == 201:
                return {
                    "login": login,
                    "password": password,
                    "first_name": first_name
                }

            # Если регистрация не удалась
            print(f"Ошибка регистрации: {response.status_code}, {response.json()}")

        except requests.RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")

        # Возвращаем пустой список в случае ошибки
        return None
