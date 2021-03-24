"""Locators for checkout details items"""
from selenium.webdriver.common.by import By


class CheckoutDetailsLoc:
    """Checkout Details locators.
    Locators are relative to parent container div.
    """
    QUANTITY = (By.CLASS_NAME, 'cart_quantity')
    TITLE = (By.CLASS_NAME, 'inventory_item_name')
    DESCRIPTION = (By.CLASS_NAME, 'inventory_item_desc')
    PRICE = (By.CLASS_NAME, 'inventory_item_price')
    BTN = (By.XPATH, "//button[contains(@class,'btn_secondary cart_button')]")
    BACK_BTN = (By.CLASS_NAME, 'btn_secondary')
    CHECKOUT_BTN = (By.CLASS_NAME, 'btn_action checkout_button')
