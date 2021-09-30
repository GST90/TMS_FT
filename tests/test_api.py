import random
from helpers.api_swagger import Api
import allure
from time import sleep


@allure.feature('API-swagger test')
def test_add_pet():
    id = random.randint(2425, 2426)
    name = "Oondasta"
    role = "Hunting pet"
    photoUrls = "http://missset.com/models/dinosaurs/t-rex-in-zbrush/"
    status = "available"
    with allure.step(f'Add pet to the store with id {id},'
                     f'name {name}'):
        api_page = Api(id=id, name=name, role=role, photoUrls=photoUrls, status=status)
        api_page.add_pet(api_page.url, api_page.id,
                         api_page.name, api_page.photoUrls,
                         api_page.role, api_page.status)
        sleep(1)
    with allure.step('Check pet in the store'):
        api_page.check_pet()
    with allure.step('Delete pet from the store'):
        api_page.delete_pet()
    with allure.step('Check pet in the store is deleted'):
        api_page.check_pet_deleted()
