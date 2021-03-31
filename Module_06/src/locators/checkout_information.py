"""Locators for checkout details items"""
from selenium.webdriver.common.by import By


class CheckoutInformationLoc:
    """Checkout Information locators.
    Locators are relative to parent container div.
    """
    CANCEL = (By.XPATH, "//*[@class='checkout_buttons']/a[contains(@class,'cart_cancel_link btn_secondary')]")
    CONTINUE = (By.XPATH, "//*[@class='checkout_buttons']/a[contains(@class,'btn_primary cart_button')]")
