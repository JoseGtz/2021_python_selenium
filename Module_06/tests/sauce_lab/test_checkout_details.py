"""Test cases for inventory item"""
from Module_06.src.elements.inventory_item import InventoryItem
from Module_06.src.elements.header import Header
from Module_06.src.pages.login import LoginPage
from Module_06.tests.common.test_base import TestBase
from Module_06.src.elements.row_inventory_item import RowInventoryItem
from Module_06.src.pages.checkout_details import CheckoutDetailsPage

_DEF_USER = 'standard_user'
_DEF_PASSWORD = 'secret_sauce'


class TestCheckoutDetails(TestBase):

    def test_checkout_details(self):
        """Test inventory prices"""
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        first_item.add_to_cart()
        first_item: Header
        checkout_item = first_item.goto_cart()
        checkout_item: RowInventoryItem
        print(f'Quantity: {checkout_item.get_quantity()}')
        print(f'Title: {checkout_item.get_title()}')
        print(f'Description: {checkout_item.get_description()}')
        print(f'Price: {checkout_item.get_price()}')
        assert len(checkout_item.get_quantity) == 1, 'Only one inventory item is displayed'
