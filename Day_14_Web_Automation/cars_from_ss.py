# 14. 11.04.2022

import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("C:\\Temp\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

url = "https://www.ss.com/lv/"
driver.get(url)
time.sleep(1)
cars_element = driver.find_element(by=By.ID, value="mtd_97")  # Vieglie auto
print(cars_element.text)
# print(cars_element.get_attribute("href"))
cars_element.click()
time.sleep(1)
ford = driver.find_element(by=By.LINK_TEXT, value="Ford")

print(ford.text)
ford.click()
time.sleep(1)
# print(driver.current_url) # https://www.ss.com/lv/cars/ford/

c1 = driver.find_elements(by=By.CLASS_NAME, value="am")  # all cars from the first page

get_all_links = [x.get_attribute("href") for x in c1 if x.text != ""]
get_all_msg_links = [x for x in get_all_links if x.startswith("https://www.ss.com/msg/lv/transport/cars/ford/")]

# print(get_all_links)

with open("all_cars_first_page.txt", "w") as f:
    json.dump(get_all_msg_links, f, indent=2)

# with open("C:\\Temp\\all_cars_first_page.csv", "w") as f:
#     json.dump(get_all_msg_links, f, indent=2)

# Get screenshot of the first page
driver.maximize_window()

driver.get_screenshot_as_file("all_cars_first_page.png")
driver.close()