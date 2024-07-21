import pytest
import allure
import requests
import json
from constants import Constants
from conftest import reg
from helpers.helpers import Helpers

class TestCreate2IdenticalCouriers():
    login = Constants.LOGIN
    password = Constants.PASSWORD

    @allure.title('Негативная проверка создания 2-ух одинаковых курьеров')
    @allure.description('Запрос должен вернуть ошибку и правильный код ответа')
    @pytest.mark.usefixtures('reg')
    def test_сreate_2_identical_couriers_error(self):

        payload = {
            "login": Constants.LOGIN,
            "password": Constants.PASSWORD,
            "firstName": Constants.FIRSTNAME
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+'/api/v1/courier', data=payload_string, headers=headers)
        print(f"Создание курьера: {response.text}")
        print(f'код ответа: {response.status_code}')
        assert '"message":"Этот логин уже используется. Попробуйте другой."' in response.text
        assert response.status_code == 409

    def teardown_method(self):
        helper = Helpers()
        helper.login(Constants.LOGIN, Constants.PASSWORD)
        self.id = helper.id
        helper.delete_courier(self.id)



