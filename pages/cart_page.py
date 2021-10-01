from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators
from decimal import Decimal


class CartPage(BasePage):

    def check_title_appeared(self, goods_title):
        title = self.find_element(CartPageLocators.LOCATOR_GOODS_TITLE).text
        assert title == goods_title, f" title not equal {goods_title}"

    def check_price_appeared(self, num, total):
        price_for_unit = int(Decimal(self.find_element(CartPageLocators.LOCATOR_UNIT_PRICE).text.strip('$')))
        total_price = int(Decimal(self.find_element(CartPageLocators.LOCATOR_TOTAL_PRICE).text.strip('$')))
        assert total_price == total and price_for_unit * num, f"not equal {total_price}"

    def click_confirm_button(self):
        confirm_button = self.find_element(CartPageLocators.LOCATOR_CONFIRM_ORDER)
        confirm_button.click()
