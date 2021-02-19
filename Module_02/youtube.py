from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = get_driver('chrome')
wait = WebDriverWait(driver, 5)
driver.get('https://www.youtube.com/')

locator = (By.ID, 'search')
search_textbox = wait.until(EC.element_to_be_clickable(locator))
search_textbox.send_keys('Selenium')

locator = (By.ID, 'search-icon-legacy')
search_button = wait.until(EC.element_to_be_clickable(locator))
search_button.click()

locator = (By.ID, 'video-title')
results = wait.until(EC.visibility_of_all_elements_located(locator))
wait = WebDriverWait(driver, 15)
print(f'Titulos: {len(results)}')
for result in results:
    print(result.text)

driver.quit()