import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pytest

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



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    time.sleep(2)  # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()