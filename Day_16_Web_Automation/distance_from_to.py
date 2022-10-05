import time
from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome("C:\Windows\Temp\chromedriver.exe")  # set path to chromedriver if you have no PATH
driver = webdriver.Chrome()

url = "https://www.distancefromto.net/"
driver.get(url)  # this will open the url in browser
time.sleep(2)  # this will wait for 2 seconds
element = driver.find_elements(By.CLASS_NAME, "form")
element = driver.find_elements(By.CLASS_NAME, "bg-gray")
# distance_from: list[WebElement] = driver.find_elements_by_id("distancefrom")
# distance_from.insert("Riga")
# print(distance_from)

# driver.find_element_by_xpath('//*[@id="distancefrom"]').send_keys("Riga")
driver.find_element(By.XPATH, '//*[@id="distancefrom"]').send_keys("Riga")
# driver.find_element_by_xpath('//*[@id="distanceto"]').send_keys("Liepaja")
driver.find_element(By.XPATH, '//*[@id="distanceto"]').send_keys("Liepaja")
# driver.find_element_by_id("hae").submit()
driver.find_element(By.ID, "hae").click()
driver.send_keys(Keys.PAGE_DOWN)
