from selenium import webdriver
import allure
import pytest
from helpers.database import DB


@pytest.fixture()
def browser():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--disable-gpu')
#     browser = webdriver.Chrome(chrome_options=chrome_options)
    browser = webdriver.Chrome("C:\chromedriver.exe")
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        try:
            if 'browser' in item.fixturenames:
                browser = item.funcargs['browser']
            else:
                print('Does not have browser fixture')
                return
            allure.attach(browser.get_screenshot_as_png(), "Screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f'Failed to make screenshot: {e}')


@pytest.fixture()
def db_client():
    db = DB()
    db.create_conn()
    yield db
    db.conn.close()
