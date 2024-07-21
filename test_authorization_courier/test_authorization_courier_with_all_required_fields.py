import pytest
import allure
import requests
import json
from constants import Constants
from conftest import reg
from helpers.helpers import Helpers


class TestAutorizationCourier():
    @allure.title('Позитивная проверка авторизации курьера с заполнением всех обязательных полей')
    @allure.description('Запрос должен вернуть правильный код ответа и "id" курьера')
    @pytest.mark.usefixtures('reg')
    def test_authorization_courier_success(self):
        payload = {
            "login": Constants.LOGIN,
            "password": Constants.PASSWORD
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+'/api/v1/courier/login', data=payload_string, headers=headers)
        r = response.json()
        print(f"Авторизация курьера: {response.text}")
        assert 'id' in response.text
        assert response.status_code == 200
        self.id = r['id']

    def teardown_method(self):
        helper = Helpers()
        helper.delete_courier(self.id)




