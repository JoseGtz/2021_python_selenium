from selenium.webdriver.support.wait import WebDriverWait
from Module_06.src.elements.base_page_element import BasePageElement
from Module_06.src.locators.checkout import CheckoutLoc


class Checkout:
    def __init__(self, wait: WebDriverWait):
        self._wait = wait
        self._subtotal = BasePageElement(CheckoutLoc.SUBTOTAL_LABEL, wait=wait)
        self._total = BasePageElement(CheckoutLoc.TOTAL_LABEL, wait=wait)
        self._cancel_btn = BasePageElement(CheckoutLoc.CANCEL_BTN, wait=wait)
        self._finish_btn = BasePageElement(CheckoutLoc.FINISH_BTN, wait=wait)
        self._success_msg = BasePageElement(CheckoutLoc.SUCCESS_MSG, wait=wait)
        self._title = BasePageElement(CheckoutLoc.TITLE_LABEL, wait=wait)

    def cancel_checkout(self):
        self._cancel_btn.click()

    def finish(self):
        self._finish_btn.click()

    def get_subtotal(self) -> str:
        return self._subtotal.get_text()

    def get_total(self) -> str:
        return self._total.get_text()

    def get_success_msg(self) -> str:
        return self._success_msg.get_text()

    def get_title(self) -> str:
        return self._title.get_text()
