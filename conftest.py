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
    requests.post(Constants.URL+Constants.REG_PATH, data=payload_string, headers=headers)




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
    requests.post(Constants.URL+Constants.CREATE_PATH, data=payload_string, headers=headers)





