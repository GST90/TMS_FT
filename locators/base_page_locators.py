from selenium.webdriver.common.by import By


class BasePageLocators:

    LOCATOR_OPEN_CHANGES = (By.CLASS_NAME, 'fancybox-region')
    LOCATOR_CURRENCY_APPEARANCE = (By.XPATH, '//*[@id="region"]/div[2]')
    LOCATOR_COUNTRY_APPEARANCE = (By.XPATH, '//*[@id="region"]/div[3]')
    LOCATOR_LOGIN = (By.XPATH, '//input[@name="email"]')
    LOCATOR_PASSWORD = (By.XPATH, '//input[@name="password"]')
    LOCATOR_LOGIN_BUTTON = (By.XPATH, '//button[@name="login"]')
    LOCATOR_GOODS = (By.XPATH, '//div[@class="name" and text()="Red Duck"]')
