"""Test cases for login"""
from selenium.webdriver.support.wait import WebDriverWait
from common.webdriver_factory import get_driver
from Module_05.souce_func_lib.login import login


def test_valid_user():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'secret_sauce')


def test_invalid_user():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'invalid_sauce')