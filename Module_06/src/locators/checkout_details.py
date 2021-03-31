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
    REMOVED_ITEM = (By.CLASS_NAME, 'removed_cart_item')
    BACK_BTN = (By.XPATH, "//*[@class='cart_footer']/a[contains(@class,'btn_secondary')]")
    CHECKOUT_BTN = (By.XPATH, "//*[@class='cart_footer']/a[contains(@class,'btn_action checkout_button')]")
    REMOVE_BTN = (By.XPATH, "//button[contains(@class,'btn_secondary cart_button')]")
