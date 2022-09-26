# # # # # # # # # # # Python Dictionaries
# # # # # # # # # # # https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# # # # # # # # # # # key - value pairs
# # # # # # # # # # # unordered
# # # # # # # # # # # other languages - associative array, map, hashmap
# # # # # # # # # # # O(1) value lookup - very quick even for large dictionaries
# # # # # # # # mutable - can be changed
# # # # # # # # dynamic can grow or shrink in size
# # # # # ### iterable can loop through (order from 3.6+ is in order of insertion)
# # # # # # # # can be nested - matroyshka principle
# # # # # # # # from Python 3.6 dictionaries preserve insertion order
# # #
# empty_dict = {}  # another way is with dict() compare with list which is []
# another_empty_dict = dict()
# # # # # avoid calling your variable dict  because dict is used as builtin function
# # best dictionary name would actually explain what it stores
# # for example - phonebook, user_info, etc.
# # # #
# print(empty_dict)
# print(another_empty_dict)
# # # #
# print(len(empty_dict))
# print(type(empty_dict))
# # #
# # # #
# # we can create a dictionary with some values
# tel = {'valdis': 2640, 'līga': 2911}  # create dict with 2 key-value pairs
# print(tel)
# # # adding new key-value pair
# tel['maija'] = 2653  # i add a new key-value pair to the dictionary or overwrite the old one
# print(tel)
# # # print(type(tel))
# # # #
# # # # # # this is why we use dictionaries very fast to look up
# print(tel['valdis'])  # this lookup will be very fast O(1) even with huge dictionary
# # # #
# key = "maija"  # variable key could be named anything
# print(tel[key])  # get value by key

