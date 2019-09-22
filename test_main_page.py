import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture
def link():
    yield 'http://selenium1py.pythonanywhere.com/'


def test_guest_can_go_to_login_page(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    page = MainPage(browser, link)
    page.open()


