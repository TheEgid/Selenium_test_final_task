import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pytest

# from pages.login_page import LoginPage
# from pages.main_page import MainPage
from pages.product_page import ProductPage


product_base_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


@pytest.fixture
def link():
    yield product_base_link
    #yield 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    browser.implicitly_wait(5)
    page.solve_quiz_and_get_code()
    page.should_be_add_product_to_basket()
    page.should_prices_equal()
    page.should_products_equal()
    browser.implicitly_wait(5)







