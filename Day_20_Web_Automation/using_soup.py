import requests
from bs4 import BeautifulSoup as bs

url = "https://mdn.github.io/beginner-html-site/"

response = requests.get(url)  # this is like going to our browser and going to the url
print(response.status_code)  # 200 would be good 404 would be bad

print(response.text[:500])  # first 500 characters

# i could parse by hand but i can use beautiful soup

# # we parse our raw text html into a soup object
soup = bs(response.text, "html.parser")  # html parser is optional we can tell it use lxml which might be better parser
print(soup.title)
print(type(soup))
headline = soup.find("h1") # there should only be one h1 tag in the html
print(headline)

print(headline.text)  # gets you text
images = soup.find_all("img")  # get all images tags
print(images)
print(len(images))
# we would want some logic here to test length of images
if len(images) > 0:
    first_image = images[0]
    print(first_image.attrs)
    for key, value in first_image.attrs.items():  # attrs is a dictionary
        print("attribute", key, "value:", value)
