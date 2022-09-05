import requests

response = requests.get("https://api.openbrewerydb.org/breweries")
data = response.json()

for x in data:
    print(x['name'], x['brewery_type'])

city = "riga"
# r = requests.get(f"https://api.openbrewerydb.org/breweries?by_city={city}")
r = requests.get("https://api.openbrewerydb.org/breweries?by_city=san_diego")
# careful with string interpolation if you do not control city

print(r.json())
# TODO save data to a file
