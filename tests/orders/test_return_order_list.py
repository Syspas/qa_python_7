import allure
import requests
from data import BASE_URL, ORDERS_URL

class TestReturnOrderList:
    @allure.title('В тело ответа возвращается список заказов')
    def test_list_order(self):
        """
        Тест проверяет успешное получение списка заказов.
        Ожидается:
        - Статус-код ответа 200.
        - В теле ответа должен быть ключ "orders".
        """
        # Отправляем GET-запрос для получения списка заказов
        with allure.step("Отправка запроса на получение списка заказов"):
            response = requests.get(f'{BASE_URL}{ORDERS_URL}')

        # Проверяем статус-код ответа
        with allure.step(f"Проверка статус-кода: {response.status_code}"):
            assert response.status_code == 200, f"Неверный статус-код: {response.status_code}. Ответ: {response.text}"

        # Проверяем, что в ответе есть ключ "orders"
        with allure.step("Проверка наличия ключа 'orders' в теле ответа"):
            response_json = response.json()
            assert "orders" in response_json, f"Ответ не содержит 'orders': {response_json}"
