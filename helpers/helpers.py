import requests
import json
from constants import Constants

class Helpers:
    def login(self, login, password):
        payload = {
        "login": login,
        "password": password
        }
        payload_string = json.dumps(payload)
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+'/api/v1/courier/login', data=payload_string, headers=headers)
        r = response.json()
        print(f"Авторизация курьера: {response.text}")
        self.id = r['id']

    def delete_courier(self, id):
        self.id = id
        response = requests.delete(Constants.URL+'/api/v1/courier/{}'.format(self.id))
        print(f"удаление курьера: {response.text}")

    def cancel_order(self, track):
        self.track = track
        payload = {
            "track": self.track
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.put(Constants.URL+'/api/v1/orders/cancel', data=payload_string, headers=headers)
        print(f"Отмена заказа: {response.text}")

