from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BTN_OPEN_BASKET = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
    BASKET_CONTAINS = (By.XPATH, '//*[@id="content_inner"]/p')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    EMAIL = (By.ID, "id_registration-email")
    PASSWORD1 = (By.ID, "id_registration-password1")
    PASSWORD2 = (By.ID, "id_registration-password2")
    BTN_REGISTER = (By.CSS_SELECTOR, "#register_form > button")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    MSG_ADD_TO_BASKET = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BASKET_PRODUCT = (By.CSS_SELECTOR, 'h3 > a')
    BASKET_PRODUCT_PRICE = (By.XPATH, '// *[ @ id = "messages"] / div[3] / div / p[1] / strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success")



