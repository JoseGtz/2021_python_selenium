from selenium.webdriver.support.wait import WebDriverWait
from Module_06.src.elements.cart_item import CartInventoryItem
from selenium.webdriver.support import expected_conditions as EC


class CartItems:
    """Represents any input text element."""

    def __init__(self, loc: tuple, wait: WebDriverWait = None):
        self._wait = wait
        self._loc = loc
        self.__elements = []

    def reload(self):
        """Force reload of inventory items. fro interaction between pages and have the list of products updated"""
        self.__elements.clear()
        elements = self._wait.until(EC.visibility_of_all_elements_located(self._loc))
        for element in elements:
            inv_item = CartInventoryItem(self._wait, element)
            self.__elements.append(inv_item)

    def __getitem__(self, key):
        if not self.__elements:
            self.reload()
        return self.__elements[key]

    def __iter__(self):
        self.reload()
        return iter(self.__elements)

    def __len__(self):
        return len(self.__elements)