from selenium.webdriver.common.by import By


class ChangeTabLocators:

    LOCATOR_CURRENCY_SELECTION = (By.XPATH, "//select[@name='currency_code']")
    LOCATOR_COUNTRY_SELECTION = (By.XPATH, "//select[@name='country_code']")
    LOCATOR_SAVE_BUTTON = (By.XPATH, "//button[@name='save']")
