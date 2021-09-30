from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators


class CartPage(BasePage):

    def check_title_appeared(self, goods_title):
        title = self.find_element(CartPageLocators.LOCATOR_GOODS_TITLE).text
        assert title == goods_title, f" title not equal {goods_title}"

    def check_price_appeared(self, goods_price):
        price = self.find_element(CartPageLocators.LOCATOR_TOTAL_PRICE).text
        assert price == goods_price, f" title not equal {goods_price}"

    def click_confirm_button(self):
        confirm_button = self.find_element(CartPageLocators.LOCATOR_CONFIRM_ORDER)
        confirm_button.click()
