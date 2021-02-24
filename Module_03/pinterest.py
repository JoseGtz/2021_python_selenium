from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.webdriver_factory import get_driver


def login(wait: WebDriverWait, email, my_pass):
    login_locator = (By.XPATH, "//*[@data-test-id='simple-login-button']//button")
    login_element = wait.until(EC.element_to_be_clickable(login_locator))
    login_element.click()
    user_locator = (By.ID, 'email')
    user_element = wait.until(EC.element_to_be_clickable(user_locator))
    user_element.clear()
    user_element.send_keys(email)
    password_locator = (By.ID, 'password')
    password_element = wait.until(EC.element_to_be_clickable(password_locator))
    password_element.clear()
    password_element.send_keys(my_pass)
    submit_bttn_locator = (By.XPATH, "//*[@data-test-id='registerFormSubmitButton']//button")
    submit_bttn = wait.until(EC.element_to_be_clickable(submit_bttn_locator))
    submit_bttn.click()


def search(wait: WebDriverWait, value: str):
    textbox_locator = (By.XPATH, "//*[@data-test-id='search-box-input']")
    textbox_element = wait.until(EC.element_to_be_clickable(textbox_locator))
    textbox_element.clear()
    textbox_element.send_keys(value)
    textbox_element.send_keys(Keys.ENTER)


if __name__ == '__main__':
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 10)
    driver.get('https://www.pinterest.com.mx')
    login(wait, 'qamindstester@gmail.com', 'Q@Minds4%')
    search(wait, 'Selenium')
    driver.quit()
