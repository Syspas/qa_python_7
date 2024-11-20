import pytest

@pytest.fixture()
def order_methods():
    return OrderMethods()

@pytest.fixture()
def courier_methods():
    return CourierMethods()

@pytest.fixture()
def courier(courier_methods):
    response = courier_methods.create_courier(COURIER_NAME)
    yield response.json()['id']
    courier_methods.delete_courier(response.json()['id'])
