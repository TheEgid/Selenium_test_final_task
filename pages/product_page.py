import time
import pytest
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        btn_add_to_basket = \
            self.browser.find_element(
                *ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()

    def should_be_add_product_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME), "No product name"
        assert self.is_element_present(
            *ProductPageLocators.MSG_ADD_TO_BASKET), \
            "No msg about product add to basket"

    def should_prices_equal(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.browser.find_element(
            *ProductPageLocators.BASKET_PRODUCT_PRICE)
        assert basket_price.text == product_price.text, \
            "Product_price and basket_price are not equal"

    def should_products_equal(self):
        basket_product = self.browser.find_element(
            *ProductPageLocators.MSG_ADD_TO_BASKET)
        product = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME)
        assert product.text == basket_product.text, \
            "Product and basket_product are not equal"

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def message_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

