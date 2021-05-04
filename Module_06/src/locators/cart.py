"""Locators for inventory details items"""
from selenium.webdriver.common.by import By


class CartLoc:
    """Cart item locators.
    Locators are relative to parent container div.
    """
    TITLE = (By.CLASS_NAME, "title")
    CTN_SHOPPING = (By.ID , "continue-shopping")
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BTN = (By.ID, "checkout")