import requests
import json


class Api:

    def __init__(self, id, name, role, photoUrls, status):
        self.url = "https://petstore.swagger.io/v2/pet"
        self.id = id
        self.name = name
        self.photoUrls = photoUrls
        self.role = role
        self.status = status
        self.headers = {'accept': 'application/json', 'content-type': 'application/json'}

    def add_pet(self, url, id, name, photoUrls, role, status):
        data = {"id": id, "name": name,
                "Photo": photoUrls, "status": status,
                "type": role}
        response = requests.post(url, headers=self.headers, data=json.dumps(data))
        status = response.status_code
        code = 200
        assert status == code, f'not equal {code}'

    def check_pet(self):
        url = self.url + '/' + str(self.id)
        response = requests.get(url, headers=self.headers)
        status = response.status_code
        code = 200
        assert status == code, f'not equal {code}'

    def delete_pet(self):
        url = self.url + '/' + str(self.id)
        response = requests.delete(url, headers=self.headers)
        status = response.status_code
        code = 200
        assert status == code, f'not equal {code}'

    def check_pet_deleted(self):
        url = self.url + '/' + str(self.id)
        response = requests.get(url, headers=self.headers)
        status = response.status_code
        code = 404
        assert status == code, f'not equal {code}'
