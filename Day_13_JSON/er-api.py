import json
import requests  # this library is not included with Python but is very popular and comes with Anaconda
import time

my_json_url = "https://open.er-api.com/v6/latest/EUR"
response = requests.get(my_json_url)
i = 0
error_msg = ""
print(response.status_code)

if str(response.status_code) != "200":
    print("here")
    while response.status_code != "200":
        response = requests.get(my_json_url)
        time.sleep(1)
        i += 1;
        if i == 10:
            error_msg = "Resource not available"
            break

if error_msg == "":
    data_from_json = response.json()
    print(data_from_json)

    print(data_from_json['rates'])
    print("Current EUR rate in USD = ", data_from_json['rates']["USD"])
else:
    print(error_msg)

with open("my_rates_indented.json", mode="w") as write_file:
    json.dump(data_from_json, write_file, indent=4)  # so mydata could be any standard python data structur