# # # # values can be changed
# tel['valdis'] = 1188  # keys have to be unique, so here I will overwrite my old value
# print(tel)
# # # # # if I have many phones well, then I have options, how about a list?
# tel['valdis'] = [2640, 1188, 911]  # setting value to a list
# print(tel)
# print(tel['valdis'])
# print(tel['valdis'][-1], tel['valdis'][2])
# # #
# # #
# # # #
# may_phone = tel[key] # we can always save values/reference in a new variable
# print(may_phone) # once it is out no relation to dictionary
# tel['ValdisZ'] = 1001 # case sensitive keys
# tel['Valdisz'] = 1002 # case sensitive keys, not good style of course for such variables
# print(tel)
# # # # # # # # # # # # keys are unique, values can match for different keys
# tel['valdis'] = 1001
# print(tel) # so by givine new value to key we overwrote the old one
# # # # # # tel['valdis'] = [2900, 2911, 2640]
# # # # # # print(tel)
# # # # # # val_phones = tel['valdis'] # instant lookup
# # # # # # print(val_phones) # so this should be a list
# # # # # # tel['valdis'] = 2640
# # # # # # print(tel)
# tel['petēris'] = 2911
# print(tel)
# # string keys can be of any length including whitespace
# tel['visvaldis otrais pētera dēls'] = 1888
# print(tel)
# # #
# print(tel.keys(), type(tel.keys()))
# key_list = list(tel.keys()) # so i can create a list of dictionary keys
# print(key_list)  # these values are not related to dictionary keys anymore
# # # #
# # # # # # # similarly I can extract values from a dictionary
# print(tel.values(), type(tel.values()))
# value_list = list(tel.values())
# print(value_list)
# # # #
# key_list.append("rūta")
# value_list.append(1008)
# # # # of course I could have just added tel["rūta"] = 1008 directly like in the above examples
# # #
# print(key_list)
# print(value_list)
# # # # # i can create a new dictionary from two lists(iterables actually)
# key_list.append("edith")
# key_list.append("kitty")
# # however I will not add a value for edith
# print(key_list)
# # so using zip will create pairs as long as the shortest list !
# new_dict = dict(zip(key_list,value_list))
# print(new_dict)
# print(tel)
# # # #
# print(tel['valdis'])
# # print(tel['joker']) # KeyError you would have to handle errors in try: block or we could check first
# # membership test
# print('valdis' in tel) # so i check for key in my dictionary very quickly
# print('Valdis' in tel) # case sensitive so False
# print('joker' in tel)
# # #
# # # # we could use if to check for existance of key
# key = "valdis"
# key = "Nevaldis" # i am going to overwrite the above variable
# if key in tel:
#     print(f"Key {key} -> value {tel[key]}") # do something with the value
# else:
#     print("Sorry no such key", key)
# # #
# # # # turns out Python offers a get method to get the values out without if and without errors
# print(tel.get("valdis"))  # so it is just like tel["valdis"] but with error handling
# print(tel.get("NoSuchKey"))  # so if no key exists I get None back
# print(tel.get("NoSuchKey", "Sorry no such key found"))  # i can also add a default value
# print(tel.get("valdis", "Sorry no such key found"))  # i can also add a default value
# # #
# # # # I want to find out if any values have 1001 this can not be fast
# # # # because I have to check every key:value pair
# print(1001 in tel.values()) # going through values will be slow in a big dictionary, unlike keys
# # # #
# # tel[""] = "Should not work" # it but turns out it does
# # print(tel.keys())
# # print(tel[""])
# # tel["empty_string"]= "" # this is normal
# # tel["none_value"] = None # this is normal to store unknown values
# # print(tel)
# # # #
# # # # print("THe next operation will be slow in a big dictionary")
# # # # print(1001 in tel.values()) # just in keep in mind this will be slow on big dictionaries
# # # #
# # # # tel["many_values"] = 4444, 5555, "Hmmm" # this will actually be a tuple(similar to fixed list) as a value
# # # # print(tel["many_values"])
# tel["inner_dict"] = {"first phone":22222, "second phone" : 34322}  #so we can store dictionaries inside dictionaries
# print(tel)
# # # #
# # # # num_1, num_2, msg_1 = tel["many_values"] # this is tuple unpacking
# # # # print(num_1, num_2, msg_1)
# # # #
# # # # # # # # # print(tel.keys()[2]) # not possible so we need list if we need index
# # print(list(tel.keys())[2]) #  we need list if we need index
# # # #
# # # # # # # how do we handle bad keys?
# # # #
# # # # # print(tel['badkey']) # this will be an error
# # # # # my_key = "valdis"
# # # # my_key = "notarealkey"
# # # # if my_key in tel:
# # # #     print("key:", my_key, "value:", tel[my_key])
# # # # else:
# # # #     print("Couldn't find this key", my_key)
# # # #
# # # #
# # # # print(tel.get('valdis')) # so we get value by key 'valdis' similar to tel['valdis'] but without errors
# # # # print(tel.get('nevaldis'))  # default is None if not found
# # # # print(tel.get('none_value')) # here we actually get a value but it is None no way to tell without if :)
# # # # print(tel.get('valdis', "couldn't find the key")) # returns value for the key if found
# # # # print(tel.get('nevaldis', "couldn't find the key")) # or second argument if key is not found
# # # #
# # # #

# # deletion of key:value pairs
# # if we know the key we can delete the corresponding key:value pair from the dictionary
# del tel['visvaldis otrais pētera dēls']  # delet
# del tel['inner_dict']  # delete inner dictionary
# print(tel)

# # # # # # # how about looping?
# # # # #
# for key in tel: # so we can iterate over all keys in a dictionary
#     print("key:", key, "value:", tel[key], tel.get(key) )# no need for get since we are guaranteed key
# # just remember NOT to modify dictionary size(delete or add) when looping over it
# # #
# print(tel.items())  #special dict_items collection
# # # # # # # # # # # # # # iterate over all items (key->value pairs) in dictionary
# for key, value in tel.items(): # also common is k,v
#     # it is important not to modify this dictionary while we are looping over it
#     print(f"{key=}, {value=}") # this Python 3.8+ syntax good for debugging
#     print(f"key={key}, value={value}") # Python 3.6+
#     print("key=", key, "value=", value)  #older style
#     # do more stuff with each key value pair we could change values, but not keys!
# # # #
# # #

# TODO mutate dictionary while looping in a safe way

