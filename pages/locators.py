from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")

    MSG_ADD_TO_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(1)")

    #ALERT_ADDED_TO_CART = (By.CSS_SELECTOR, "div.alertinner")
    # ALERT_CART_STATUS = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")
    # ALERT_ADDED_TO_CART = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_NAME = (By.TAG_NAME, "h1")

    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, ".basket-mini")

    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color:nth-child(2)")


