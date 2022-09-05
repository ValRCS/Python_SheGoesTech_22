# def clean_dict_value(b, dzest):
#     key_list = list(b.keys())
#     value_list = list(b.values())
#     gala_list = []
#     gala_list2 = []
# #    print(key_list)
# #    print(value_list)
#     for i in range(0,len(b)):
#          if value_list[i] != dzest:
#             gala_list.append(key_list[i])
#             gala_list2.append(value_list[i])
#             #print(gala_list)
#             #print(gala_list2)
#     dict_new = dict(zip(gala_list, gala_list2))
#     return dict_new

# def clean_dict_value_3a(d, bad_val):
#     new_d = dict()
#     for k in d:  #idiomatic/typical way to loop through a dictionary
#         if d[k] != bad_val:
#             new_d[k] = d[k]  # so here we add with good key: value pair to the new dictionary
#     return new_d

# dictionary comprehension of the above
def clean_dict_value_3a(d, bad_val):
    return {k: v for k, v in d.items() if v != bad_val}


dict2 = {'a': 5, 'b': 10, 'c': 15, 'd': 20, 'e': 25, 'f': 10}
dict_new = clean_dict_value_3a(dict2, 10)
print(dict2)
print(dict_new)

dict2 = clean_dict_value_3a(dict2, 10)  # so we could simply overwrite the reference to original dictionary
# if nothing else references the original, it will be so called garbage collected
print(dict2)


# def clean_dict_values_3b(d, v_list):
#     new_d = dict()
#     for k in d:
#         if d[k] not in v_list:
#             new_d[k] = d[k]
#         # isGood = True
#         # for list_item in v_list:
#         #     if d[k] == list_item:
#         #         isGood = False
#         # if isGood:
#         #     new_d[k] = d[k]
#     return new_d

def clean_dict_values_3b(d, bad_list):
    return {k: v for k, v in d.items() if v not in bad_list}


print(clean_dict_values_3b({'a': 5, 'b': 6, 'c': 5, 'd': 3}, [3, 4, 5]))

# print(clean_dict_values_3b({'a': 5, 'b': 6, 'c': 5, 'd': 3}, [3, 4, 5]))

# in place approach
dict2 = {'a': 5, 'b': 10, 'c': 15, 'd': 20, 'e': 25, 'f': 10}


def clean_dict_values_inplace(d, bad_list):
    for k in d.copy():
        if d[k] in bad_list:
            del d[k]
    return d  # so for inplace I do not even need return, because I change the original


print(dict2)
# in place i do not need the new return actually
clean_dict_values_inplace(dict2, bad_list=[3, 4, 5, 20])
print(dict2)
