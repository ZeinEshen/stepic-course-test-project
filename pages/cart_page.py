from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):
    def should_be_empty_cart_message(self):
        message = self.browser.find_element(*CartPageLocators.EMPTY_CART_MESSAGE)
        assert "Ваша корзина пуста" in message.text or "Your basket is empty" in message.text,\
            "Messages that the cart is empty is not present"

    def should_be_empty_cart(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEM), "Cart is not empty"
