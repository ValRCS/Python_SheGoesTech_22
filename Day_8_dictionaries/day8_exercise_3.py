# # 3. Dictionary cleaner



# 3a. Write clean_dict_value(d, bad_val), which returns a cleaned dictionary without any keys with the value bad_val

# The parameters of the function are the dictionary d to be processed and the value bad_val to be disposed of together with its key.

# Example:

# clean_dict_value ({'a': 5, 'b': 6, 'c': 5}, 5) -> {'b': 6}, because 5 was a value for both a and c keys to get rid of.



# 3b Write clean_dict_values ​​(d, v_list), which returns a cleaned dictionary

# The parameters of the function are the dictionary d to be processed and the list of values ​​v_list to get rid of.

# clean_dict_values ​​({'a': 5, 'b': 6, 'c': 5, 'd':3}, [3,4,5]) -> {'b': 6} because 3 and 5 were in the list of values to delete.



# PS. Remember we can use del d['a'] only if the key 'a' exists.

# !! When resizing a dictionary, we are not allowed to iterate at the same time!


# There are two options: either walk through the copy my_dict.copy.items(), or build a new dictionary. 
# Dictionary comprehension would be one option.

# OUT OF PLACE function, it returns a new dictionary, old one is not changed
def clean_dict_value(d, bad_val):
    new_dict = {}
    for key, value in d.items():
        if value != bad_val:
            new_dict[key] = value
    return new_dict

print(clean_dict_value({'a': 5, 'b': 6, 'c': 5}, 5)) 

my_dict = {'a': 5, 'b': 6, 'c': 5, 'd':3, 'e': 5, 'f': 5, 'g':8}	
new_dict = clean_dict_value(my_dict, 5)
print(new_dict)
print(my_dict)

# you can also use dictionary comprehension, STILL OUT OF PLACE
def clean_dict_value_2(d, bad_val):
    return {key: value for key, value in d.items() if value != bad_val}

also_new_dict = clean_dict_value_2(my_dict, 5)
print(also_new_dict)
print(my_dict)

# TODO 3b clean dict values from list