from urllib.parse import urlparse
from .base_page import BasePage
from .locators import BasePageLocators
from .locators import ProductPageLocators


class BasketPage(BasePage):

    def guest_cant_see_product_in_basket_opened(self, _href):
        language_hrefs = ['/es/basket/', '/fr/basket/', '/ru/basket/',
                     '/en-gb/basket/', '/it/basket/']
        checks = ['vacío', 'vide', 'пуста', 'is empty', 'vuoto']
        basket_msg = self.browser.find_element(
            *BasePageLocators.BASKET_CONTAINS).text
        language_href = urlparse(_href).path
        assert checks[language_hrefs.index(language_href)] in basket_msg, \
            "No message about empty basket!"
        assert self.is_not_element_present(*ProductPageLocators.BASKET_PRODUCT), \
            "Should not be product in basket!"
