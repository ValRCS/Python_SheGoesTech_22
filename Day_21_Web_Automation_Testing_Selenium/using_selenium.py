# main difference between selenium and 
# requests with Beautiful Soup 
# is that selenium is used for web automation testing
# Selenium is a web automation testing tool
# Selenium controls the browser


# unofficial documentation
# https://selenium-python.readthedocs.io/
# 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# we need to install drivers for the browser that we want to use
# https://www.selenium.dev/documentation/en/webdriver/driver_requirements/
# https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

# browser = webdriver.Firefox()
# browser = webdriver.Safari() # Mac
# browser = webdriver.Chrome()
# indicate the path to the driver
# browser = webdriver.Chrome('C:/DRIVERS/chromedriver.exe')
# alternative is to add the driver to the PATH
# https://www.selenium.dev/documentation/en/webdriver/driver_requirements/#adding-the-chrome-driver-to-your-path

# now that I have copied the driver to the PATH in this case C:/temp
# it is not necessary to indicate the path to the driver
browser = webdriver.Chrome()

# browser.get('http://www.yahoo.com')
browser.get('http://www.google.com')
time.sleep(32) # 1200 milliseconds
# assert 'Yahoo' in browser.title  # assert that we got the right page
assert 'Google' in browser.title  # assert that we got the right page

# click on privacy policy
# browser.find_element_by_link_text('Privacy').click()
# Click on element with text "Piekrist visiem"
print("Ready to click")
accept  = browser.find_element_by_xpath("//*[contains(text(), 'Piekrist visiem')]")
accept.click()
# browser.find_element_by_link_text('Piekrist visiem').click()
time.sleep(5)  # we might want to look for specific elements on the page to indicate loaded page

# 

# elem = browser.find_element_by_name('p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)
