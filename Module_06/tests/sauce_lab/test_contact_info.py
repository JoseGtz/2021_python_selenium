from Module_06.src.pages.login import LoginPage
from Module_06.tests.common.test_base import TestBase

_DEF_USER = 'standard_user'
_DEF_PASSWORD = 'secret_sauce'


class TestContactInfo(TestBase):

    def test_contact_info_incomplete_LastName(self):
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        for item in inventory.products:
            item.add_to_cart()
        cart_page = inventory.open_cart()
        contact_info_page = cart_page.checkout()
        contact_info_page.fill_info(firstname="Jose Luis")
        contact_info_page.checkout()
        assert contact_info_page.get_error_msg() == "Error: Last Name is required"

    def test_contact_info_incomplete_FirstName(self):
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        for item in inventory.products:
            item.add_to_cart()
        cart_page = inventory.open_cart()
        contact_info_page = cart_page.checkout()
        contact_info_page.fill_info(lastname="Gutierrez")
        contact_info_page.checkout()
        assert contact_info_page.get_error_msg() == "Error: First Name is required"

    def test_contact_info_incomplete_PostalCode(self):
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        for item in inventory.products:
            item.add_to_cart()
        cart_page = inventory.open_cart()
        contact_info_page = cart_page.checkout()
        contact_info_page.fill_info(firstname="Jose Luis", lastname="Gutierrez")
        contact_info_page.checkout()
        assert contact_info_page.get_error_msg() == "Error: Postal Code is required"

    def test_navigation_back(self):
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        for item in inventory.products:
            item.add_to_cart()
        cart_page = inventory.open_cart()
        contact_info_page = cart_page.checkout()
        contact_info_page.fill_info(firstname="Jose Luis", lastname="Gutierrez", postal_code="555555")
        contact_info_page.back_to_cart()
        assert cart_page.get_title() == 'YOUR CART', 'Cart page label should be "YOUR CART"'
