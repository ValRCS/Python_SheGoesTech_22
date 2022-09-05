import requests
import json

response = requests.get('https://api.fbi.gov/wanted/v1/list', params={
    'race': 'white', 'eyes': 'green', 'sex': 'male'
    #    'terrorism': 'all'
})
# fbi_data = json.loads(response.content)
fbi_data = response.json() # same as above
count = fbi_data['total']
print(count)
print(fbi_data['items'][0]['race'], type(fbi_data['items'][1]['race']))

i = 0
while i < 10:
    print(fbi_data['items'][i]['title'], fbi_data['items'][i]['publication'])
    i = i + 1

max_items=10
for item in fbi_data['items'][:max_items]:
    print(item['title'], item['publication'])

with open("fbi_data_file.json", mode="w") as write_file:
    json.dump(fbi_data, write_file, indent=4)  # so mydata could be any standard python data structure