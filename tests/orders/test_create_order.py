import json
import allure
import pytest
import requests
from data import ORDER_DATA_1, ORDER_DATA_2, BASE_URL, ORDERS_URL


class TestCreateOrder:
    @pytest.mark.parametrize(
        'order_data_base, order_color',
        [
            (ORDER_DATA_1, {"color": ["BLACK"]}),
            (ORDER_DATA_1, {"color": [""]}),
            (ORDER_DATA_2, {"color": ["GREY"]}),
            (ORDER_DATA_2, {"color": ["BLACK", "GREY"]}),
        ]
    )
    @allure.title('Создание заказа с разными параметрами данных и цвета')
    def test_create_order(self, order_data_base, order_color):
        """
        Тест проверяет успешное создание заказа с разными наборами данных и параметрами цвета.
        """
        with allure.step("Подготовка данных для заказа"):
            order_data_to_send = self.prepare_order_data(order_data_base, order_color)

        with allure.step("Отправка запроса на создание заказа"):
            response = self.send_create_order_request(order_data_to_send)

        with allure.step("Проверка ответа на корректность"):
            self.check_response(response)

    @allure.step("Подготовка данных для заказа")
    def prepare_order_data(self, base_data, additional_data):
        """
        Создает и возвращает данные для заказа, объединяя базовые и дополнительные параметры.
        """
        order_data = base_data.copy()  # Базовые данные заказа (ORDER_DATA_1 или ORDER_DATA_2)
        order_data.update(additional_data)  # Добавляем параметры цвета
        return order_data

    @allure.step("Отправка POST-запроса на создание заказа")
    def send_create_order_request(self, order_data):
        """
        Отправляет POST-запрос на создание заказа и возвращает ответ.
        """
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            f'{BASE_URL}{ORDERS_URL}',
            data=json.dumps(order_data),
            headers=headers
        )
        # Вложение отправленных данных и ответа в отчет Allure
        allure.attach(
            json.dumps(order_data, indent=4),
            name="Отправленные данные",
            attachment_type=allure.attachment_type.JSON
        )
        allure.attach(
            response.text,
            name="Ответ сервера",
            attachment_type=allure.attachment_type.TEXT
        )
        return response

    @allure.step("Проверка ответа сервера")
    def check_response(self, response):
        """
        Проверяет статус-код и наличие поля 'track' в ответе сервера.
        """
        assert response.status_code == 201, (
            f"Неверный статус-код: {response.status_code}. Ожидаемый: 201. Ответ: {response.text}"
        )
        assert 'track' in response.json(), (
            f"Ответ не содержит ключ 'track': {response.json()}"
        )
