from common.webdriver_factory import get_driver
from selenium.webdriver.support.ui import Select

driver = get_driver('chrome')
driver.get('https://formsmarts.com/html-form-example')
driver.switch_to.frame(driver.find_element_by_class_name('fs_embed'))

firstname = driver.find_element_by_id('u_jSx_4607')
firstname.clear()
firstname.send_keys('Jose Luis')

lastname = driver.find_element_by_id('u_jSx_338354')
lastname.clear()
lastname.send_keys('Gutierrez')

email = driver.find_element_by_id('u_jSx_4608')
email.clear()
email.send_keys('jgutz@gmail.com')

dropdown = driver.find_element_by_id("u_jSx_338367")
dropdown = Select(dropdown)
dropdown.select_by_value("Sales Inquiry")

inquiry = driver.find_element_by_id('u_jSx_4609')
inquiry.clear()
inquiry.send_keys('Inquiry Test')

siguiente = driver.find_element_by_name('submit')
siguiente.click()

driver.quit()