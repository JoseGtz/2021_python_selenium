from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait

driver = get_driver('chrome')
wait = WebDriverWait(driver, 10)
driver.get('https://www.google.com/')

element = driver.find_elements_by_xpath("//body/div[1]")
print(element)

element = driver.find_elements_by_xpath("//body/div[last()]")
print(element)

element = driver.find_elements_by_xpath("//body/div[last()]")
print(element)

driver.quit()