tel = {"valdis": 1001, "līga": 1002, "rūta": 9000}
print(tel)
print(tel.items())
# I can mutate/change values but not keys safely while looping
# so I will loop through all key,value pairs and adjust some values
for key, value in tel.items():
    if value < 2000: # I will get an error if value is not a numeric type
        print("small value", value, "for key", key)
        # it is okay to change a value inside loop
        tel[key] = tel[key] + 2_000_000 # also tel[key] += 2000 would work
#
print(tel)

# # # i can remove keys but should be careful to do it inside loop
# del tel['visvaldis otrais pētera dēls']
# #
# print(tel)
# #
# # # how to remove keys:value pairs inside loop?
# # 1. create a new dictionary
new_dict = {}
for key,value in tel.items():
    if type(value) is int and value > 10_000:  # so I check if value is int and if it is bigger than 2000
        # really nothing
        new_dict[key] = value # add a new pair to new dictionary

print(new_dict)
print(tel)  # we still have the original
# #
# # # 2. we can make this shorter with dictionary comprehension, similar idea to list comprehension
# dict_with_only_int_values = {key:value for key, value in tel.items() if type(value) is int}
# print(dict_with_only_int_values)  # this is a new dictionary with only int values
# # now I am sure that all values are int and I can do something with them
new_dict_2 = {key:value for key,value in tel.items() if value > 10_000}
# # # # note we can change key:value to our needs like key:value*2
print(new_dict_2)

# new_dict_3 = {key:value for key,value in tel.items() if type(value) is int and value > 2_000}
# print(new_dict_3)

new_dict_alias = new_dict # this is just an alias to the same dictionary new_dict_2

print("Dictionaries have same contents", new_dict == new_dict_2)
print("Dictionaries are actually same", new_dict is new_dict_2)  # this is false because they are different objects

# check new_dict_alias
print("Dictionaries have same contents", new_dict == new_dict_alias)
print("Dictionaries are actually same", new_dict is new_dict_alias)  # this is true because they are same object

# new_dict_4_ref = new_dict_3  #this is just a reference to the same object
# print("Dictionaries are actually same", new_dict_3 is new_dict_4_ref)  # this is true because they are the same object
# # print(tel)  # we still have the original
# #

# above approach was bottom up, we could also do top down

# # # we can change the original by looping through copy
backup = tel.copy() # just in case :) this is technically a so called shallow copy - it copies first level references
print("Dictionaries are actually same", tel is backup)  # this is false because they are different objects
print("Dictionaries have same contents", tel == backup)

# so you could loop through a copy and delete keys from original
for key,value in tel.copy().items(): # i could have gone through backup as well
    if value > 10_000:
        del tel[key] # this changes the size of original dictionary
        # tel[key+"BIGGIE"] = value*10 # i can add a new key too if i want
print(tel)  # original is changed
print(backup) # backup is not changed

# how to restore the original phone book?
tel = backup.copy() # this is a shallow copy
# alternatively i could have just used tel = backup then there is no backup

food = "kartupelis"
numbers = list(range(10))
print(food)
print(numbers)
letter_dict = dict(zip(numbers, food))
print(letter_dict)
print(letter_dict[3]) # here list would better since we have numbers in order
# so numbers as keys in a dictionary will be useful if we have a lot of sparse data
# meaning our keys do big jumps like 1000, 5000, 3425252, and so on
# if you have to store numberic from 0 to 500 you would be better off with a list

number_dict = dict(zip(food, numbers))
print(number_dict)
# in effect we have built indexes both ways


my_counter = {key:0 for key in food}  # set default value to 0
print(my_counter)

# so now I could loop through my food and adjust the counter dictionary

# #
# # # so how to adjust values in dictionary
# blank_dict = {}
# numbers = list(range(12))
# for n in numbers: # we loop through list and do something to dictionary
#     if n > 4:
#         if "over4" in blank_dict:  #there is an option called setdefault which is a bit shorter
#             blank_dict["over4"] += 1 #we increase the count by 1
#         else:
#             blank_dict["over4"] = 1   # initialize the value to 1
#     else: # 4 or less
#         if "4orless" in blank_dict:
#             blank_dict["4orless"] += 1
#         else:
#             blank_dict["4orless"] = 1

