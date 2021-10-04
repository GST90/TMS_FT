import requests
import json
from requests import Session
from requests.adapters import HTTPAdapter, Retry


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
        retry = Retry(
            total=5,
            status_forcelist=[404, 405, 500],
            backoff_factor=1)
        session = Session()
        session.mount('https://petstore.swagger.io/v2/pet', HTTPAdapter(max_retries=retry))
        data = {"id": id, "name": name,
                "Photo": photoUrls, "status": status,
                "type": role}
        response = requests.post(url, headers=self.headers, data=json.dumps(data))
        status = response.status_code
        code = 200
        assert status == code, f'not equal {code}'

    def check_pet(self, id):
        retry = Retry(
            total=5,
            status_forcelist=[404, 405, 500],
            backoff_factor=1)
        session = Session()
        session.mount('https://petstore.swagger.io/v2/pet', HTTPAdapter(max_retries=retry))
        url = self.url + '/' + str(id)
        response = session.get(url, headers=self.headers)
        status = response.status_code
        code = 200
        assert status == code, f'not equal {code}'

    def delete_pet(self, id):
        retry = Retry(
            total=5,
            status_forcelist=[404, 405, 500],
            backoff_factor=1)
        session = Session()
        session.mount('https://petstore.swagger.io/v2/pet', HTTPAdapter(max_retries=retry))
        url = self.url + '/' + str(id)
        response = session.delete(url, headers=self.headers)
        status = response.status_code
        code = 200
        assert status == code, f'not equal {code}'

    def check_pet_deleted(self, id):
        retry = Retry(
            total=5,
            status_forcelist=[200, 500],
            backoff_factor=1)
        session = Session()
        session.mount('https://petstore.swagger.io/v2/pet', HTTPAdapter(max_retries=retry))
        url = self.url + '/' + str(id)
        response = session.get(url, headers=self.headers)
        status = response.status_code
        code = 404
        assert status == code, f'not equal {code}'
        
