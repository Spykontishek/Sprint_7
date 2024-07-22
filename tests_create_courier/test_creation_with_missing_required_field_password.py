import pytest
import requests
import allure
import json
from constants import Constants
from faker import Faker

faker = Faker()

class TestCreateCourierWithoutPassword():
    @allure.title('Негативная проверка авторизации курьера без заполнения обязательного поля "password"')
    @allure.description('Запрос должен вернуть ошибку и правильный код ответа')
    def test_creating_сourier_without_password_error(self):
        self.login = faker.user_name()[:5]

        payload = {
            "login": self.login,
            "password": "",
            "firstName": ""
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+Constants.REG_PATH, data=payload_string, headers=headers)
        assert '"message":"Недостаточно данных для создания учетной записи"' in response.text
        assert response.status_code == 400