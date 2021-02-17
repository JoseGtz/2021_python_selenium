from common.webdriver_factory import get_driver
from selenium.webdriver.support.ui import Select

driver = get_driver('chrome')
driver.implicitly_wait(5)
driver.get('https://formsmarts.com/form/axi?mode=h5')

firstname = driver.find_element_by_id('u_LY9_60857')
firstname.clear()
firstname.send_keys('Jose Luis')

lastname = driver.find_element_by_id('u_LY9_60858')
lastname.clear()
lastname.send_keys('Gutierrez')

email = driver.find_element_by_id('u_LY9_60859')
email.clear()
email.send_keys('jgutz@gmail.com')

address = driver.find_element_by_id('u_LY9_60860')
address.clear()
address.send_keys('123 Street')

country = Select(driver.find_element_by_id('u_LY9_60871'))
country.select_by_visible_text('Mexico')

date = driver.find_element_by_id('u_LY9_60861')
date.clear()
date.send_keys('12/12/2021')

room_type = driver.find_element_by_id('u_LY9_60866_1')
room_type.click()

nights = driver.find_element_by_id('u_LY9_60870')
nights.clear()
nights.send_keys('2')

submit = driver.find_element_by_name('submit')
submit.click()

forms_fields = ['Jose Luis', 'Gutierrez', 'jgutz@gmail.com','123 Street','Mexico', '12/12/2021']
out_name = driver.find_elements_by_
out_lastname = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[2]/td')
out_email = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td')
out_inquiry = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[5]/td')
out_subject_inquiry = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[4]/td')

for fields in forms_fields:
    if fields in out_name.text:
        print(f'Name: {fields} -> {out_name.text}')
    elif fields in out_lastname.text:
        print(f'Last Name: {fields} -> {out_lastname.text}')
    elif fields in out_email.text:
        print(f'email: {fields} -> {out_email.text}')
    elif fields in out_inquiry.text:
        print(f'Inquiry: {fields} -> {out_inquiry.text}')
    elif fields in out_subject_inquiry.text:
        print(f'Subject of Your Inquiry: {fields} -> {out_subject_inquiry.text}')
    else:
        print('Form is not matching')

#driver.quit()