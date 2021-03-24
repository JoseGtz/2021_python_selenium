"""Implements checkout details loc."""
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

    def __init__(self, wait: WebDriverWait, root: WebElement):
        self._wait = wait
        self.__back_btn = BasePageElement(CheckoutDetailsLoc.BACK_BTN, wait=wait, root=root)
        self.__checkout_btn = BasePageElement(CheckoutDetailsLoc.CHECKOUT_BTN, wait=wait, root=root)
        self.header = Header(self._wait)

    def continue_shopping(self):
        """Go back to details page."""
        self._back_btn.click()

    def checkout_btn(self):
        """Go to Checkout page."""
        self._checkout_btn.click()
