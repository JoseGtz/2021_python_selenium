"""Abstraction to interact with inventory details."""
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from Module_06.src.elements.base_page_element import BasePageElement
from Module_06.src.locators.inventory_details import InventoryDetailsLoc


class InventoryDetailsItem:
    """Represents inventory item."""

    __ADDED_LABEL = 'ADD TO CART'
    __REMOVE_LABEL = 'REMOVE'

    def __init__(self, wait: WebDriverWait, root: WebElement):
        self.__title = BasePageElement(InventoryDetailsLoc.TITLE, wait=wait, root=root)
        self.__description = BasePageElement(InventoryDetailsLoc.DESCRIPTION, wait=wait, root=root)
        self.__price = BasePageElement(InventoryDetailsLoc.PRICE, wait=wait, root=root)
        self.__inv_btn = BasePageElement(InventoryDetailsLoc.BTN, wait=wait, root=root)

    def get_title(self) -> str:
        """Get title for item."""
        return self.__title.get_text()

    def get_description(self) -> str:
        """Get description."""
        return self.__description.get_text()

    def get_price(self) -> str:
        """Get price."""
        return self.__price.get_text()

    def is_in_the_cart(self) -> str:
        """Get item status"""
        return self.__inv_btn.get_text() == InventoryDetailsItem.__REMOVE_LABEL

    def add_to_cart(self):
        """Add to cart."""
        if self.__inv_btn.get_text() == InventoryDetailsItem.__ADDED_LABEL:
            self.__inv_btn.click()
        else:
            raise ValueError(f'Inventory item is already in the cart')

    def remove_from_cart(self):
        """Remove from cart."""
        if self.__inv_btn.get_text() == InventoryDetailsItem.__REMOVE_LABEL:
            self.__inv_btn.click()
        else:
            raise ValueError(f'Inventory item is not in the cart')
