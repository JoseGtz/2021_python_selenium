"""First Selenium Example"""
from selenium import webdriver

driver_path = '/Users/user/2021_python_selenium/drivers/geckodriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://google.com')
search_box = driver.find_element_by_name('q')
search_box.send_keys('QA Minds')
driver.quit()