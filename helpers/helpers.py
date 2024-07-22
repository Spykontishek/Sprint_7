import requests
import json
from constants import Constants

class Helpers:
    def __init__(self):
        self.id = None
    def login(self, login, password):
        payload = {
        "login": login,
        "password": password
        }
        payload_string = json.dumps(payload)
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+Constants.AUTH_PATH, data=payload_string, headers=headers)
        r = response.json()
        self.id = r['id']

    def delete_courier(self, id):
        self.id = id
        requests.delete(Constants.URL+Constants.DEL_PATH.format(self.id))

    def cancel_order(self, track):
        self.track = track
        payload = {
            "track": self.track
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        requests.put(Constants.URL+Constants.CANCEL_PATH, data=payload_string, headers=headers)


