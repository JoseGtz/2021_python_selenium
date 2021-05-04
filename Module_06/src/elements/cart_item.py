from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from Module_06.src.elements.base_page_element import BasePageElement
from Module_06.src.locators.cart_items import CartItemLoc
from Module_06.src.mixin.InventoryItemMixin import InventoryItemMixin


class CartInventoryItem(InventoryItemMixin):
    def __init__(self, wait: WebDriverWait, root: WebElement):
        self._wait = wait
        self._title = BasePageElement(CartItemLoc.TITLE, wait=wait, root=root)
        self._description = BasePageElement(CartItemLoc.DESCRIPTION, wait=wait, root=root)
        self._price = BasePageElement(CartItemLoc.PRICE, wait=wait, root=root)
        self._inv_btn = BasePageElement(CartItemLoc.BTN, wait=wait, root=root)