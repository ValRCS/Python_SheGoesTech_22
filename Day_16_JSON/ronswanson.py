import json
import requests

print("Find a JSON API of your choice")
print("This will get: Ron Swanson quotes.")
print("________________________________________________________")


def get_Ron_Swanson_quotes(url="https://ron-swanson-quotes.herokuapp.com/v2/quotes/25"):
    requests.get(url)
    response = requests.get(url)
    data_from_json = response.json() # we get a list in this case
    print(type(data_from_json)) # should be list
    with open("Quotes.json", mode="w") as write_file:
        json.dump(data_from_json, write_file, indent=4)

    return response


# getcount = int(input("How many quotes do you want to se: : "))
print(get_Ron_Swanson_quotes())
