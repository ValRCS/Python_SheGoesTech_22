# # 1. What's the frequency?

# Write a function: get_char_count(text) that receives a string and returns a dictionary with the number of single letter counts.

# get_char_count("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, ' ': 1} 

# # dictionary sequence doesn't matter and the whole alphabet doesn't have to be included

#  There may also be a solution with Counter from standard Python library but this is definitely not necessary, although it is very elegant smile

# def get_char_count(text):
#     new_dict = {}
#     for i in text:
#         letter_count = text.count(i) # this approach is not optimal, but it works
#         # the problem with count is that it has a hidden loop inside
#         new_dict[i] = letter_count
#     return new_dict

# more optimal approac
def get_char_count(text):
    my_counter = {}
    for c in text: # just a single loop
        if c in my_counter:
            my_counter[c] += 1 # this is constant time operation
        else:
            my_counter[c] = 1 # this is constant time operation
    return my_counter

# get_char_count("hubba bubba")

print(get_char_count("hubba bubba"))
print(get_char_count("Valdis and his friends and family"))

# above approach is so popular that we have a special data structure for it
# called Counter from collections module
# python Collections module is a built-in module that implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.
# https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter # generally we import all modules at the top of the file
my_counter = Counter("hubba bubba")
print(my_counter)
print(type(my_counter)) # Counter is a dictionary subclass, dictionary with some extra benefits :)
regular_dict = dict(my_counter) # we can convert it back to regular dictionary
print(regular_dict)
# Counter provides a lot of useful methods
valdis_counter = Counter("Valdis and his friends and family")
print(valdis_counter)
print(valdis_counter.most_common(3)) # most common 3 elements
print(valdis_counter.total()) # total number of elements counted

# we can count words as well
print(Counter("Valdis and his friends and family".split())) # split gave us a list of words
my_list = ["Apple", "Apple", "Apple", "Orange", "Orange", "Banana", "Banana", "Peach","Banana", "Banana", "Banana"]
fruit_counter = Counter(my_list)
print(fruit_counter)
number_list = [1, 2, 3, 4, 5, 6, 3, 70, 8, 9, 10, 1, 2, 3, 54, 5, 6, 7, 8, 9, 10]
print(Counter(number_list))

