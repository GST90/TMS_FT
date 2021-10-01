from selenium.webdriver.common.by import By


class CartPageLocators:
    LOCATOR_GOODS_TITLE = (By.XPATH, '//strong[text()="Red Duck"]')
    LOCATOR_UNIT_PRICE = (By.XPATH, '//tbody//td[@class="unit-cost"]')
    LOCATOR_TOTAL_PRICE = (By.XPATH, '(//tr[@class="footer"]//strong)[2]')
    LOCATOR_CONFIRM_ORDER = (By.XPATH, '//button[@name="confirm_order"]')
