import json
import requests

r = requests.get('https://date.nager.at/api/v2/publicholidays/2020/US')
print(r.json())
print(type(r))

json_data = json.loads(r.text)

jsonStr = json.dumps(json_data)
print(jsonStr)
print(type(jsonStr))

with open('public_holidays.json', 'w', encoding="UTF8") as f:
    json.dump(json_data, f, indent=4, ensure_ascii=False)
# writeFile = open('public_holidays_us.json', 'w')
# writeFile.write(jsonStr)
# writeFile.close()
