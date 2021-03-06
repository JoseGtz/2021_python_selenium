"""Implements checkout details loc."""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from Module_06.src.elements.base_page_element import BasePageElement
from Module_06.src.elements.header import Header
from Module_06.src.locators.checkout_details import CheckoutDetailsLoc
from Module_06.src.mixin.InventoryItemMixin import InventoryItemMixin
from Module_06.src.pages.base_page import BasePage

_URL = 'https://www.saucedemo.com/cart.html'


class CheckoutDetailsPage(InventoryItemMixin, BasePage):
    """Implements inventory item details"""

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self._back_btn = BasePageElement(CheckoutDetailsLoc.BACK_BTN, wait=self._wait)
        self._checkout_btn = BasePageElement(CheckoutDetailsLoc.CHECKOUT_BTN, wait=self._wait)
        self._remove_btn = BasePageElement(CheckoutDetailsLoc.REMOVE_BTN, wait=self._wait)
        self.header = Header(self._wait)

    def continue_shopping(self):
        """Go back to details page."""
        self._back_btn.click()

    def checkout_btn(self):
        """Go to Checkout page."""
        self._checkout_btn.click()

    def remove_item_checkout(self):
        """Go back to details page."""
        self._remove_btn.click()
