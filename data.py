BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
ORDERS_URL = 'orders/'
COURIERS_URL = 'courier/'

# Данные для тестов заказов
ORDER_DATA_1 = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": "ул. Тестовая, д. 1",
    "metroStation": 4,
    "phone": "+7 999 999 99 99",
    "rentTime": 5,
    "deliveryDate": "2024-11-21",
    "comment": "Тестовый заказ",
    "color": ["BLACK"]
}

ORDER_DATA_2 = {
    "firstName": "Анна",
    "lastName": "Петрова",
    "address": "ул. Примерная, д. 5",
    "metroStation": 7,
    "phone": "+7 888 888 88 88",
    "rentTime": 3,
    "deliveryDate": "2024-11-22",
    "comment": "Ещё один тестовый заказ",
    "color": ["GREY"]
}