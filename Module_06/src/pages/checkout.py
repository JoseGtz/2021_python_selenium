from Module_06.src.elements.cart_items import CartItems
from Module_06.src.elements.checkout import Checkout
from Module_06.src.pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from Module_06.src.elements.header import Header

_URL = "https://www.saucedemo.com/checkout-step-two.html"


class CheckoutPage(BasePage):
    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self.header = Header(self._wait)
        self.checkout = Checkout(self._wait)
        self.items = CartItems(self._wait)

    def cancel_buy(self):
        self.checkout.cancel_checkout()

    def finish_buy(self):
        self.checkout.finish()

    def get_subtotal_text(self) -> str:
        return self.checkout.get_subtotal()

    def get_total_text(self) -> str:
        return self.checkout.get_total()

    def get_title_text(self) -> str:
        return self.checkout.get_title()

    def get_success_msg(self) -> str:
        return self.checkout.get_success_msg()
