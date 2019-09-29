from urllib.parse import urlparse
import urllib
from .base_page import BasePage
from .locators import MainPageLocators


class BasketPage(BasePage):

    def guest_cant_see_product_in_basket_opened(self):
        language_list = ['/es/', '/fr/', '/ru/', '/en-gb/', '/it/']
        checked_list = ['vacío', 'vide', 'пуста', 'is empty', 'vuoto']

        href = self.browser.find_element(
            *MainPageLocators.BASKET).get_attribute('href')
        basket_msg= self.browser.find_element(
            *MainPageLocators.BASKET_CONTAINS).text
        language = urlparse(href).path
        assert checked_list[language_list.index(language)] in basket_msg, \
            "No message about empty basket!"
