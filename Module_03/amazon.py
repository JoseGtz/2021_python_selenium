from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait

driver = get_driver('chrome')
wait = WebDriverWait(driver, 10)
driver.get('https://www.amazon.com/')

elements = driver.find_elements_by_xpath("//a")
print(f'Tags con A encontrados: {len(elements)}')
for element in elements:
    print(element)

elements = driver.find_elements_by_xpath("//head/*")
print(f'Elementos hijos de Head encontrados: {len(elements)}')
for element in elements:
    print(element)

driver.quit()