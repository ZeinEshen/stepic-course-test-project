from selenium.webdriver.common.by import By


class MainPageLocators(object):
    CART_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators(object):
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ADD_TO_CART_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")


class CartPageLocators(object):
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "[id='content_inner'] p")
    CART_ITEM = (By.ID, "basket-items")
