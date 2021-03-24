"""Abstraction to interact with cart inventory item."""
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from Module_06.src.elements.base_page_element import BasePageElement
from Module_06.src.mixin.InventoryItemMixin import InventoryItemMixin
from Module_06.src.locators.checkout_details import CheckoutDetailsLoc


class RowInventoryItem(InventoryItemMixin):
    """Represents inventory item."""

    def __init__(self, wait: WebDriverWait, root: WebElement):
        self.__quantity = BasePageElement(CheckoutDetailsLoc.QUANTITY, wait=wait, root=root)
        self.__title = BasePageElement(CheckoutDetailsLoc.TITLE, wait=wait, root=root)
        self.__description = BasePageElement(CheckoutDetailsLoc.DESCRIPTION, wait=wait, root=root)
        self.__price = BasePageElement(CheckoutDetailsLoc.PRICE, wait=wait, root=root)
        self.__inv_btn = BasePageElement(CheckoutDetailsLoc.BTN, wait=wait, root=root)

    def get_quantity(self) -> int:
        """Get title for item."""
        return self.__quantity.get_text()
