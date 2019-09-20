import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pytest

# from pages.login_page import LoginPage
# from pages.main_page import MainPage
from pages.product_page import ProductPage


PRODUCT_BASE_LINK = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'


# @pytest.yield_fixture
# def link():
#yield 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


urls = [
    f"{PRODUCT_BASE_LINK}/?promo=offer0", f"{PRODUCT_BASE_LINK}/?promo=offer1",
    f"{PRODUCT_BASE_LINK}/?promo=offer2", f"{PRODUCT_BASE_LINK}/?promo=offer3",
    f"{PRODUCT_BASE_LINK}/?promo=offer4", f"{PRODUCT_BASE_LINK}/?promo=offer5",
    f"{PRODUCT_BASE_LINK}/?promo=offer6",
    pytest.param(f"{PRODUCT_BASE_LINK}/?promo=offer7",
                 marks=pytest.mark.xfail),
    f"{PRODUCT_BASE_LINK}/?promo=offer8", f"{PRODUCT_BASE_LINK}/?promo=offer9"
]


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()

    browser.implicitly_wait(3)
    page.solve_quiz_and_get_code()
    # time.sleep(30)
    browser.implicitly_wait(3)

    page.should_be_add_product_to_basket()
    page.should_prices_equal()
    page.should_products_equal()
    browser.implicitly_wait(3)

    # time.sleep(15)


