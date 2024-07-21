import pytest
import requests
import allure
import json
from constants import Constants
from faker import Faker

faker = Faker()

class TestCreateCourierWithoutLogin():
    @allure.title('Негативная проверка создания курьера без заполнения обязательного поля "login"')
    @allure.description('Запрос должен вернуть ошибку и правильный код ответа')
    def test_creating_сourier_without_login_error(self):
        self.password = faker.password()[:4]

        payload = {
            "login": "",
            "password": self.password,
            "firstName": ""
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+'/api/v1/courier', data=payload_string, headers=headers)
        print(f"Создание курьера: {response.text}")
        print(f'код ответа: {response.status_code}')
        assert '"message":"Недостаточно данных для создания учетной записи"' in response.text
        assert response.status_code == 400