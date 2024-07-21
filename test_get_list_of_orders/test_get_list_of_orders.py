import pytest
import allure
import requests
from constants import Constants
from conftest import create_order_with_different_values_metroStation
from helpers.helpers import Helpers


class TestGetListOfOrders:
    @allure.title('Позитивная проверка получения списка заказов')
    @allure.description('Создаем 2 заказа с указанием станций "3333" и "4444", система должна вернуть все заказы, связанные с этими станциями')
    @pytest.mark.usefixtures('create_order_with_different_values_metroStation')
    def test_get_list_of_orders_success(self, create_order_with_different_values_metroStation):
        response = requests.get(Constants.URL + 'api/v1/orders?nearestStation=["3333", "4444"]')
        print(f"Список заказов: {response.text}")
        self.track = create_order_with_different_values_metroStation

    @allure.issue('https://spykontishek.youtrack.cloud/issue/7M-170/Oshibka-400-Bad-Request-pri-otmene-zakaza-na-ruchku-api-v1-orders-cancel','7M-170')
    def teardown_method(self):
        helper = Helpers()
        helper.cancel_order(self.track)






