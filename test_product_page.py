from pages.base_page import generate_temp_password
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(self, browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    # page.solve_quiz_and_get_code()
    page.checking_added_to_basket_product_name(page.return_product_name())
    page.checking_added_to_basket_product_price(page.return_product_price())


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.success_message_should_be_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url, 0)
    basket_page.checking_that_the_basket_is_empty()
    basket_page.checking_that_the_basket_is_empty_success_message()


@pytest.mark.login
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = generate_temp_password(10)
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        # page.solve_quiz_and_get_code()
        page.checking_added_to_basket_product_name(page.return_product_name())
        page.checking_added_to_basket_product_price(page.return_product_price())
