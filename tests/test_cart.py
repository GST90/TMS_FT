from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.cart_page import CartPage
import allure
import time


@allure.feature('Check order confirmation')
def test_check_order_confirmed(browser, db_client):
    base_page = BasePage(browser)
    main_page = MainPage(browser)
    cart_page = CartPage(browser)
    user = "erebb@mail.ru"
    passwd = "1111"
    title = "Red Duck"
    price = "$60.00"
    with allure.step('Open page'):
        base_page.open_base_page()
    with allure.step('Set login keys'):
        base_page.fill_login_input(user)
    with allure.step('Set passwd keys'):
        base_page.fill_password_input(passwd)
    with allure.step('Click login button'):
        base_page.click_login_button()
    with allure.step('Select duck'):
        base_page.select_goods_red_duck()
    with allure.step('Clean the input field'):
        main_page.clear_input_field()
    with allure.step('Set quantity'):
        main_page.set_quantity(3)
    with allure.step('Click "Add to cart" button'):
        main_page.click_added_to_card_button()
        time.sleep(3)
    with allure.step('Click "Checkout" button'):
        main_page.click_checkout_button()
    with allure.step(f'Check goods title {title} appeared'):
        cart_page.check_title_appeared(title)
    with allure.step(f'Check total price {price} appeared'):
        cart_page.check_price_appeared(3)
    with allure.step('Click the "Confirm order" button'):
        cart_page.click_confirm_button()
    with allure.step('Check order added in database'):
        db_client.check_order(title)
