# # #!/usr/bin/env python
# # # coding: utf-8
# #
# # # ## JSON
# #
# # # # JSON - Javascript Object Notation
# # # #### Invented by Douglas Crockford when working at Yahoo in early 2000s.
# # #
# # # * Goal - Human Readable, Machine Parsable
# # #
# # # * Specification: https://www.json.org/
# #
# # # JSON — short for JavaScript Object Notation — format for sharing data.
# # #
# # # JSON is derived from the JavaScript programming language
# # #
# # # Available for use by many languages including Python
# # #
# # # usually file extension is .json when stored
# # #
# # #
# #

import json
import requests


# # # In[ ]:
# #
# #
# # # Sample JSON below from https://json.org/example.html
# # # Question why is Syntax highlighting working properly ? :)
# #
# #
# # # In[1]:
#
#
# # {"widget": {
# #     "debug": "on",
# #     "window": {
# #         "title": "Sample Konfabulator Widget",
# #         "name": "main_window",
# #         "width": 500,
# #         "height": 500
# #     },
# #     "image": {
# #         "src": "Images/Sun.png",
# #         "name": "sun1",
# #         "hOffset": 250,
# #         "vOffset": 250,
# #         "alignment": "center"
# #     },
# #     "text": {
# #         "data": "Click Here",
# #         "size": 36,
# #         "style": "bold",
# #         "name": "text1",
# #         "hOffset": 250,
# #         "vOffset": 100,
# #         "alignment": "center",
# #         "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
# #     }
# # }}
# #
# #
# # # In[4]:
# #
# #
# # # if this was string starting with { it would be our json
# mydata = {
#     "firstName": "Jane",
#     "lastName": "Doe",
#     "hobbies": ["running", "sky diving", "dancing"],
#     "age": 43,
#     "children": [
#         {
#             "firstName": "Alice",
#             "age": 7
#         },
#         {
#             "firstName": "Bob",
#             "age": 13
#         }
#     ]
# }
# print(type(mydata))  # <class 'dict'>
# print(mydata)
# print(mydata.keys())  # dict_keys(['firstName', 'lastName', 'hobbies', 'age', 'children'])
# # we get a list of children (each child is a dictionary again)
# print(mydata['children'])  # [{'firstName': 'Alice', 'age': 7}, {'firstName': 'Bob', 'age': 13}]
# print(mydata['children'][0])  # {'firstName': 'Alice', 'age': 7}
# print(mydata['children'][0]['firstName'])  # Alice
# print(mydata['children'][0]['age'])  # 7
# print(mydata['hobbies'][1])  # sky diving
# print(mydata.get('hobbies'))  # ['running', 'sky diving', 'dancing']

# #
# #
# # # In[2]:
# #
# #
# # type(mydata)
# #
# #
# # # In[ ]:
# #
# #
# # print(mydata)
# #
# #
# # # In[3]:
# #
# #
# # mydata['children']
# #
# #
# # # In[4]:
# #
# #
# # type(mydata['children'])
# #
# #
# # # In[ ]:
# #
# #
# print(mydata['children'][0])
# print(mydata['children'][0]['firstName'])
#
# #
# #
# # # In[ ]:
# #
# #
# # type(mydata['children'][0])
# #
# #
# # # In[ ]:
# #
# #
# # mydata['children'][0]['age']
# #
# #
# # # In[ ]:
# #
# #
# # mydata['children'][-1]['age']
# #
# #
# # # In[ ]:
# #
# #
# # mydata.get('hobbies') # get has the default value None if the key is not found
# #
# #
# # # In[ ]:
# #
# #
# print(mydata.get("hobbies"))
# print(mydata.get('hobbies')[-1], mydata['hobbies'][-1], mydata['hobbies'][2])
# #
# #
# # # In[ ]:
# #
# #
# # # list has no get [1,2,3].get(2)
# #
# #
# # # In[ ]:
# #
# #
# # {"a":43,"b":30}.get("b")
# #
# #
# # # The process of encoding JSON is usually called serialization. This term refers to the transformation of data into a series of bytes (hence serial) to be stored or transmitted across a network. You may also hear the term marshaling, but that’s a whole other discussion. Naturally, deserialization is the reciprocal process of decoding data that has been stored or delivered in the JSON standard.
# # #
# # # All we’re talking about here is reading and writing. Think of it like this: encoding is for writing data to disk, while decoding is for reading data into memory.
# # #  https://realpython.com/python-json/
# #
# # # In[5]:
# #
# #
# # mydata # simply a PYthon dictionary with some lists inside etc
# #
# #
# # # In[2]:
# #
# #
# # # we need a library for decoding and encoding json
# # # comes built into standard Python library
import json

