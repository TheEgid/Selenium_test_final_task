import pytest
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


PRODUCT_BASE_LINK = f'http://selenium1py.pythonanywhere.com/catalogue'


@pytest.fixture
def link():
    yield 'http://selenium1py.pythonanywhere.com/'


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    browser.implicitly_wait(1)
    next_page = BasketPage(browser, browser.current_url)
    next_page.guest_cant_see_product_in_basket_opened(_href=browser.current_url)


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        browser.implicitly_wait(1)
        next_page = LoginPage(browser, browser.current_url)
        next_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()



