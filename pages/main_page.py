from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def clear_input_field(self):
        self.find_element(MainPageLocators.LOCATOR_QUANTITY).clear()

    def set_quantity(self, num: int):
        quantity_field = self.find_element(MainPageLocators.LOCATOR_QUANTITY)
        quantity_field.send_keys(num)

    def click_added_to_card_button(self):
        self.find_element(MainPageLocators.LOCATOR_ADD_TO_CART).click()

    def click_checkout_button(self):
        self.find_element(MainPageLocators.LOCATOR_CART_BUTTON).click()
