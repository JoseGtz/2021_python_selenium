from Module_06.src.elements.base_page_element import BasePageElement
from Module_06.src.elements.cart_items import CartItems
from Module_06.src.locators.cart import CartLoc
from Module_06.src.pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from Module_06.src.elements.header import Header
from Module_06.src.pages.contact_info import ContactInfoPage

_URL = "https://www.saucedemo.com/cart.html"


class CartPage(BasePage):

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self.header = Header(self._wait)
        self.products = CartItems(CartLoc.CART_ITEMS, self._wait)
        self.__title = BasePageElement(CartLoc.TITLE, self._wait)
        self.__ctn_shopping = BasePageElement(CartLoc.CTN_SHOPPING, self._wait)
        self.__remove_button = BasePageElement(CartLoc.REMOVE_BUTTON, self._wait)
        self.__checkout_btn = BasePageElement(CartLoc.CHECKOUT_BTN, self._wait)

    def back_shopping(self):
        self.__ctn_shopping.click()

    def checkout(self):
        self.__checkout_btn.click()
        return ContactInfoPage(self._wait._driver, self._wait._timeout)

    def get_title(self) -> str:
        return self.__title.get_text()

    def remove_item(self):
        self.__remove_button.click()