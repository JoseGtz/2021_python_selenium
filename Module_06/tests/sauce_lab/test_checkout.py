import pytest

from Module_06.src.pages.login import LoginPage
from Module_06.tests.common.test_base import TestBase

_DEF_USER = 'standard_user'
_DEF_PASSWORD = 'secret_sauce'
VALID_PRICES = ['$29.99', '$9.99', '$15.99', '$49.99', '$7.99', '$15.99']


class TestCheckout(TestBase):

    @pytest.mark.regression
    @pytest.mark.checkout
    def test_checkout_page(self):
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        for item in inventory.products:
            item.add_to_cart()
        cart_page = inventory.open_cart()
        contact_info_page = cart_page.checkout()
        contact_info_page.fill_info(firstname="Jose Luis", lastname="Gutierrez", postal_code="555555")
        checkout_page = contact_info_page.checkout()
        assert checkout_page.get_title_text() == 'CHECKOUT: OVERVIEW', 'Checkout page title should be CHECKOUT: OVERVIEW'

    @pytest.mark.regression
    @pytest.mark.checkout
    def test_checkout_cancel(self):
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        for item in inventory.products:
            item.add_to_cart()
        cart_page = inventory.open_cart()
        contact_info_page = cart_page.checkout()
        contact_info_page.fill_info(firstname="Jose Luis", lastname="Gutierrez", postal_code="555555")
        checkout_page = contact_info_page.checkout()
        checkout_page.cancel_buy()
        assert inventory.get_label() == 'PRODUCTS', 'Inventory page label should be Products'

    @pytest.mark.regression
    @pytest.mark.checkout
    def test_checkout_complete(self):
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        for item in inventory.products:
            item.add_to_cart()
        cart_page = inventory.open_cart()
        contact_info_page = cart_page.checkout()
        contact_info_page.fill_info(firstname="Jose Luis", lastname="Gutierrez", postal_code="555555")
        checkout_page = contact_info_page.checkout()
        checkout_page.finish_buy()
        assert checkout_page.get_success_msg() == 'THANK YOU FOR YOUR ORDER', 'Success page label should be THANK YOU FOR YOUR ORDER'