from selenium.webdriver import Chrome

def test_imdb_search():
    driver = Chrome("/Users/andymckerrow/Helio/QAPoint/Python-Selenium-UI-Tests/_drivers/chromedriver")
    driver.get("https://www.imdb.com/")
    driver.find_element_by_id('navbar-query').send_keys('badlands')
    driver.find_element_by_css_selector('[class*="magnifyingglass"]').click()
    assert driver.title == 'Find - IMDb'

def test_imdb_halloween():
    driver = Chrome("/Users/andymckerrow/Helio/QAPoint/Python-Selenium-UI-Tests/_drivers/chromedriver")
    driver.get("https://www.imdb.com/")
    driver.find_element_by_link_text('Halloween').click()
    assert driver.title == 'Halloween (2018) - IMDb'

#next test searches for movie and selects the desired one
def test_imdb_navtobadlands():
    driver = Chrome("/Users/andymckerrow/Helio/QAPoint/Python-Selenium-UI-Tests/_drivers/chromedriver")
    driver.get("https://www.imdb.com/")
    driver.find_element_by_id('navbar-query').send_keys('badlands')
    driver.find_element_by_css_selector('[class*="magnifyingglass"]').click()
    driver.find_element_by_link_text('Badlands').click()
    assert driver.title == 'Badlands (1973) - IMDb'  

#next test navigates to page and makes assertions about the content displayed
def test_imdb_badlandsreleasedate():
    driver = Chrome("/Users/andymckerrow/Helio/QAPoint/Python-Selenium-UI-Tests/_drivers/chromedriver")
    driver.get("https://www.imdb.com/")
    driver.find_element_by_id('navbar-query').send_keys('badlands')
    driver.find_element_by_css_selector('[class*="magnifyingglass"]').click()
    driver.find_element_by_link_text('Badlands').click()
    assert 'Badlands (1973) - IMDb' + '1973'
    assert 'Badlands (1973) - IMDB' + 'PG'
    assert 'Badlands (1973) - IMDB' + '1hr 34min'
    assert 'Badlands (1973) - IMDB' + 'Crime'
    assert 'Badlands (1973) - IMDB' + 'Drama'
    assert 'Badlands (1973) - IMDB' + 'Terrence Malick'

    