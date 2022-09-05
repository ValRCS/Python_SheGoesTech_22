# Martins Klavins
# day-13

import requests
import json


def get_whole_currency(url="https://api.coinbase.com/v2/currencies"):
    response = requests.get(url)
    """
    type(response.json()) = dict
    type((response.json()).values()) = dict_values
    type(data) = list
    list((response.json()).values())[0] = data[0]
    """
    # data = list((response.json()).values())[0]
    data = response.json().get("data", ())  # i am using get to provide a default value in case the data is not found
    output_json = list()
    output_data = list()
    for element in data:
        """
        The get() method returns the value for the specified key
        element = dictionaries
        data = list of dictionaries
        """
        if element.get("min_size") == "1.00000000":
            output_data.append(element.get("name"))
            output_json.append(element)
    create_json(output_json)

    return output_data


def create_json(data):
    with open("my.json", "w") as output_file:
        json.dump(data, output_file)


if __name__ == '__main__':
    print("currencies without decimal places: ", get_whole_currency())
