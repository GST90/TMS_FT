from selenium.webdriver.common.by import By


class MainPageLocators:
    GOODS_PRICE = (By.XPATH, '//span[@class="price"]')
    LOCATOR_QUANTITY = (By.XPATH, '//input[@name="quantity"]')
    LOCATOR_ADD_TO_CART = (By.XPATH, '//*[@name="add_cart_product"]')
    LOCATOR_CART_BUTTON = (By.XPATH, '//*[@id="cart"]/a[3]')
