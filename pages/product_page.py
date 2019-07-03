from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def should_be_added_to_cart(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        add_to_cart_message = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_MESSAGE)
        assert product_name.text == add_to_cart_message.text, "Wrong product added to cart"
