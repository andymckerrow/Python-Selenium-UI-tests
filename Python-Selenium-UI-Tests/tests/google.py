from selenium.webdriver import Chrome

def test_google_search():
    driver = Chrome("/Users/andymckerrow/Helio/QAPoint/_drivers/chromedriver")
    driver.get("https://google.com")
    driver.find_element_by_name('q').send_keys('puppies')
    driver.find_element_by_name('btnK').submit()
    assert driver.title == 'puppies - Google Search'
