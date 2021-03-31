"""Implements checkout details loc."""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from Module_06.src.elements.base_page_element import BasePageElement
from Module_06.src.elements.header import Header
from Module_06.src.locators.checkout_information import CheckoutInformationLoc
from Module_06.src.mixin.InventoryItemMixin import InventoryItemMixin
from Module_06.src.pages.base_page import BasePage

_URL = 'https://www.saucedemo.com/checkout-step-one.html'


class CheckoutInformationPage(InventoryItemMixin, BasePage):
    """Implements inventory item details"""

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self._cancel_btn = BasePageElement(CheckoutInformationLoc.CANCEL, wait=self._wait)
        self._continue_btn = BasePageElement(CheckoutInformationLoc.CONTINUE, wait=self._wait)
        self.header = Header(self._wait)

    def cancel_checkout(self):
        """Go back to details page."""
        self._cancel_btn.click()

    def continue_checkout(self):
        """Go to Checkout page."""
        self._continue_btn.click()
