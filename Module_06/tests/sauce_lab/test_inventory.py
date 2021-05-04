"""Test cases for inventory item"""
from Module_06.src.elements.inventory_item import InventoryItem
from Module_06.src.pages.inventory import InventorySortOptions
from Module_06.src.pages.login import LoginPage
from Module_06.tests.common.test_base import TestBase

_DEF_USER = 'standard_user'
_DEF_PASSWORD = 'secret_sauce'
VALID_PRICES = ['$29.99', '$9.99', '$15.99', '$49.99', '$7.99', '$15.99']
TITLE_DATA = [
    'Sauce Labs Backpack',
    'Sauce Labs Bike Light',
    'Sauce Labs Bolt T-Shirt',
    'Sauce Labs Fleece Jacket',
    'Sauce Labs Onesie',
    'Test.allTheThings() T-Shirt (Red)'
]


class TestInventory(TestBase):

    def test_prices(self):
        """Test inventory prices"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        for index, item in enumerate(inventory.products):
            item: InventoryItem
            assert item.get_price() == VALID_PRICES[index], f'Price for item {index} should be {VALID_PRICES[index]}'
            print('\n')
            print(item.get_title())
            print(item.get_description())
            print(item.get_price())
            print('*' * 80)

    def test_items_name(self):
        """Test inventory names"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        for index, item in enumerate(inventory.products):
            item: InventoryItem
            assert item.get_title() == TITLE_DATA[index], f'Title for item {index} should be {TITLE_DATA[index]}'
            print('\n')

    def test_label(self):
        """Test production label."""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        assert inventory.get_label() == 'Products', 'Inventory page label should be Products'

    def test_sort(self):
        """Test sort products"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        inventory.get_sort_value() == InventorySortOptions.A_TO_Z.value, 'Default sort should be A to Z'
        for option in InventorySortOptions:
            inventory.sort_by(option)
            inventory.get_sort_value() == option.value, f'Default sort should be {option.value}'

    def test_add_remove(self):
        """This is to test items functionality on catalog"""
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        for item in inventory_page.products:
            item.add_to_cart()
            item.remove_from_cart()
