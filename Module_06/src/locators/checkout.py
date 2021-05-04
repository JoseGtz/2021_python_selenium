"""Checkout Info Locators"""
from selenium.webdriver.common.by import By


class CheckoutLoc:
    SUBTOTAL_LABEL = (By.CLASS_NAME, "summary_subtotal_label")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    CANCEL_BTN = (By.ID, 'cancel')
    FINISH_BTN = (By.ID, 'finish')
    TITLE_LABEL = (By.CLASS_NAME, 'title')

    SUCCESS_MSG = (By.CLASS_NAME, 'complete-header')
    SUCCESS_MSG_TWO = (By.CLASS_NAME, 'complete-text')