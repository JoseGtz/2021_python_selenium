from common.webdriver_factory import get_driver

driver = get_driver('chrome')
driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&dsh=S-754881558%3A1613063574131574&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')

firstname = driver.find_element_by_id('firstName')
firstname.clear()
firstname.send_keys('Jose Luis')
lastname = driver.find_element_by_id('lastName')
lastname.clear()
lastname.send_keys('Gutierrez')
username = driver.find_element_by_id('username')
username.clear()
username.send_keys('jgutz')
password = driver.find_element_by_name('Passwd')
password.clear()
password.send_keys('password')
password = driver.find_element_by_name('ConfirmPasswd')
password.clear()
password.send_keys('password')

login = driver.find_element_by_id('accountDetailsNext')
login.click()

driver.quit()