# print(blank_dict)
# #
# # for c in "my name is Valdis":
# #     if c.isalpha():
# #         print("This is a letter", c)
# #     else:
# #         print("Not a letter", c)
# #
# #
# # # we can remove from original by going through copy
# # # # # # print(tel.items())
print(tel)
# # #
# # # # # # # # # # idea to set key value pair UNLESS it is already set
del(tel["rūta"])
print(tel)

# so setdefault is a good way to set a value UNLESS it is already set
tel.setdefault("rūta", 2911)
print(tel)
tel.setdefault("rūta", 5555) # so this will not run because "rūta" is already set
print(tel)
tel.setdefault("maija", 2911)
print(tel)

# # # # in other words I save one if (it is done by Python)
# # # tel["rūta"] = 1001 # so this will always work, overwriting or not
# # # print(tel)
# # #
# # # # # tel["valdis"] = 2911 # so changing value
# # # # # print(tel)
# # #
value_to_find = 2911  # so called needle
new_dict = {} # empty dict to hold both key and value
names_with_1001 = [] # empty list to hold just the names/keys, not really needed
# # #
# # # # # so filtering for values in a dictionary
for key, value in tel.items():
    if value == value_to_find:
        print(f"Match for {value} found! The key to be added is {key}")
        new_dict[key] = value # setdefault would also work
        names_with_1001.append(key) # saving just the names in a list
# # #
print(new_dict)
print(names_with_1001, list(new_dict.keys()))

# i could do the same with a dictionary comprehension
new_dict_again = {key:value for key,value in tel.items() if value == value_to_find}
print(new_dict_again)
# print(new_dict)
# # #
# # # # # # # # # delete
# # del tel['petēris']
# # print(tel)
# # # # # del tel['petēris'] # should be KeyError
# # # # # # # no shortcut se we might want to check before deleting
# # # # if "petēris" in tel:
# # # #     print("Deleting")
# # # #     del tel['petēris']
# # # # else:
# # # #     print("Nothing to delete")
# # #
# # # # # how to delete multiple keys from dict
# bad_key_list = ["none_value", "many_values", "Valdisz", "nosuchkey","petēris", "inner_dict","empty_dict"]
# tel = backup.copy()
# for key in bad_key_list: # we are not going through our dictionary, so it is okay to delete
#     if key in tel:
#         print("Deleting", key)
#         del tel[key]
#     else:
#         print("Nothing to delete did not find", key)
# print(tel)
# # #
# # # # # # # same as below but creating a new dictionary with a filter
# # # # # so new dictionary without keys which containe "aldis"
# no_aldis_dict = {k:v for k,v in tel.items() if "aldis" not in k} # if is not required
# print("Dict comprehension", no_aldis_dict)
# # # no_aldis_dict_also = {k:tel[k] for k in tel if "aldis" not in k} # if is not required
# # # print("Dict comprehension", no_aldis_dict_also)
# # # # no_aldis_dict = {k:v*1_000 for k,v in tel.items() if "aldis" not in k} # if is not required
# # # # print("Dict comprehension", no_aldis_dict)
# # #
# # # full_dict = {k:v for k,v in tel.items()}
# # # print(full_dict) # just a copy (shallow one)
# # # print(tel == full_dict, tel is full_dict) # contents == are equal, but we have two different dictionaries
# # #
# # # # # # withotu dictionary comprehension
# # # # # # so looping and deleting we want to use copy
# # # for key in tel.copy(): # we use copy to go through if we want to delete from original
# # #     if "aldis" in key:
# # #         del tel[key] # careful here we need iterate over copy then or use dictionary comprehension
# # # print(tel)
# # #
# # # # # # # # # # # # set value for key if not set
# # # # # # tel.setdefault('pēteris', 2911)
# # # # # # # # # # # # the above will not overwrite unlike tel['pēteris'] = 2911
# # #
# dictionary update with another dictionary
tel.update({"pēteris": 2911, "valdis": 2911, "rūta": 2911})
print(tel)
popped_value = tel.pop("pēteris") # so this will remove and return the value
print(popped_value)
print(tel)

