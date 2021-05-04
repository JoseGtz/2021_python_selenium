from Module_06.src.elements.contact_info import ContactInfo
from Module_06.src.pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from Module_06.src.elements.header import Header
from Module_06.src.pages.checkout import CheckoutPage

_URL = "https://www.saucedemo.com/checkout-step-one.html"


class ContactInfoPage(BasePage):

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self._contact_info = ContactInfo(self._wait)
        self.header = Header(self._wait)

    def fill_info(self, firstname="", lastname="", postal_code=""):
        self._contact_info.fill_info(firstname, lastname, postal_code)

    def checkout(self):
        self._contact_info.checkout()
        return CheckoutPage(self._wait._driver, self._wait._timeout)

    def back_to_cart(self):
        self._contact_info.back_to_cart()

    def get_error_msg(self):
        return self._contact_info.get_error_msg()
