import pytest
from constants import Constants
import requests
import json
from datetime import datetime, timedelta

@pytest.fixture
def reg():
    payload = {
        "login": Constants.LOGIN,
        "password": Constants.PASSWORD,
        "firstName": Constants.FIRSTNAME
    }
    payload_string = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(Constants.URL + '/api/v1/courier', data=payload_string, headers=headers)
    print(f"Создание курьера: {response.text}")
    print(f'код ответа: {response.status_code}')


@pytest.fixture
def delete(self, id):
    self.id = id
    response = requests.delete(Constants.URL+'/api/v1/courier/{}'.format(self.id))
    print(f"удаление курьера: {response.text}")


@pytest.fixture(scope="function", params=["3333", "4444"])
def create_order_with_different_values_metroStation(request):
    metroStation = request.param
    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": metroStation,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": (datetime.now() + timedelta(days=1)).strftime('%Y.%m.%d'),
        "comment": "Saske, come back to Konoha",
        "color": [
    "BLACK"
    ]
    }
    payload_string = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(Constants.URL+'/api/v1/orders', data=payload_string, headers=headers)
    print(f"создание заказа: {response.text}")