#
# #
# #
# # # In[6]:
# #
# #
# # # first we are going to dump our data into a text file
# with open("data_file.json", mode="w") as write_file:
#     json.dump(mydata, write_file)
# # # remember that stream is closed here and file is written by now
# #
# #
# # # In[ ]:
# #
# #
# # # json.dump()
# #
# #
# # # In[7]:
# #
# #
# # # this will be nicer
# with open("data_file_indented.json", mode="w") as write_file:
#     json.dump(mydata, write_file, indent=4)  # so mydata could be any standard python data structure
# #
# #
# # # In[ ]:
# #
# #
# # mydata
# #
# #
# # # In[8]:
# #
# #
# mydata['children'].append({'firstName': "Čarlijs", 'age': 14})
# print(mydata)
# mydata['hobbies'].append("ābolu ēšana")
# print(mydata)
# #
# #
# # # In[9]:
# #
# #
# # # this will be nicer
# with open("data_file_indented_ch.json", mode="w") as write_file:
#     json.dump(mydata, write_file, indent=4)  # so mydata could be any standard python data structure
# # #
# # #
# # # # In[10]:
# # #
# # #
# # # # when we want to save unicode directly
# with open("data_file_indented_ch_unicode.json", mode="w", encoding="utf-8") as write_file:
#     json.dump(mydata, write_file, indent=4, ensure_ascii=False)  # when we want unicode inside our json text file
# #
# #
# # if we want a JSON string but are not ready to write just yet
# my_string = json.dumps(mydata, indent=4, ensure_ascii=False)
# print(my_string)
# print(type(my_string))
#
# my_tuple = ("Valdis", 14, "Ābolu ēšana", None, True, False, (5,9), [1, 2, 3], {"a": 43, "b": 30})
# print(my_tuple)
# my_json_from_tuple = json.dumps(my_tuple, ensure_ascii=False)
# print(my_json_from_tuple)
# print(type(my_json_from_tuple))  # just a string
# my_list_from_json_string = json.loads(my_json_from_tuple)
# print(my_list_from_json_string)
# # my_string is a string not a Python dictionary any more!
# # # In[12]:
# #
# #
# # mylist = ["Valdis", {"likes":["potatoes", "chocolate"]}, 50, 60, 70, None, True, False, "Something"]
# # mylist
# #
# #
# # # In[13]:
# #
# #
# # with open("mylist.json", mode="w") as write_file:
# #     json.dump(mylist, write_file, indent=4)
# #
# #
# # # # Reading JSON and then deserialization (txt -> Python data structure)
# #
# # # In[14]:
# #
# #
# with open("data_file_indented_ch_unicode.json", encoding='utf-8') as file_stream:
#     raw_string = file_stream.read()
# # # raw_txt[:150] # so again raw JSON is just text
# print(raw_string)
# print(type(raw_string))
# # #
# # #
# # # # In[ ]:
# # #
# # #
# # # type(raw_txt)
# # #
# # #
# # # # In[15]:
# # #
# # #
# # # # deserialize, decode from json string into Python Data structure
# my_data = json.loads(raw_string)
# print(my_data)
# print(type(my_data))  # now it is a Python dictionary
# # #
# # #
# # # # In[16]:
# # #
# # #
# # # my_data.keys()
# # #
# # #
# # # # In[17]:
# # #
# # #
# # # my_data
# # #
# # #
# # # # In[18]:
# # #
# # #
# # # my_data['children']
# # #
# # #
# # # # In[19]:
# # #
# # #
# # # # more often we will load json immediately
# # with open("data_file_indented.json") as f:
# #     my_data_2 = json.load(f)  # if json is malformed then you will get some sort of error
# # print(my_data_2)
# # print(type(my_data_2))
# #
# # with open("data_file_indented_ch.json") as f:
# #     my_data_ch = json.load(f)  # if json is malformed then you will get some sort of error
# # print(my_data_ch)
# #
# with open("data_file_indented_ch_unicode.json", encoding="utf-8") as file_stream:
#     my_data_ch = json.load(file_stream)  # if json is malformed then you will get some sort of error
# # of course file_stream is closed here
# print(my_data_ch)
# print(type(my_data_ch))
# #
# # # In[21]:
# #
# #
# # # more often we will load json immediately
# # with open("mylist.json") as f:
# #     mylist_loaded = json.load(f) # if json is malformed then you will get some sort of error
# # type(mylist_loaded)
# #
# #
# # # In[22]:
# #
# #
# # mylist_loaded
# #
# #
# # # In[23]:
# #
# #
# # mylist_loaded[1]
# #
# #
# # # In[24]:
# #
# #
# # mylist_loaded[1]['likes']
# #
# #
# # # In[25]:
# #
# #
# # mylist_loaded[1]['likes'][0]
# #
# #
# # # In[20]:
# #
# #
# # # contents are the same but two different objects
# # my_data == my_data_2, my_data is my_data_2
# #
# #
# # # In[ ]:
# #
# #
# # my_json_string = json.dumps(my_data) # convert Python data structure(list,dictionary, and so on) into json string
# # # my_json_string[:100]
# # my_json_string
# #
# #
# # # In[ ]:
# #
# #
# # type(my_json_string)
# #
# #
# # # In[ ]:
# #
# #
# # my_data_structure = json.loads(my_json_string)
# # my_data_structure
# #
# #
# # # In[ ]:
# #
# #
# # mylist.extend([True, False, None])
# # mylist
# #
# #
# # # In[ ]:
# #
# #
# # json.dumps(mylist) # this gives us json formatted string
# #
# #
# # # In[ ]:
# #
# #
# # mylist.append((1,2,3))
# # mylist
# #
# #
# # # In[ ]:
# #
# #
# # json.dumps(mylist) # this gives us json formatted string
# #
# #
# # # In[ ]:
# #
# #
# # json.dumps(my_data)
# #
# #
# # # In[26]:
# #
# #
# import requests  # this library is not included with Python but is very popular and comes with Anaconda
#
# # # pip install requests otherwise
# #
# #
# # # In[27]:
# #
# #
# # # we make a http request to a url and print the response code
# # url = "https://my.api.mockaroo.com/ageincluded.json?key=58227cb0"
url = "https://jsonplaceholder.typicode.com/users/1/todos"
response = requests.get(url)  # so we made a HTTP GET request here just like a browser would
# # so you want to be careful how often you make requests
# # some/many sites will rate limit you or even block you if you make too many requests (100 a second would not be cool)
print(response.status_code)  # Response Code 200 is good! 404 not good :)
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
print(type(response))  # response is a Response object
print(response.text)  # string in unicode format

