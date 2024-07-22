import pytest
import allure
import requests
import json
from constants import Constants
from conftest import reg
from helpers.helpers import Helpers

class TestAutorizationCourierWithWrongLogin():
    @allure.title('Негативная проверка авторизации курьера с неверным заполнением обязательного поля "login"')
    @allure.description('Запрос должен вернуть ошибку и правильный код ответа')
    @pytest.mark.usefixtures('reg')
    def test_authorization_courier_with_wrong_login_error(self):
        payload = {
            "login": 'ujnio',
            "password": Constants.PASSWORD
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+Constants.AUTH_PATH, data=payload_string, headers=headers)
        assert '"message":"Учетная запись не найдена"' in response.text
        assert response.status_code == 404

    def teardown_method(self):
        helper = Helpers()
        helper.login(Constants.LOGIN, Constants.PASSWORD)
        self.id = helper.id
        helper.delete_courier(self.id)