# # # # # # # # complete clearing of dictionary
tel.clear()  # IN PLACE will clear the dictionary
print(tel)
# # #
common_phone = 1888
keys = ["Valdis","Līga","Rūta", "Maija"]

for key in keys:
    tel.setdefault(key, common_phone) # could also use tel[key] = common_phone
print(tel)
# # #
# # # # # # # # dictionary comprehension to do the above loop
new_dict = {key:common_phone for key in keys}
print(new_dict)
# # #
# # # # # #how about making a dictionary of each character and their ASCII/UNICODE codes
print(ord("a"))
import string # this is a library of constants for strings
letters = string.ascii_letters
print(letters)
# # #
letter_dictionary = {k:ord(k) for k in letters }
print(letter_dictionary)
# # #
# letter_dictionary_2 = {k:ord(k) for k in "Raibi ruņči rīgā rūc"}
# print(letter_dictionary_2)
# # #
# # #
# # #
# # # import random # this should go up top generally
# # # rand_dict = {key:random.randint(10_000_000, 99_999_999) for key in keys}
# # # print(rand_dict)
# # # squares = {f"Square-{n}":n*n for n in range(10)}
# # # print(squares)
# # #
# # # # # # # # # so pop destroys key and returns its value,
# # # # # # # # # raises KeyError unless 2nd argument is given
# ede = tel.pop('Ede', "couldnt find this key")
# print(ede)
# ruta = tel.pop("Rūta", "no such key")
# print(ruta)
# # # # print(tel)
# # #
# tel.update({"Valdis":29000, "3": 500, "foo": "Bar"}) # so merging dictionaries
# print(tel)
# tel[3] = 3000 # looks like list syntax but it is not
# print(tel)
# # # # # # # # better to stick with one type of key and one data type for values if possible
# # # # # tel["emergency"] = [112,113,114,115]
# # # # # print(tel)
# # # # # # # # #
# # # # tel_alias = tel # still points to same data NOT A COPY!
# # # # print(tel is tel_alias) # so tel and tel_alias are both shortcuts to same dictionary
# # # # tel["ede"] = 9000
# # # # print(tel_alias) # so what we change in one will change in another
# # #
# # # shallow_copy = tel.copy() # this does creat a new dictionary with same values in 1st level
# # # print(shallow_copy)
# # # print(tel is shallow_copy)
# # # shallow_copy["demogorgs"] = 5000
# # # print(tel)
# # # print(shallow_copy)
# # # # tel["emergency"][3]=1188
# # # # print(tel)
# # # # print(shallow_copy)
# # # # # # # # so with shallow copy the 2nd level references stay the same
# # #
# # #
# # #
# # # # # def get_filtered_dict(in_dict, value_to_find):
# # # # #     resulting_dict = {}
# # # # #     for key, value in in_dict.items():
# # # # #         if value_to_find == value:
# # # # #         # if value_to_find in value:  # only check if there is some string in
# # # # #             resulting_dict[key] = value
# # # # #             # setdefault would also work here
# # # # #     return resulting_dict
# # #
# # # # # find_1888 = get_filtered_dict(tel, 1888)
# # # # # print(find_1888)
# # #
# # # # # def get_filtered_dict_2(in_dict, value_to_find):
# # # # #     return {k:v for k,v in in_dict.items() if v == value_to_find}
# # #
# # # # # find_1888_2 = get_filtered_dict_2(tel, 1888)
# # # # # print(find_1888_2)
# # #
# # #
# # # # # list_of_dicts = []
# # # # # for n in range(10):
# # # # #     list_of_dicts.append({"n":n,"sq":n*n})
# # # # # print(list_of_dicts)
# # #
# # # # # # # so list comprehension outside
# # # # # # # dictionary comprehension inside
# # # # # list_dicts = [{f"i{i}":i for i in range(n)} for n in range(10)]
# # # # # print(list_dicts)
# # #
# # # # tel["Valdis"] += 1 # increase the value for key Valdis by 1
# # # print(tel)