# typically, when accessing json you will want to parse it into a Python data structure

# #
# #
# # # In[28]:
# #
# #
data_from_json = response.json()  # we do not need json.loads
print(data_from_json)
print(type(data_from_json))  # so list of dictionaries
print(data_from_json[0])  # first element of the list - dictionary
#
# # if i wanted to save json from our url to a file
# here i skip unicode since this data is all in ascii english
with open("data_from_url.json", mode="w") as write_file:
    json.dump(data_from_json, write_file, indent=4)
    # json.dump(response.json(), write_file, indent=4) # same as above
#
# # if we wanted to save json from our url to a file directly
with open("data_from_url_direct.json", mode="w") as write_file:
    write_file.write(response.text)  # no need to deserialize it and then serialize it again
#
# # to convert our JSON to CSV we will make some assumptions
# # column names will be keys in the dictionary - in this case first one
# # and we will assume that all the dictionaries have the same keys
#
# # if that assumption is wrong then we will have to do some manual work
# # create a set of keys from all dictionaries to create column names
#
# # then after first row we will print all the values for each key
#
with open("data_from_url.csv", mode="w") as f:
    column_names = ",".join(data_from_json[0].keys())
    f.write(column_names + "\n")
    for row in data_from_json:  # each row is a dictionary
        values = ",".join([str(item) for item in row.values()])  # this manual method will break if there are commas in the values
        f.write(values + "\n")
#
import time  # this is a standard library that allows us to do time related stuff
#
# # it is considered good practice to use time.sleep() to slow down your requests
for i in range(10):
    print(i)
    # so make request here
    time.sleep(0.3)  # sleep for 0.3 seconds
