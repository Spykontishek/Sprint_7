import pytest
import requests
import allure
import json
from constants import Constants
from faker import Faker

from helpers.helpers import Helpers

faker = Faker()

class TestCreateCourier():
    login = faker.user_name()[:5]
    password = faker.password()[:4]

    @allure.title('Позитивная проверка создания курьера с заполнением всех обязательных полей')
    @allure.description('Запрос должен вернуть правильный код и тело ответа')
    def test_creating_сourier_with_all_required_fields_success(self):
        firstName = faker.first_name()[:5]

        payload = {
            "login": self.login,
            "password": self.password,
            "firstName": firstName
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+Constants.REG_PATH, data=payload_string, headers=headers)
        assert response.json() == {'ok': True}
        assert response.status_code == 201

    def teardown_method(self):
        helper = Helpers()
        helper.login(self.login, self.password)
        self.id = helper.id
        helper.delete_courier(self.id)














