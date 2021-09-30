from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "http://localhost/en/"

    def open_base_page(self):
        self.driver.get(self.url)

    def find_element(self, locator: tuple, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def open_changes_tab(self):
        changes_button = self.find_element(BasePageLocators.LOCATOR_OPEN_CHANGES)
        changes_button.click()

    def check_currency_presents(self, currency):
        text = self.find_element(BasePageLocators.LOCATOR_CURRENCY_APPEARANCE).text
        assert text == currency, f'is not equal {currency}'

    def check_country_presents(self, country):
        text = self.find_element(BasePageLocators.LOCATOR_COUNTRY_APPEARANCE).text
        assert text == country, f'is not equal {country}'

    def fill_login_input(self, username):
        login_input = self.find_element(BasePageLocators.LOCATOR_LOGIN)
        login_input.send_keys(username)

    def fill_password_input(self, password):
        login_input = self.find_element(BasePageLocators.LOCATOR_PASSWORD)
        login_input.send_keys(password)

    def click_login_button(self):
        login_input = self.find_element(BasePageLocators.LOCATOR_LOGIN_BUTTON)
        login_input.click()

    def select_goods_red_duck(self):
        save_button = self.find_element(BasePageLocators.LOCATOR_GOODS)
        save_button.click()
