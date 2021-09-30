from pages.base_page import BasePage
from locators.change_tab_locators import ChangeTabLocators
from selenium.webdriver.support.ui import Select


class ChagesTab(BasePage):

    def select_currency(self, currency):
        select = Select(self.find_element(ChangeTabLocators.LOCATOR_CURRENCY_SELECTION))
        select.select_by_value(currency)

    def select_country(self, country):
        select = Select(self.find_element(ChangeTabLocators.LOCATOR_COUNTRY_SELECTION))
        select.select_by_visible_text(country)

    def click_save_button(self):
        save_button = self.find_element(ChangeTabLocators.LOCATOR_SAVE_BUTTON)
        save_button.click()
