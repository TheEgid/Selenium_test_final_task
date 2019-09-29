from urllib.parse import urlparse
import urllib
from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):

    def guest_cant_see_product_in_basket_opened(self, _href):
        languages = ['/es/basket/', '/fr/basket/', '/ru/basket/',
                     '/en-gb/basket/', '/it/basket/']
        checks = ['vacío', 'vide', 'пуста', 'is empty', 'vuoto']
        basket_msg= self.browser.find_element(
            *BasePageLocators.BASKET_CONTAINS).text
        language = urlparse(_href).path
        # breakpoint()
        assert checks[languages.index(language)] in basket_msg, \
            "No message about empty basket!"
