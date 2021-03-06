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

out_name = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[1]/td')
out_lastname = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[2]/td')
out_email = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td')
out_inquiry = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[5]/td')
out_subject_inquiry = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[4]/td')

forms_fields = ['Jose', 'Gutierrez', 'jgutz@gmail.com', 'Test', 'Sales Inquiry']

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

driver.quit()