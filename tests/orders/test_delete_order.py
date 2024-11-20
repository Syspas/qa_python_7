import allure
import requests
from data import BASE_URL, COURIERS_URL


class TestDeleteCourier:

    @allure.title('Удаление курьера по id')
    def test_delete_courier_success(self):
        """
        Тест проверяет успешное удаление курьера по его ID.
        Ожидаемый результат:
        - Статус-код ответа 200.
        - Ответ содержит {"ok": true}.
        """
        # Предположим, что курьер с id "3" существует
        courier_id = "3"
        response = requests.delete(
            f'{BASE_URL}{COURIERS_URL}{courier_id}'
        )

        with allure.step(f"Проверка статус-кода: {response.status_code}"):
            assert response.status_code == 200, f"Неверный статус-код: {response.status_code}. Ответ: {response.text}"

        with allure.step("Проверка содержания ответа"):
            assert response.json() == {"ok": True}, f"Ответ не содержит 'ok': {response.json()}"

    @allure.title('Ошибка при удалении без id')
    def test_delete_courier_no_id(self):
        """
        Тест проверяет ошибку при попытке удалить курьера без указания id.
        Ожидаемый результат:
        - Статус-код ответа 400.
        - Ответ содержит сообщение "Недостаточно данных для удаления курьера".
        """
        response = requests.delete(
            f'{BASE_URL}{COURIERS_URL}'
        )

        with allure.step(f"Проверка статус-кода: {response.status_code}"):
            assert response.status_code == 400, f"Неверный статус-код: {response.status_code}. Ответ: {response.text}"

        with allure.step("Проверка текста ошибки в ответе"):
            assert response.json().get("message") == "Недостаточно данных для удаления курьера", \
                f"Ответ не содержит ожидаемое сообщение: {response.json()}"

    @allure.title('Ошибка при удалении несуществующего курьера')
    def test_delete_courier_not_found(self):
        """
        Тест проверяет ошибку при попытке удалить курьера с несуществующим id.
        Ожидаемый результат:
        - Статус-код ответа 404.
        - Ответ содержит сообщение "Курьера с таким id нет".
        """
        # ID несуществующего курьера
        courier_id = "99999"
        response = requests.delete(
            f'{BASE_URL}{COURIERS_URL}{courier_id}'
        )

        with allure.step(f"Проверка статус-кода: {response.status_code}"):
            assert response.status_code == 404, f"Неверный статус-код: {response.status_code}. Ответ: {response.text}"

        with allure.step("Проверка текста ошибки в ответе"):
            assert response.json().get("message") == "Курьера с таким id нет", \
                f"Ответ не содержит ожидаемое сообщение: {response.json()}"
