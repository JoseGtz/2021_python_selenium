from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def search(wait: WebDriverWait, value: str):
    textbox_locator = By.ID, 'search'
    textbox_element = wait.until(EC.element_to_be_clickable(textbox_locator))
    textbox_element.clear()
    textbox_element.send_keys(value)
    textbox_element.send_keys(Keys.ENTER)

def get_catalog_info(wait: WebDriverWait) -> list:
    result = []
    result_locator = (By.CLASS_NAME, 'result_item')
    search_results = wait.until(EC.visibility_of_all_elements_located(result_locator))
    for search_result in search_results:
        search_result: WebElement
        name = search_result.find_element_by_class_name('title')
        result.append(f'Name: {name.text}')
    return result

if __name__ == '__main__':
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 10)
    driver.get('https://www.tiktok.com/?lang=es')
    search(wait, 'Python')
    print(get_catalog_info(wait))
    driver.quit()
