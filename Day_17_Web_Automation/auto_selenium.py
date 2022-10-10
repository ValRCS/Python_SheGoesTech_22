from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # we might need to insert some delay in the code
from selenium.webdriver.chrome.service import Service

# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
#
# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome()
# deprecation warning, use webdriver.Chrome() instead if you have path to chromedriver set up
# driver = webdriver.Chrome("C:\\Temp\\chromedriver.exe")  # set path to chromedriver if you have no PATH
driver = webdriver.Chrome()  # I have path to chromedriver in my PATH so i can do this
# driver.get("https://www.tvnet.lv/")
url = "https://www.ss.com/"
driver.get(url)  # this will open the url in browser
time.sleep(2)  # this will wait for 2 seconds
print(driver.title)  # this will print the title of the page

# apartment_element = driver.find_element_by_id("mtd_59")  # this id is for this particular page
# apartment_element = driver.find_element("#mtd_59")  # this id is for this particular page
apartment_element = driver.find_element(by=By.ID, value="mtd_59")
# driver.find_element(by=By.ID, value="mtd_59").click() # this will find AND click on the element

print(apartment_element.text)  # this will print the text of the element
# apartment_element.click()  # this will click on the element with id "mtd_59"
# print(apartment_element.a)
print(apartment_element.get_attribute("href"))
print(apartment_element.get_attribute("nosuchattributehref"))
apartment_element.click()
time.sleep(0.5)
# regions = driver.find_elements_by_tag_name("h4")  # there is also a singular  find_element which find first match
regions = driver.find_elements(by=By.TAG_NAME, value="h4")  # there is also a singular  find_element which find first match
print("Found", len(regions), "regions")
first_region = regions[0]  # should be Riga in our example
print(first_region.text)
#
# # first_region_children = first_region.children  # this will return a list of elements that are children of first region
# # https://stackoverflow.com/questions/24795198/get-all-child-elements
first_region_children = first_region.find_elements(By.XPATH, ".//*")
#
# # this will return first anchor among children
print("Found", len(first_region_children), "children")
print(first_region_children)
print(first_region_children[0].tag_name, first_region_children[0].text)
# first_anchor_among_children = first_region_children[0].find_element_by_tag_name("a")
first_anchor_among_children = first_region.find_element(By.TAG_NAME, "a")
print(first_anchor_among_children == first_region_children[0])
print(first_region_children[0].get_attribute("href"))
first_region_children[0].click()
#
#
# def my_function(my_param):
#     """
#     This is a function
#     also it has a docstring
#     @my_param is a parameter
#     """
#     print("Hello from my_function")
#     print(my_param)
#
#
# my_function("Hello")
