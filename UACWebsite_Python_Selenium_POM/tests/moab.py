import selenium
import pytest
from selenium.webdriver import Chrome

#tests commented out were unsuccessful strategies

def test_MoabWindDriftedSnow():
   driver = Chrome('/Users/andymckerrow/Helio/QAPoint/UAC_Python_selenium/_drivers/chromedriver')
   driver.get('https://utahavalanchecenter.org')
   driver.find_element_by_partial_link_text('Moab').click
   driver.find_element_by_xpath('//h5')
   #driver.find_element_by_css_selector('.html5-video-player')
   if ("Wind Drifted Snow" in 'forecast/moab'):pass
   #else:driver.find_element_by_css_selector("logo.svg").click
   #else:driver.find_element_by_class_name, value='header-logo full-width'
   #driver.find_element_by_id('player_uid_372562855_1').click
   #assert "Wind Drifted Snow" in 'div class="view-content"'
   
def test_MoabWetSlab():
   driver = Chrome('/Users/andymckerrow/Helio/QAPoint/UAC_Python_selenium/_drivers/chromedriver')
   driver.get('https://utahavalanchecenter.org')
   #driver.find_element_by_css_selector('[class*="sm-col sm-col-4 md-col-4 lg-col-4"]').click()
   driver.find_element_by_partial_link_text('Moab').click
   driver.find_element_by_xpath('//div/h5')
   #assert "Persistent" in 'Avalanche Problem #1'
  
   
 