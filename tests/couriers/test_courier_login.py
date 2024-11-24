import allure
import requests
import pytest
# Импорт констант из модуля config
from config import BASE_URL, COURIERS_URL

class TestLoginCourier:

    @allure.title('Авторизация под курьером выдает id')
    def test_courier_log_in(self):
        """
        Тест проверяет успешную авторизацию курьера.
        Ожидаемый результат:
        - Статус-код ответа 200.
        - В теле ответа должен содержаться 'id'.
        """
        # Данные для авторизации (замените на реальные)
        data_current = {
            "login": "valid_login",
            "password": "valid_password"
        }

        # Отправляем POST-запрос для авторизации
        response = requests.post(
            f'{BASE_URL}{COURIERS_URL}login',
            json=data_current
        )

        # Проверяем статус-код и наличие 'id' в ответе
        with allure.step(f"Проверка статус-кода: {response.status_code}"):
            assert response.status_code == 200, f"Неверный статус-код: {response.status_code}. Ответ: {response.text}"

        with allure.step("Проверка наличия 'id' в ответе"):
            assert 'id' in response.json(), f"Ответ не содержит 'id': {response.json()}"

    @allure.title('Ошибка при авторизации если логин или пароль не корректные')
    def test_courier_log_negative(self):
        """
        Тест проверяет ошибку при неверных данных для авторизации.
        Ожидаемый результат:
        - Статус-код ответа 404.
        - Ответ должен содержать сообщение 'Учетная запись не найдена'.
        """
        # Данные с неверным логином или паролем
        data_negative = {
            "login": "invalid_login",
            "password": "invalid_password"
        }

        # Отправляем POST-запрос для авторизации с неверными данными
        response = requests.post(
            f'{BASE_URL}{COURIERS_URL}login',
            json=data_negative
        )

        # Проверяем статус-код и содержание ответа
        with allure.step(f"Проверка статус-кода: {response.status_code}"):
            assert response.status_code == 404, f"Неверный статус-код: {response.status_code}. Ответ: {response.text}"

        with allure.step("Проверка текста ошибки в ответе"):
            assert 'Учетная запись не найдена' in response.text, f"Ответ не содержит 'Учетная запись не найдена': {response.text}"

    @pytest.mark.parametrize('data_without_login_or_password', [
        {"password": "valid_password"},
        {"login": "valid_login"}
    ])
    @allure.title('Ошибка при авторизации если не заполнить логин или пароль')
    def test_courier_log_not_all_data(self, data_without_login_or_password):
        """
        Тест проверяет ошибку при отсутствии логина или пароля.
        Ожидаемый результат:
        - Статус-код ответа 400.
        - Ответ должен содержать сообщение 'Недостаточно данных для входа'.
        """
        # Отправляем POST-запрос с неполными данными
        response = requests.post(
            f'{BASE_URL}{COURIERS_URL}login',
            json=data_without_login_or_password
        )

        # Проверяем статус-код и содержание ответа
        with allure.step(f"Проверка статус-кода: {response.status_code}"):
            assert response.status_code == 400, f"Неверный статус-код: {response.status_code}. Ответ: {response.text}"

        with allure.step("Проверка текста ошибки в ответе"):
            assert 'Недостаточно данных для входа' in response.text, f"Ответ не содержит 'Недостаточно данных для входа': {response.text}"
