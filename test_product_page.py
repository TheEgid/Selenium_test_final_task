import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


PRODUCT_BASE_LINK = f'http://selenium1py.pythonanywhere.com/catalogue'

urls = [
    f"{PRODUCT_BASE_LINK}/the-shellcoders-handbook_209/?promo=newYear",
    f"{PRODUCT_BASE_LINK}/coders-at-work_207/?promo=newYear2019",
    f"{PRODUCT_BASE_LINK}/coders-at-work_207/?promo=offer0",
    f"{PRODUCT_BASE_LINK}/coders-at-work_207/?promo=offer1",
    f"{PRODUCT_BASE_LINK}/coders-at-work_207/?promo=offer2",
    f"{PRODUCT_BASE_LINK}/coders-at-work_207/?promo=offer3",
    f"{PRODUCT_BASE_LINK}/coders-at-work_207/?promo=offer4",
    f"{PRODUCT_BASE_LINK}/coders-at-work_207/?promo=offer5",
    f"{PRODUCT_BASE_LINK}/coders-at-work_207/?promo=offer6",
    pytest.param(f"{PRODUCT_BASE_LINK}/coders-at-work_207/?promo=offer7",
                 marks=pytest.mark.xfail),
    f"{PRODUCT_BASE_LINK}/coders-at-work_207/?promo=offer8",
    f"{PRODUCT_BASE_LINK}/coders-at-work_207/?promo=offer9",
]


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    browser.implicitly_wait(1)
    page.should_be_add_product_to_basket()
    page.should_prices_equal()
    page.should_products_equal()
    browser.implicitly_wait(1)


@pytest.mark.xfail
@pytest.mark.parametrize('link', [f'{PRODUCT_BASE_LINK}/coders-at-work_207'])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    browser.implicitly_wait(1)
    page.guest_cant_see_success_message()


@pytest.mark.parametrize('link', [f'{PRODUCT_BASE_LINK}/coders-at-work_207'])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    browser.implicitly_wait(1)
    page.guest_cant_see_success_message()


@pytest.mark.parametrize('link', [f'{PRODUCT_BASE_LINK}/the-city-and-the-stars_95'])
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    browser.implicitly_wait(1)
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.parametrize('link', [f'{PRODUCT_BASE_LINK}/the-city-and-the-stars_95'])
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    browser.implicitly_wait(1)
    page.should_be_login_link()


@pytest.mark.xfail
@pytest.mark.parametrize('link', [f'{PRODUCT_BASE_LINK}/coders-at-work_207'])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    browser.implicitly_wait(1)
    page.message_disappeared()


@pytest.mark.parametrize('link', [f'{PRODUCT_BASE_LINK}/coders-at-work_207'])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    browser.implicitly_wait(1)
    next_page = BasketPage(browser, browser.current_url)
    next_page.guest_cant_see_product_in_basket_opened(_href=browser.current_url)

