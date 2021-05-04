"""Element Contact Info"""
from selenium.webdriver.support.wait import WebDriverWait
from Module_06.src.elements.base_page_element import BasePageElement
from Module_06.src.locators.contact_info import ContactInfoLoc


class ContactInfo:
    """Represent Contact Info section"""

    def __init__(self, wait: WebDriverWait):
        self._wait = wait
        self._firstname = BasePageElement(ContactInfoLoc.FIRSTNAME, wait=wait)
        self._lastname = BasePageElement(ContactInfoLoc.LASTNAME, wait=wait)
        self._postal_code = BasePageElement(ContactInfoLoc.POSTAL_CODE, wait=wait)
        self._warning_msg = BasePageElement(ContactInfoLoc.WARNING_MSG, wait=wait)
        self._cancel_btn = BasePageElement(ContactInfoLoc.CANCEL_BTN, wait=wait)
        self._continue_btn = BasePageElement(ContactInfoLoc.CONTINUE_BTN, wait=wait)

    def fill_info(self, firstname="", lastname="", postal_code=""):
        self._firstname.write(firstname)
        self._lastname.write(lastname)
        self._postal_code.write(postal_code)

    def checkout(self):
        self._continue_btn.click()

    def back_to_cart(self):
        self._cancel_btn.click()

    def get_error_msg(self):
        return self._warning_msg.get_text()