import selenium
import pytest
from selenium.webdriver import Chrome

def test_google():
   #test code here
   driver = Chrome('/Users/andymckerrow/Helio/QAPoint/Python-Selenium-UI-Tests/_drivers/chromedriver')
   driver.get('https://google.com')
   driver.find_element_by_name('q').send_keys('weather')
   driver.find_element_by_name('btnK').submit()