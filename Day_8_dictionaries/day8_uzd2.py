# IN PLACE - meaning we change the original dictionary
def replace_dict_value(d, bad_val, good_val):
    for key, value in d.items():
        if value == bad_val:
            d[key] = good_val
    return d


my_dict = {'a': 5, 'b': 6, 'c': 5, 'd': 6}

print(my_dict, "->", replace_dict_value(my_dict, 5, 10))


# OUT OF PLACE - meaning we create a new dictionary
def replace_dict_value_out_of_place(d, bad_val, good_val):
    new_dict = {}
    for key, value in d.items():
        if value == bad_val:
            new_dict[key] = good_val
        else:
            new_dict[key] = value
    return new_dict


print(my_dict, "->", replace_dict_value_out_of_place(my_dict, 10, 25))


# OUT OF PLACE with dictionary comprehension
# Ex. 2
def replace_dict_value_2b(d, bad_val, good_val):
    return {k: (v if v != bad_val else good_val) for k, v in d.items()}


print(my_dict, "->", replace_dict_value_2b(my_dict, 10, 25))
print(my_dict) # still the same dictionary
new_dict = replace_dict_value_2b(my_dict, 10, 25)
print(my_dict, new_dict) # now the new dictionary is different from the original one
