import allure
import requests
from methods.register_courier import CourierMethods  # Импорт методов курьеров


class TestCreateCourier:
    @allure.title('Создание нового курьера')
    def test_create_courier(self):
        """
        Тест для создания нового курьера.

        Ожидаемый результат:
            Статус-код ответа 201, и тело ответа должно содержать {"ok": True}.
        """
        courier_data = CourierMethods.register_new_courier_and_return_login_password()

        assert courier_data is not None, "Ошибка при создании курьера: данные не были возвращены"

        payload = {
            "login": courier_data['login'],
            "password": courier_data['password'],
            "firstName": courier_data['first_name']
        }

        response = requests.post(CourierMethods.COURIER_API, json=payload)

        assert response.status_code == 201, f"Неверный статус-код: {response.status_code}"
        assert response.json() == {"ok": True}, f"Неверное тело ответа: {response.json()}"

    @allure.title('Создание курьера с одинаковым логином')
    def test_create_courier_with_duplicate_login(self):
        """
        Тест для проверки, что нельзя создать курьера с логином,
        который уже используется.

        Ожидаемый результат:
            Второй запрос возвращает статус-код 409 и сообщение
            'Этот логин уже используется'.
        """
        courier_data = CourierMethods.register_new_courier_and_return_login_password()

        assert courier_data is not None, "Ошибка при создании первого курьера: данные не были возвращены"

        payload = {
            "login": courier_data['login'],
            "password": courier_data['password'],
            "firstName": courier_data['first_name']
        }

        # Первый запрос для регистрации курьера
        requests.post(CourierMethods.COURIER_API, json=payload)

        # Второй запрос с тем же логином
        response = requests.post(CourierMethods.COURIER_API, json=payload)

        assert response.status_code == 409, f"Неверный статус-код: {response.status_code}"
        assert 'Этот логин уже используется' in response.text, f"Неверное сообщение: {response.text}"

    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login(self):
        """
        Тест для проверки, что нельзя создать курьера без логина.

        Ожидаемый результат:
            Запрос возвращает статус-код 400 и сообщение
            'Недостаточно данных для создания учетной записи'.
        """
        payload = {
            "password": CourierMethods.generate_random_string(10),
            "firstName": CourierMethods.generate_random_string(10)
        }

        response = requests.post(CourierMethods.COURIER_API, json=payload)

        assert response.status_code == 400, f"Неверный статус-код: {response.status_code}"
        assert 'Недостаточно данных для создания учетной записи' in response.text, f"Неверное сообщение: {response.text}"

    @allure.title('Нельзя создать курьера без пароля')
    def test_create_courier_without_password(self):
        """
        Тест для проверки, что нельзя создать курьера без пароля.

        Ожидаемый результат:
            Запрос возвращает статус-код 400 и сообщение
            'Недостаточно данных для создания учетной записи'.
        """
        payload = {
            "login": CourierMethods.generate_random_string(10),
            "firstName": CourierMethods.generate_random_string(10)
        }

        response = requests.post(CourierMethods.COURIER_API, json=payload)

        assert response.status_code == 400, f"Неверный статус-код: {response.status_code}"
        assert 'Недостаточно данных для создания учетной записи' in response.text, f"Неверное сообщение: {response.text}"
