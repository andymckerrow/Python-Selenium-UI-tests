from selenium.webdriver import Chrome

def test_imdb_search():
    driver = Chrome("/Users/andymckerrow/Helio/QAPoint/Python-Selenium-UI-Tests/_drivers/chromedriver")
    driver.get("https://www.imdb.com/")
    driver.find_element_by_id('navbar-query').send_keys('badlands')
    driver.find_element_by_css_selector('[class*="magnifyingglass"]').click()
    assert driver.title == 'Find - IMDb'

def test_imdb_halloween():
    driver = Chrome("/Users/andymckerrow/Helio/QAPoint/_drivers/chromedriver")
    driver.get("https://www.imdb.com/")
    driver.find_element_by_link_text('Halloween').click()
    assert driver.title == 'Halloween (2018) - IMDb'

    #next tests: go to results page, pick the right movie, then make assertions about all the facts
    