# 2 exercise
def replace_dict_value(d, bad_val, good_val):
    print(d)
    for key, value in d.items():
        if value == bad_val:
            d[key] = good_val # so this is the version where we modify the original IN PLACE
    print(d)
    return d # returns the original dictionaly

my_dict = {'a': 5, 'b': 6, 'c': 5}
print(my_dict)
new_dict = replace_dict_value(my_dict, 5, 12)
print(new_dict)
print(my_dict)
print("dictionaries are the same dictionary in fact", my_dict is new_dict)  # is it the same one ?