# #
# # # In[29]:
# #
# #
# # response.text[:50]
# #
# #
# # # In[23]:
# #
# #
# # my_mock_data = json.loads(response.text) # kind of useless since we have response.json()
# # type(my_mock_data), len(my_mock_data)
# #
# #
# # # In[ ]:
# #
# #
# # data_from_json == my_mock_data, data_from_json is my_mock_data
# # # again data is the same, but 2 different objects
# #
# #
# # # In[30]:
# #
# #
# import pandas as pd # Anaconda includes by default
# #
# #
# # # In[31]:
# #
# #
# # # good when JSON is relatively flat (2d preferably)
# # df = pd.read_json(url) # so includes parsing and request to the server
# # df.head()
# #
# #
# # # In[26]:
# #
# #
# # df.to_csv("mock_data.csv")
# #
# #
# # # In[ ]:
# #
# #
# # data_from_json[:3]
# #
# #
# # # In[ ]:
# #
# #
# # df2 = pd.DataFrame(data_from_json) # in this data_from_json is Python data structure list
# # df2.head()
# #
# #
# # # In[ ]:
# #
# #
# # # idea get average age of Japanese Men in our JSON data
# #
# #
# # # In[ ]:
# #
# #
# # df.head()
# #
# #
# # # In[ ]:
# #
# #
# # males = df[df.gender == "Male"]
# # males.head(10)
# #
# #
# # # In[ ]:
# #
# #
# # adult_males = df[(df.gender == "Male") & (df.age > 18)]
# # adult_males.head()
# #
# #
# # # In[ ]:
# #
# #
# # data_from_json[:5]
# #
# #
# # # In[ ]:
# #
# #
# # myjson = data_from_json # just an alias
# # myjson[:3]
# #
# #
# # # In[ ]:
# #
# #
# # japanese = [person for person in myjson if person.get('email',"").endswith('.jp')]
# # # potentially person.get('email') could return None then .endswith('.jp') would fail with error
# # japanese
# #
# #
# # # In[ ]:
# #
# #
# # japanese_men = [p for p in japanese if p.get('gender') == "Male"]
# # # potentially person.get('email') could return None then .endswith('.jp') would fail with error
# # japanese_men
# #
# #
# # # In[ ]:
# #
# #
# # uk = [person for person in myjson if person.get('email',"").endswith('.uk')]
# # uk
# #
# #
# # # In[ ]:
# #
# #
# # uk_ages = [(person.get('first_name'),person.get('email'), person.get('sports'), int(person.get('age'))) for person in uk]
# # uk_ages # noone plays sports in uk....
# #
# #
# # # In[ ]:
# #
# #
# # with open("uk_ages.json", mode="w") as fstream:
# #     json.dump(uk_ages, fstream, indent=4)
# #
# #
# # # In[ ]:
# #
# #
# # uk_ages
# #
# #
# # # In[ ]:
# #
# #
# # # so we lose the tuple designed when writing to JSON and back
# # with open("uk_ages.json") as fstream:
# #     uk_data = json.load(fstream)
# # uk_data
# #
# #
# # # In[ ]:
# #
# #
# # with open("jp_ages.json", mode="w") as fstream:
# #     json.dump(jp_ages, fstream, indent=4)
# #
# #
# # # In[ ]:
# #
# #
# #
# #
# #
# # # In[ ]:
# #
# #
# # type(mydata)
# #
# #
# # # In[ ]:
# #
# #
# # json_string = my_json_string # just an alias
# # json_string
# #
# #
# # # In[ ]:
# #
# #
# # type(json_string)
# #
# #
# # # In[ ]:
# #
# #
# # type(mydata)
# #
# #
# # # In[ ]:
# #
# #
# # # Convert Json_string back to our Python Object
# # my_obj = json.loads(json_string)
# # my_obj
# #
# #
# # # In[ ]:
# #
# #
# # my_obj.get('firstName')
# #
# #
# # # In[ ]:
# #
# #
# # mydata
# #
# #
# # # In[ ]:
# #
# #
# # newlist = json.loads('[1,3,5,"Valdis"]')
# # newlist
# #
# #
# # # In[ ]:
# #
# #
# # type(newlist)
# #
# #
# # # In[ ]:
# #
# #
# # badlist = json.loads('[1,3,5,"Vald]",334342]')
# # badlist
# #
# #
# # # In[ ]:
# #
# #
# #
# #
# #
# # # In[ ]:
# #
# #
# # type(json_string)
# #
# #
# # # In[ ]:
# #
# #
# # # Avove example JSON and Python object have the same syntax but there are some differences
# #
# #
# # # ![object](../img/object.png)
# #
# # # ![Array](../img/array.png)
# #
# # # ![Value](../img/value.png)
# #
# # # Simple Python objects are translated to JSON according to a fairly intuitive conversion.
# # #
# # # Python	JSON
# # #
# # # dict <->	object
# # #
# # # list, tuple <->	array
# # #
# # # str	<-> string
# # #
# # # int, float	<-> number
# # #
# # # True <->true
# # #
# # # False <->false
# # #
# # # None <->	null
# #
# # # Keep in mind that the result of this method could return any of the allowed data types from the conversion table. This is only important if you’re loading in data you haven’t seen before. In most cases, the root object will be a dict or a list.
# #
# # # If you've gotten JSON data in from another program or have otherwise obtained a string of JSON formatted data in Python, you can easily deserialize that with loads(), which naturally loads from a string:
# #
# # # In[ ]:
# #
# #
# # json_string = """
# # {
# #     "researcher": {
# #         "name": "Ford Prefect",
# #         "species": "Betelgeusian",
# #         "relatives": [
# #             {
# #                 "name": "Zaphod Beeblebrox",
# #                 "species": "Betelgeusian"
# #             }
# #         ]
# #     }
# # }
# # """
# # data = json.loads(json_string)
# # data
# #
# #
# # # In[ ]:
# #
# #
# # # get value of relative's name
# # data['researcher']
# #
# #
# # # In[ ]:
# #
# #
# # # get value of relative's name
# # data['researcher']['relatives']
# #
# #
# # # In[ ]:
# #
# #
# # # get value of relative's name
# # data['researcher']['relatives'][0]
# #
# #
# # # In[ ]:
# #
# #
# # # get value of relative's name
# # data['researcher']['relatives'][0]['name']
# #
# #
# # # In[ ]:
# #
# #
# # data['researcher']['relatives'][0]['name'].split()[0]
# #
# #
# # # In[ ]:
# #
# #
# # data['researcher']['relatives'][0]['name'].split()[0][:4]
# #
# #
# # # In[ ]:
# #
# #
# # type(data)
# #
# #
# # # In[ ]:
# #
# #
# # import json
# # import requests
# #
# #
# # # In[ ]:
# #
# #
# # ## Lets get some data https://jsonplaceholder.typicode.com/
# #
# #
# # # In[ ]:
# #
# #
# # response = requests.get("https://jsonplaceholder.typicode.com/todos")
# # if response.status_code != 200:
# #     print("Bad Response: ", response.status_code)
# # print(response.status_code)
# # todos = json.loads(response.text)
# #
# #
# # # can open https://jsonplaceholder.typicode.com/todos in regular browser too..
# #
# # # In[ ]:
# #
# #
# # type(todos)
# #
# #
# # # In[ ]:
# #
# #
# # len(todos)
# #
# #
# # # In[ ]:
# #
# #
# # todos[:10]
# #
# #
# # # In[ ]:
# #
# #
# # # completedworks = [el for el in todos if el['completed'] == True]
# # completedworks = [el for el in todos if el.get('completed') == True]
# # len(completedworks)
# #
# #
# # # In[ ]:
# #
# #
# # completedworks[-10:]
# #
# #
# # # In[ ]:
# #
# #
# # type(completedworks)
# #
# #
# # # In[ ]:
# #
# #
# # users = {}
# # for el in completedworks:
# #     k = el['userId']
# #     if k in users:
# #         users[k] +=1
# #     else:
# #         users[k] = 1
# # users
# #
# #
# # # In[ ]:
# #
# #
# # users.items()
# #
# #
# # # In[ ]:
# #
# #
# # sorted(users.items(),key = lambda el: el[1], reverse=True)
# #
# #
# # # In[ ]:
# #
# #
# # # much simpler to use Counter
# # from collections import Counter
# #
# #
# # # In[ ]:
# #
# #
# # [el['userId'] for el in completedworks]
# #
# #
# # # In[ ]:
# #
# #
# # count = Counter([el['userId'] for el in completedworks])
# # count.most_common()
# #
# #
# # # In[ ]:
# #
# #
# # todos[:2]
# #
# #
# # # In[ ]:
# #
# #
# # # lets do everything at once
# # finishedcount = Counter([el.get('userId') for el in todos if el.get('completed') == True])
# # finishedcount.most_common()
# #
# #
# # # In[ ]:
# #
# #
# # import matplotlib.pyplot as plt
# #
# #
# # # In[ ]:
# #
# #
# # plt.bar(finishedcount.keys(), finishedcount.values())
# # plt.show()
# #
# #
# # # In[ ]:
# #
# #
# # todos[-3:]
# #
# #
# # # In[ ]:
# #
# #
# # [1,2] + [3,4,6,6]
# #
# #
# # # In[ ]:
# #
# #
# # todos += [{'completed':True},{'completed':True},{'completed':True},{'completed':True}]
# # todos[-5:]
# #
# #
# # # In[ ]:
# #
# #
# # # lets do everything at once
# # finishedcount = Counter([el.get('userId') for el in todos if el.get('completed') == True])
# # finishedcount.most_common()
# #
# #
# # # In[ ]:
# #
# #
# # myl = [('Valdis', 40), ('Alice',35), ('Bob', 23),('Carol',70)]
# #
# #
# # # In[ ]:
# #
# #
# # # Lambda = anonymous function
# #
# #
# # # In[ ]:
# #
# #
# # def myfun(el):
# #     return el[1]
# # # same as myfun = lambda el: el[1]
# #
# #
# # # In[ ]:
# #
# #
# # sorted(myl, key = lambda el: el[1], reverse=True)
# #
# #
# # # In[ ]:
# #
# #
# # # Exercise find out top 3 users with most tasks completed!
# #
# # # TIPS
# # # we need some sort of structure to store these user results before finding out top 3
# # # at least two good data structure choices here :)
# # # here the simplest might actually be the best if we consider userId values
# #
# #
# # # In[ ]:
# #
# #
# # todos[0]
# #
# #
# # # In[ ]:
# #
# #
# # todos[0]['userId']
# #
# #
# # # In[ ]:
# #
# #
# # todos[0]['completed']
# #
# #
# # # In[ ]:
# #
# #
# # # Here we create a new dictionary and and count the completed works by id
# # newdict = {}
# # for todo in todos:
# #     if todo['completed'] == True:
# #         if todo['userId'] in newdict:
# #             newdict[todo['userId']] += 1
# #         else:
# #             newdict[todo['userId']] = 1
# #
# #
# # # In[ ]:
# #
# #
# # newdict
# #
# #
# # # In[ ]:
# #
# #
# # sorted(newdict.items())
# #
# #
# # # In[ ]:
# #
# #
# # bestworkers = sorted(newdict.items(), key=lambda el: el[1], reverse=True)
# # bestworkers[:3]
# #
# #
# # # In[ ]:
# #
# #
# # users = [ el['userId'] for el in todos]
# # len(users),users[:15]
# #
# #
# # # In[ ]:
# #
# #
# # uniqusers = set(users)
# # uniqusers
# #
# #
# # # In[ ]:
# #
# #
# # # dictionary comprehension but could live without one
# # users = { el['userId'] : 0 for el in todos}
# #
# #
# # # In[ ]:
# #
# #
# # users
# #
# #
# # # In[ ]:
# #
# #
# # users.keys()
# #
# #
# # # In[ ]:
# #
# #
# # users.value
# #
# #
# # # In[ ]:
# #
# #
# # #{'completed': True,
# # # 'id': 8,
# # #  'title': 'quo adipisci enim quam ut ab',
# # #  'userId': 1}
# #
# #
# # # In[ ]:
# #
# #
# #
# #
# #
# # # In[ ]:
# #
# #
# # #idiomatic
# # for el in todos:
# #     users[el['userId']] += el['completed'] # Boolean False is 0 True is 1 obviously this might not be too readable
# #
# #
# # # In[ ]:
# #
# #
# # # same as above could be useful in more complicated cases
# # for el in todos:
# #     if el['completed'] == True:
# #         users[el['userId']] += 1
# #
# #
# # # In[ ]:
# #
# #
# # # there could be a one liner or a solution with from collections import Counter
# #
# #
# # # In[ ]:
# #
# #
# # users.items()
# #
# #
# # # In[ ]:
# #
# #
# # list(users.items())
# #
# #
# # # In[ ]:
# #
# #
# # userlist=list(users.items())
# #
# #
# # # In[ ]:
# #
# #
# # type(userlist[0])
# #
# #
# # # In[ ]:
# #
# #
# # # we pass a key anonymous(lambda) function
# # sorted(userlist, key=lambda el: el[1], reverse=True)[:3]
# #
# #
# # # In[ ]:
# #
# #
# # # lets try a simple way
# #
# #
# # # In[ ]:
# #
# #
# # mylist=[0]
# # mylist*=11
# #
# #
# # # In[ ]:
# #
# #
# # for el in todos:
# #     if el['completed'] == True:
# #         mylist[el['userId']] +=1
# #
# #
# # # In[ ]:
# #
# #
# # mylist
# #
# #
# # # In[ ]:
# #
# #
# # mylist.index(max(mylist))
# #
# #
# # # In[ ]:
# #
# #
# # # kind of hard to get more values need to get tricky
# #
# #
# # # # How about Pandas and Json ?
# #
# # # In[ ]:
# #
# #
# # import pandas as pd
# #
# #
# # # In[ ]:
# #
# #
# # df = pd.read_json('https://jsonplaceholder.typicode.com/todos') # SO THIS ACCESSes THE url
# #
# #
# # # In[ ]:
# #
# #
# # df.head()
# #
# #
# # # In[ ]:
# #
# #
# # df.to_csv('my_todos.csv')
# #
# #
# # # In[ ]:
# #
# #
# # df.shape
# #
# #
# # # In[ ]:
# #
# #
# # df.describe()
# #
# #
# # # In[ ]:
# #
# #
# # df.describe(include=['O'])
# #
# #
# # # In[ ]:
# #
# #
# # # we see that completed
# # df.groupby(['userId']).sum()
# #
# #
# # # In[ ]:
# #
# #
# # df.groupby(['userId']).sum()['completed']
# #
# #
# # # In[ ]:
# #
# #
# # df.groupby(['userId']).sum()['completed'].plot(kind="bar")
# #
# #
# # # In[ ]:
# #
# #
# # busyjson
# #
# #
# # # In[ ]:
# #
# #
# # df.groupby(['userId'])['completed'].sum()
# #
# #
# # # In[ ]:
# #
# #
# # # if we need a single column dataframe
# # df.groupby(['userId'])[['completed']].sum()
# #
# #
# # # In[ ]:
# #
# #
# # df.groupby(['userId'])['completed'].sum().sort_values()
# #
# #
# # # In[ ]:
# #
# #
# # df.groupby(['userId'])['completed'].sum().sort_values(ascending=False)
# #
# #
# # # In[ ]:
# #
# #
# # busyjson = pd.read_json('https://jsonplaceholder.typicode.com/todos').groupby(['userId'])['completed'].sum().sort_values(ascending=False).to_json()
# #
# #
# # # In[ ]:
# #
# #
# # def prettyJSON(myjson):
# #     return json.dumps(json.loads(myjson), indent=4)
# #
# #
# # # In[ ]:
# #
# #
# # type(busyjson)
# #
# #
# # # In[ ]:
# #
# #
# # prettybusy = prettyJSON(busyjson)
# #
# #
# # # In[ ]:
# #
# #
# # with open('prettybusy.json', mode='w') as f:
# #     f.write(prettybusy)
# #
# #
# # # # Exercise Find Public JSON API get data and convert it into Pandas DataFrame
# # #
# # # ## Many possible sources
# # #
# # # https://github.com/toddmotto/public-apis
# # #
# # # ### You want the ones without authorization and WITH CORS unless you are feeling adventurous and want to try with auth
# # #
# # #
# #
# # # In[ ]:
# #
# #
# # df = pd.read_json('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=50')
# # df.head()
# #
# #
# # # In[ ]:
# #
# #
# # df.columns = sorted(df.columns)
# # df.head()
# #
# #
# # # In[ ]:
# #
# #
# # response = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=50")
# # if response.status_code != 200:
# #     print("Bad Response: ", response.status_code)
# # print(response.status_code)
# # cats = json.loads(response.text)
# # cats[:3]
# #
# #
# # # In[ ]:
# #
# #
# # response = requests.get("https://cat-fact.herokuapp.com/facts/random",
# #                         params={"animal_type":"cat", "amount":20})
# # if response.status_code != 200:
# #     print("Bad Response: ", response.status_code)
# # print(response.status_code)
# # cats = json.loads(response.text) # simpler response.json()
# # cats[:3]
# #
# #
# # # In[ ]:
# #
# #
# # len(cats)`
# #
# #
# # # In[ ]:
# #
# #
# # response.status_code
# #
# #
# # # In[ ]:
# #
# #
# # cats2 = response.json()
# # len(cats2)
# #
# #
# # # In[ ]:
# #
# #
# # cats2 == cats, cats2 is cats
# # #data are the same we just have two different copies of them
# #
# #
# # # In[ ]:
# #
# #
# #
# #
# #
# # # In[ ]:
# #
# #
# # df.loc[0, 'text']
# #
# #
# # # In[ ]:
# #
# #
# # ## For authorization you generally need some sort of token(key)
# # # One example for zendesk API  https://develop.zendesk.com/hc/en-us/community/posts/360001652447-API-auth-in-python
# #
# #
# # # For an API token, append '/token' to your username and use the token as the password:
# # ## This will not work for those without zendesk access token
# #
# # url = 'https://your_subdomain.zendesk.com/api/v2/users/123.json'
# # r = requests.get(url, auth=('user@example.com/token', 'your_token'))
# # # For an OAuth token, set an Authorization header:
# #
# # bearer_token = 'Bearer ' + access_token
# # header = {'Authorization': bearer_token}
# # url = 'https://your_subdomain.zendesk.com/api/v2/users/123.json'
# # r = requests.get(url, headers=header)
# #
# #
# # # In[ ]:
# #
# #
# # def myReadJSON(url):
# #     response = requests.get(url)
# #     if response.status_code != 200:
# #         print("Bad Response: ", response.status_code)
# #     print("Status CODE", response.status_code)
# #     return json.loads(response.text)
# #
# #
# # # In[ ]:
# #
# #
# # rawdrinks = myReadJSON("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
# # type(rawdrinks)
# #
# #
# # # In[ ]:
# #
# #
# # rawdrinks.keys()
# #
# #
# # # In[ ]:
# #
# #
# # type(rawdrinks.get("drinks"))
# #
# #
# # # In[ ]:
# #
# #
# # # so a list of dictionaries will translate nicely to dataframe
# # mydrinks = pd.DataFrame(rawdrinks['drinks'])
# # mydrinks.head()
# #
# #
# # # In[ ]:
# #
# #
# # # we can Transpose to get a sense of all columns
# # mydrinks.head().T
# #
# #
# # # In[ ]:
# #
# #
# # drinks = pd.read_json("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
# # drinks.head()
# #
# #
# # # In[ ]:
# #
# #
# # # requests also works with post type of requests
# #
# #
# # # In[ ]:
# #
# #
# # url = "http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=3" # think how using f string you could change parameters
# #
# #
# # # In[ ]:
# #
# #
# # response = requests.get(url)
# # response.status_code
# #
# #
# # # In[ ]:
# #
# #
# # o_data = response.json()
# # type(o_data)
# #
# #
# # # In[ ]:
# #
# #
# # o_data.keys()
# #
# #
# # # In[ ]:
# #
# #
# # o_recipes = o_data.get('results')
# # type(o_recipes)
# #
# #
# # # In[ ]:
# #
# #
# # len(o_recipes)
# #
# #
# # # In[ ]:
# #
# #
# # o_recipes[:3]
# #
# #
# # # In[ ]:
# #
# #
# # dfrec = pd.DataFrame(o_recipes)
# # dfrec.head()
# #
# #
# # # In[ ]:
# #
# #
# # # for 100 suggestion is to use time.sleep(0.2)
# # # it is good manners to sleep a little to avoid DDOS attack on API server
# # import time
# # time.sleep(0.5) # half a second delay
# #
# #
# # # In[ ]:
# #
# #
# # url = "https://data.gov.lv/dati/lv/api/3/action/datastore_search?resource_id=27fcc5ec-c63b-4bfd-bb08-01f073a52d04&limit=5"
# # r = requests.get(url)
# # r.status_code
# #
# #
# # # In[ ]:
# #
# #
# # r.text
# #
# #
# # # In[ ]:
# #
# #
# # with open("ur_yearly.json", "w", encoding="utf-8") as f:
# #     f.write(r.text)
# #
# #
# # # In[ ]:
# #
# #
# # urdata = r.json()
# #
# #
# # # In[ ]:
# #
# #
# # with open("ur_yearly_indent.json", "w", encoding="utf-8") as f:
# #     json.dump(r.json(), f, indent=4)
# #
# #
# # # In[ ]:
# #
# #
# # type(urdata)
# #
# #
# # # In[ ]:
# #
# #
# # urdata.keys()
# #
# #
# # # In[ ]:
# #
# #
# # type(urdata.get('result'))
# #
# #
# # # In[ ]:
# #
# #
# # urdata.get('result').get('records')
# #
# #
# # # In[ ]:
# #
# #
# # ur = pd.DataFrame(urdata.get('result').get('records'))
# # ur
# #
# #
# # # In[ ]:
# #
# #
# # ur.to_excel("ur_results.xlsx")
# #
# #
# # # In[ ]:
# #
# #
# # next_url = urdata['result']["_links"]["next"]
# # next_url
# #
