"""Contact Info Locators"""
from selenium.webdriver.common.by import By


class ContactInfoLoc:
    FIRSTNAME = (By.ID, 'first-name')
    LASTNAME = (By.ID, 'last-name')
    POSTAL_CODE = (By.ID, 'postal-code')
    WARNING_MSG = (By.XPATH, "//*[@class='error-message-container error']/h3")
    CANCEL_BTN = (By.ID, 'cancel')
    CONTINUE_BTN = (By.ID, 'continue')