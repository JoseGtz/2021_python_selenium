"""Test cases for inventory item"""
from Module_06.src.elements.inventory_item import InventoryItem
from Module_06.src.pages.login import LoginPage
from Module_06.tests.common.test_base import TestBase
from Module_06.src.pages.checkout_details import CheckoutDetailsPage
from Module_06.src.pages.checkout_information import CheckoutInformationPage

_DEF_USER = 'standard_user'
_DEF_PASSWORD = 'secret_sauce'


class TestCheckoutDetails(TestBase):

    def test_checkout_details(self):
        """Test inventory prices"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory.products[0]
        first_item: InventoryItem
        first_item.add_to_cart()
        inventory.header.goto_cart()
        checkout_item = CheckoutDetailsPage(self.driver, 5)
        checkout_item.continue_shopping()
        inventory.products.reload()
        print(f'Total elements in cart: {inventory.header.get_total_cart_items()}')

    def test_checkout_information(self):
        """Test inventory prices"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory.products[0]
        first_item: InventoryItem
        first_item.add_to_cart()
        inventory.header.goto_cart()
        checkout_item = CheckoutDetailsPage(self.driver, 5)
        checkout_item.checkout_btn()
        checkout_page = CheckoutInformationPage(self.driver, 5)
        checkout_page.cancel_checkout()
        print("Checkout Canceled")

    def test_checkout_remove(self):
        """Test inventory prices"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory.products[0]
        first_item: InventoryItem
        first_item.add_to_cart()
        inventory.header.goto_cart()
        checkout_item = CheckoutDetailsPage(self.driver, 5)
        checkout_item.remove_item_checkout()
        print("Checkout Canceled")
