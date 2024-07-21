import pytest
import allure
import requests
import json
from datetime import datetime, timedelta
from constants import Constants
from helpers.helpers import Helpers

class TestCreateOrder:
    @allure.title('Позитивная проверка создания заказа с разными значениями поля "color"')
    @allure.description('Запрос должен вернуть правильный код и "track" заказа')
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_different_values_colors_success(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": (datetime.now() + timedelta(days=1)).strftime('%Y.%m.%d'),
            "comment": "Saske, come back to Konoha",
            "color": color
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+'/api/v1/orders', data=payload_string, headers=headers)
        r = response.json()
        print(f"создание заказа: {response.text}")
        assert 'track' in response.text
        assert response.status_code == 201
        self.track = r['track']

    @allure.issue('https://spykontishek.youtrack.cloud/issue/7M-170/Oshibka-400-Bad-Request-pri-otmene-zakaza-na-ruchku-api-v1-orders-cancel','7M-170')
    def teardown_method(self):
        helper = Helpers()
        helper.cancel_order(self.track)
