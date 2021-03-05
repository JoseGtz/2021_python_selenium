"""Test cases for Inventory"""
from selenium.webdriver.support.wait import WebDriverWait
from common.webdriver_factory import get_driver
from Module_05.souce_func_lib.inventory import get_inventory, InventoryItem
from Module_05.souce_func_lib.login import login


def test_inventory():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'secret_sauce')
    items = get_inventory(wait)
    assert len(items) > 0, 'Inventory should be loaded'
