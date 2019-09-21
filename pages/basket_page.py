from .base_page import BasePage
from .locators import MainPageLocators


class BasketPage(BasePage):

    def guest_cant_see_product_in_basket_opened(self):
        basket_contains = self.browser.find_element(
            *MainPageLocators.BASKET_CONTAINS)
        checked_list = ['vacío', 'vide', 'пуста', 'is empty']
        matching = [(check not in basket_contains.text) for check in checked_list]
        breakpoint()
        assert any(matching), "No message about empty basket!"


    #     assert self.is_not_element_present(
    #         *ProductPageLocators.SUCCESS_MESSAGE), \
    #         "Success message is presented, but should not be"