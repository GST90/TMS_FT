from pages.base_page import BasePage
from pages.change_tab import ChagesTab
import allure


@allure.feature('Check changes saved')
def test_check_changes_saved(browser):
    base_page = BasePage(browser)
    change_tab = ChagesTab(browser)
    curr = 'USD'
    state = 'Belarus'
    with allure.step('Open "litecart" page'):
        base_page.open_base_page()
    with allure.step('Open Chages Tab'):
        base_page.open_changes_tab()
    with allure.step(f'Select currency {curr}'):
        change_tab.select_currency(curr)
    with allure.step(f'Select country {state}'):
        change_tab.select_country(state)
    with allure.step('Click "Save" button'):
        change_tab.click_save_button()
    with allure.step(f'{curr} currency appearance'):
        base_page.check_currency_presents(curr)
    with allure.step(f'The {state} country appearance'):
        base_page.check_country_presents(state)
