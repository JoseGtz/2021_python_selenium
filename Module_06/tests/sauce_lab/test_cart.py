from Module_06.src.pages.login import LoginPage
from Module_06.tests.common.test_base import TestBase

_DEF_USER = 'standard_user'
_DEF_PASSWORD = 'secret_sauce'


class TestCart(TestBase):

    def test_cart(self):
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        cart_page = inventory.open_cart()
        assert cart_page.get_title() == 'YOUR CART', 'Cart page label should be "YOUR CART"'
        cart_page.back_shopping()
        assert inventory.get_label() == 'PRODUCTS', 'Inventory page label should be Products'

    def test_added_items(self):
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        for item in inventory_page.products:
            item.add_to_cart()
        cart_page = inventory_page.open_cart()
        for item in cart_page.products:
            item.remove_from_cart()
