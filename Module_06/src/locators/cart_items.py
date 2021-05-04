from selenium.webdriver.common.by import By


class CartItemLoc:
    """Inventory item locators.
    Locators are relative to parent container div.
    """
    TITLE = (By.CLASS_NAME, 'inventory_item_name')
    DESCRIPTION = (By.CLASS_NAME, 'inventory_item_desc')
    PRICE = (By.CLASS_NAME, 'inventory_item_price')
    BTN = (By.XPATH, ".//button[contains(@class,'cart_button')]")