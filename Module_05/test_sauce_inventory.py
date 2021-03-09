"""Test cases for Inventory"""
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from common.webdriver_factory import get_driver
from Module_05.souce_func_lib.inventory import get_inventory, InventoryItem
from Module_05.souce_func_lib.login import login


LOGIN_DATA = [
    ('standard_user', 'secret_sauce'),
    ('performance_glitch_user', 'secret_sauce'),
    ('problem_user', 'secret_sauce'),
]


@pytest.mark.parametrize('user, password', LOGIN_DATA)
def test_inventory_loaded(user, password):
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, user, password)
    items = get_inventory(wait)
    assert len(items) > 0, 'Inventory should be loaded'
    driver.close()


def test_inventory_size():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'secret_sauce')
    items = get_inventory(wait)
    assert len(items) == 6, 'Items size should be as expected'
    driver.close()


TITLE_DATA = [
    'Sauce Labs Backpack',
    'Sauce Labs Bike Light',
    'Sauce Labs Bolt T-Shirt',
    'Sauce Labs Fleece Jacket',
    'Sauce Labs Onesie',
    'Test.allTheThings() T-Shirt (Red)'
]


def test_inventory_catalog():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'secret_sauce')
    items = get_inventory(wait)
    for index, item in enumerate(items):
        item: InventoryItem
        assert item.title == TITLE_DATA[index]
    driver.close()
