import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера
    # и url адрес
    page.open()                        # открываем страницу
    page.go_to_login_page()            # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.new  # pytest -s -m "new" test_main_page.py
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    # Гость открывает главную страницу
    page = MainPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url, 0)
    # Ожидаем, что в корзине нет товаров
    basket_page.checking_that_the_basket_is_empty()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.checking_that_the_basket_is_empty_success_message()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url, 0)
    # Ожидаем, что в корзине нет товаров
    basket_page.checking_that_the_basket_is_empty()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.checking_that_the_basket_is_empty_success_message()
