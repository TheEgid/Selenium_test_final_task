import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    #browser = webdriver.Chrome()
    browser = webdriver.Chrome(r'C:\\chromedriver\chromedriver.exe')
    yield browser
    print("\nquit browser..")
    time.sleep(2)
    browser.quit()


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



