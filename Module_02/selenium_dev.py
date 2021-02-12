from common.webdriver_factory import get_driver

driver = get_driver('chrome')

driver.get('https://www.selenium.dev/')
print(f'Current Title: {driver.title}')
print(f'Current URL: {driver.current_url}')


def hyperlink_search(text):
    word = text
    gmail_link = driver.find_element_by_link_text(word)
    print(f'{word} Link is displayed: {gmail_link.is_displayed()}')
    print(f'{word} Link is enabled: {gmail_link.is_enabled()}')
    print(f'{word} Link is selected: {gmail_link.is_selected()}')
    if gmail_link.is_enabled() and gmail_link.is_displayed():
        gmail_link.click()
    print(f'{word} Link is displayed {driver.page_source.count(word)} times')


hyperlink_search('Downloads')
hyperlink_search('Projects')
hyperlink_search('Support')
hyperlink_search('Blog')

driver.quit()
