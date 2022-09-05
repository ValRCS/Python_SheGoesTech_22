# Ex. 3a
# OUT OF PLACE -
def clean_dict_value_3a(d, bad_val):
    clean_dict = {k: v for k, v in d.items() if v != bad_val}
    return clean_dict


print(clean_dict_value_3a({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 3))

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
print(my_dict)
print(clean_dict_value_3a(my_dict, 3))
print(my_dict)
new_dict = clean_dict_value_3a(my_dict, 3)
print(my_dict)
print(new_dict)


# Ex. 3b
# OUT OF PLACE
def clean_dict_values_3b(d, bad_list):
    return {k: v for k, v in d.items() if v not in bad_list}


print(clean_dict_values_3b({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, [3, 4]))

cleaned_dict = clean_dict_values_3b(my_dict, [3, 4])
print(my_dict)
print(cleaned_dict)


# IN PLACE - modifies the original dictionary
def clean_dict_values_3b_in_place(d, bad_list):
    for k, v in d.copy().items():  # careful here we need to go through copy
        if v in bad_list:
            del d[k]
    return d


cleaned_dict_in_place = clean_dict_values_3b_in_place(my_dict, [3, 4])
print(my_dict)
print(cleaned_dict_in_place)
print("Are my_dict and cleaned_dict_in_place with same contents? ", my_dict == cleaned_dict_in_place)
print("Are my_dict and cleaned_dict_in_place actually same object in  memory? ", my_dict is cleaned_dict_in_place)
