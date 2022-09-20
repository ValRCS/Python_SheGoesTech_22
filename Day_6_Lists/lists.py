# # # # # you have some similar items that you want to store
# # a1 = 3
# # a2 = 5
# # a3 = 8
# # # ...
# # a99 = 241
# # a100 = 151
# # # # # # # # # There has to be a better way
# # # #
# # # # # # # # # # # What is a list after all?
# # # # # # # # # # # * ordered
# # # # # # # # # # # * collection of arbitrary objects (anything goes in)
# # # # # # # # # # # * nested (onion principle, Matroyshka)
# # # # # # # # # # # * mutable - maināmas vērtības
# # # # # # # # # # # * dynamic - size can change
# # # # # # # # # trade_off - not the most efficient as far as memory usage goes
# # # ## for more space efficiency there are Python libraries such as numpy with ndarray structures which are based C arrays
# # #
# empty_list = []  # alternative would be empty_list = list()
# # notice the square brackets
# # in Python square brackets are often used to denote a list
# print(empty_list)  # we can add values later
# print(len(empty_list)) # should be 0
# # #
from tkinter import N


my_list = [5, 6, "Valdis", True, 3.65, "alus"]  # most common way of creating a list using [el1, el2]
print(my_list)
# print(type(my_list), len(my_list)) # prints type and length
# # #
# # #
# print(my_list[0])  # so list index starts at 0 for the first element
# # # # major difference with string is that lists are mutable
# my_list[1] = "Mr. 50"  # lists are mutable (unlike strings) types inside also will change on the run
# print(my_list)
# drink = my_list[-1]  # last element
# print(my_list[-1], drink, my_list[5])  # again like in string we have indexes in both directions
# # #
# # # # typically we do not need an index for items when looping
# for el in my_list:
#     print(el, "is type", type(el))
# # # # Pythonic way to show index is to enumerate
# for i, el in enumerate(my_list):  # if we need index , default start is 0
#     print(i, el, "is type", type(el))
#     print(f"Item no. {i} is {el}")
# # #
# # # # i can start index at some value
# for i,el in enumerate(my_list, start=1000): # if we need index to start at some number
#     print(f"Item no. {i} is {el}")
# # #

# # list_2d = list(enumerate(my_list, start=100))
# # print(list_2d) # this will be a two, dimensional list, list containing lists
# # #
# # typical is to use plural for lists
# numbers = list(range(10)) # range is not a list it used to be in Python 2.7, it is ready on demand
# print(numbers)
# # #
# # # print(len(my_list))
# for i in range(len(my_list)): # this way is not encouraged, this is too C like, no need for this style
#     print(f"Item no. {i} is {my_list[i]}")

# drinks = ["water", "juice", "coffee", "tea", "milk", "beer"]
# # # idioms
# for drink in drinks:  # list in plural item in singular
#     print(drink)
# # #
# # # List slicing - we can use it to get a part of the list
# print(my_list[:3]) # so we only print the first 3 elements from the list
# print(drinks[:3]) # so we only print the first 3 elements from the list
# print(my_list[-2:]) # last two
# print(drinks[-2:]) # last two
# print(my_list[1:4]) # from the second to the fourth, fifth is not included
# print(drinks[1:4]) # from the second to the fourth, fifth is not included
# print( my_list[1:-1]) # from the second to the last but one
# print(my_list[::2]) # jumping over every 2nd one
# my_numbers = list(range(100,200,10)) # no 0 lidz 9, also shows how to create a list from another sequence like object
# print(my_numbers)
# print(numbers)
# print(numbers[::2])  # evens starting with 0, since we jump to every 2nd one
# print(numbers[1::2])  # so odd numbers here, but realy odd indexes
# print(my_numbers[::2]) # even starting with 100, 120, 140, 160, 180
# print(my_numbers[1::2]) # all odd indexed numbers, index 1, 3, 5, 7 so 110, 130, 150, 170, 190
# # # # # # print(my_list[1::2]) # start with 2nd element and then take every 2nd element
# # # # print(my_list[-1], my_list[len(my_list)-1]) # last element, we use the short syntax
# # print(my_numbers[::-1])
# print(my_list[::-1])
# print(numbers[::-1])
# print(my_numbers[::-1])

# # for iterating over large lists in reverse order we can use reversed() function
# print(reversed(numbers)) # this we would use when we do not need the list completely for looping
# # # # why would you use such a construction
# # # # because you do not want to create a new list in memory, you want to use the original
# for n in reversed(numbers):  # this is more efficient than numbers[::-1] because we do not create a new list in memory
#     print(n)
# # # print(list(reversed(numbers)))
# # my_reversed_numbers = my_numbers[::-1]
# # print(my_reversed_numbers)
# # # # # # print(reversed(my_list)) # returns an iterator - so not a list but sort of prepared to list collection
# # # # # # print(list(reversed(my_list))) # so we need to cast it to list
# # # # # # print(my_list[::-1]) # so same as above when used on a list
# # # # empty_list = []  # more common
# # # also_empty_list = list()
# # # print(empty_list, also_empty_list)
# food = "kartupelis"  # kartupelis is a potato in Latvian
# print(food)
# food_chars = list(food) # so type casing just like str, int, float, bool etc
# # list will work with any sequence type - and str is a sequence type
# print(food_chars)
# print("OLD and TIRED", food_chars[5])
# food_chars[5] = "m"  # so replacing the 6th elemen - in this case a letter p with m
# print("NEW and FRESH", food_chars[5])
# print(food_chars)
# maybe_food = str(food_chars) # not quite what we want, but it is a string
# print(maybe_food) # just a string of what printing a list would look like
# # # so maybe_food is a string, but it is not a list anymore
# food_again = "".join(food_chars) # "" shows what we are putting between each character, in this case nothing
# print(food_again)
# food_again_with_space = " ".join(food_chars) # "" shows what we are putting between each character
# print(food_again_with_space)
# food_again_with_smile = "**😁**".join(food_chars) # "" shows what we are putting between each character
# print(food_again_with_smile)
# small_list = ["Valdis", "likes", "beer"]
# separator = "==="
# new_text = separator.join(small_list)
# print(new_text)
# # num_string = "||".join(numbers) # we will need to convert numbers to theri str representation
# # print(num_string)
# # we can solve the above with list comprehension - to be seen later on

# # # # # print(list("kartupelis")) # can create a list out of string
# print("kartupelis".split("p")) # i could split string by something
# sentence = "A quick brown fox jumped \t\t over    a sleeping dog"
# print(sentence)  # string
# words = sentence.split()  # we split by some character in this case whitespace
# print(words) # list with words
# print(sentence.split(" ")) # same as above, but strictly splitting by single space
# words[3] = "bear"
# print(words)
# back_to_sentence = " ".join(words) # so we join the list back into a string
# print(back_to_sentence)

# # TODO explore more list methods
## FIXME for bugs and errors
## TODO for things to do

# #
# # sentence_with_exclams = ".!.".join(words)
# # print(sentence_with_exclams)
# # # # # # # # # # how to check for existance in list
# print(my_list)
# membership check for list
print("3.65 is in my list?", 3.65 in my_list)
print(66 in my_list)
print("Valdis" in my_list)
print(my_list[2]) # Valdis
print("al" in "Valdis", "al" in my_list[2])
print("al" in my_list)  # this is false,because in needs a exact match, to get partial we need to go deeper
# # # # # # # # # # # # iterate over items
print("*"*20)
for it in my_list:
    print(it)
# # #
## looking for a needle in a haystack
# idiomatic way to check for existance
needle = "al" # what we want to find in our list
for item in my_list:
    print("Checking ", item)
    if type(item) == str and needle in item: # not all types have in operator
        print(f"Found {needle=} in {item=}") # python 3.8 and up, good for debuggin
        print(f"Found needle={needle} in item={item}") # for python 3.7
# # #
# # # # # # # # # # # #
## adding/appending items to list
# # # # # # # # my_list.append()
# my_list.
my_list.append("Bauskas alus") # adds "Bauskas alus" at the end of my_list
my_list.append("Valmiermuižas alus")  # IN PLACE methods, means we modify the list
print(my_list)

# compare to OUT OF PLACE + 
another_list = my_list + ["Alus", "Vīns", "Šokolāde"] # this is not in place, we create a new list
print(my_list)
print(another_list)

# # #
# # # # # # # # # # example how to filter something
# find_list = [] # so we have an empty list in beginning
# needle = "al"
# for item in my_list: # i can reuse item in the loop
#     # if needle in item: will not work because we have non strings in list
#     if type(item) == str and needle in item:
#         print(f"Found {needle=} in {item=}")
#         find_list.append(item)
# print(f"{needle=} found in {find_list=}")
# # # # # # # # # # ps the above could be done simpler with list comprehension
# # #
# # # # # # # # # # # # out of place meaning find_list stays the same
# new_list = my_list + ["Kalējs", "Audējs"] # OUT OF PLACE addition, my_list is not modified
# print(len(new_list), len(my_list))
# print(my_list)
# print(new_list)
# # #
# new_list += ["Malējs", "Salīgais"] # shorthand for new_list = new_list + [new items ] so flattened
# print(new_list)
# new_list.append(["Svarīgais", "Mazais"]) #notice append added a list a s nested
# print(new_list) # notice that we have a list in the list
# print(new_list[-1])
# print(new_list[-1][-1], new_list[-1][1]) # in this case for size 2 1 and -1 give same results

# using append to add multiple items will produce a nested list
my_list.append(["Svarīgais", "Mazais"]) #notice append added a list a s nested
print(my_list) # notice that we have a list in the list
print(my_list[-1]) # negative index means we start from the end
print(my_list[8]) # positive index means we start from the beginning
# to get last item of nested list
print(my_list[-1][-1], my_list[-1][1]) # in this case for size 2 1 and -1 give same results
# if you want to keep your list flat you use extend
my_list.extend(["Fantastiskais", "Lapsa"]) # very similar to += IN PLACE
print(my_list)

my_list.remove(6) # Again IN PLACE, removes somethign from my_list
print(my_list)
my_list.remove(5) # removes first occurence of 5
print(my_list)
my_list.remove(['Svarīgais', 'Mazais'])
print(my_list)
# so how to remove last item from list?
# we could use remove 
# alternative we could use OUT OF PLACE slicing
my_list = my_list[:-1] # this is OUT OF PLACE, we create a new list overwriting old one
print(my_list)

# get rid of first three items from list
my_list = my_list[3:] # this is OUT OF PLACE, we create a new list overwriting old one
print(my_list)
# # #
# # # # print(f"{str(my_list)}") # not quite what we want
# # # # # # # how to convert all values to str
# str_list = []
# for item in my_list:
#     str_list.append(str(item)) # so if item is already string nothing will happen
# print(str_list)
# # #
# number_str_list = []
# for num in numbers:
#     number_str_list.append(str(num))
# print(numbers) # list of integers
# print(number_str_list) # a list of strings
# #
# number_string = ",".join(number_str_list)
# print(number_string)
# # # i can go in reverse as well
# numbers_deconstructed = number_string.split(",")
# print(numbers_deconstructed)
# #
# # my_numbers = []
# # for it in numbers_deconstructed:
# #     my_numbers.append(int(it))
# # print(my_numbers)
# #
# #
# #
numbers = list(range(1, 11))
print(numbers)
# how could I get squares from numbers? and save them in a list?
squares = []
for num in numbers: # numbers could have been range(1,11) as well
    squares.append(num**2) # so we are squaring each number and appending to squares
print(squares)

# so it is very typical to start with a blank list and then append to it
# by going through some other list or some other iterable(string, and other iterables)

# # # # # # # # # # # list comprehensions make it even shorter
also_squared = [num**2 for num in numbers] # so we are squaring each number and appending to squares
print(also_squared)

# if you only wanted odd squares what would you do?
odd_squared = [num**2 for num in numbers if num % 2 == 1] # so we are squaring each number and appending to squares
# so list comprehensions are very similar to for loops
# how would we do this with a for loop?
odd_squared_also = []
for num in numbers:
    if num % 2 == 1:
        odd_squared_also.append(num**2)

print(odd_squared)
print(odd_squared_also)

odd_numbers = [num for num in numbers if num % 2 == 1]
print(odd_numbers)

numbers_copy = [num for num in numbers] # so we are copying numbers to numbers_copy
print(numbers_copy)
# above is rarely seen, but it is possible
# because we have a common copy method
numbers_copy_also = numbers.copy() # so we are copying numbers to numbers_copy
print(numbers_copy_also)

# this is different than just using a variable to a list
# NOT A COPY!
numbers_alias = numbers # so we are aliasing numbers to numbers_alias

numbers[4] = 100
# so if we change numbers, numbers_alias will change as well
print(numbers)
print(numbers_alias)
print(numbers is numbers_alias) # so they are the same object

# notice how numbers_copy remains the same
print(numbers_copy)
print(numbers_copy is numbers) # so they are different objects

# == compares contents for lists!
print(numbers_copy_also == numbers_copy)
# however
print(numbers_copy_also is numbers_copy) # False because not the same objects!

numbers.append(42)
numbers.append(4)
print(numbers)
print(numbers.count(4)) # how many times 4 is in numbers

print(numbers.index(42)) # what is the first index of 42 in numbers

numbers.insert(2, 50) # insert 50 at index 2
# this will push everything to the right, could be expensive in a large list 
print(numbers)

last_item = numbers.pop() # removes last item from list and returns it
# pop will give you an error if list is empty
print(last_item)
print(numbers)
# pop and append go together
numbers.append(last_item)
print(numbers)

numbers.reverse() # IN PLACE
print(numbers)
# could use OUT OF PLACE reverse
numbers = numbers[::-1] # OUT OF PLACE
print(numbers) # back to original

# OUT OF PLACE sort 
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers) # original list is not changed

# we can sum, min and max on a list of same data types
print(sum(numbers))
print(min(numbers))
print(max(numbers))

# IN PLACE sort
numbers.sort()
print(numbers) # original list is changed and can not be retrieved

# finally we can clear the list in place
numbers.clear() # IN PLACE clears the list!
print(numbers)

# so when should you use list comprehensions and when should you use for loops?
# for loops are more flexible, you can do more things with them
# use for loops when you have more complex logic

# # print(my_list)
# str_list_2 = [str(item) for item in my_list]  # so i go through each item and make a new list with string versions of all items
# print(str_list_2)
# # #
# square_list = []
# for n in range(10):
#     square_list.append(n**2)
# print(square_list)

# # list comprehension example of square_list
# squares = [n**2 for n in my_numbers] # a new list with squares of original numbers
# print(squares)
# # # wierd_squares = [n*n or 9000 for n in my_numbers] # we could utilie or for 0
# # # print(wierd_squares)
# #
# # list comprehension can serve as a filter
# just_numbers = [1,5,2,2,5,7,9,1,5,11,10]
# odd_numbers = [n for n in just_numbers if n%2 == 1]
# print(odd_numbers)
# #
# print(numbers)
# odd_squares = [n*n for n in numbers if n%2 == 1]
# print(odd_squares)
# #
# # # same idea as above
# # odd_squares_also = []
# # for n in my_numbers:
# #     if n%2 == 1:
# #         odd_squares_also.append(n*n)
# #         # advantage of long approach is that here we can do more stuff,print etc
# # print(odd_squares_also)
# #
# print(str_list)
# print(str_list_2)
# # #
# print("Lists have equal values inside?",str_list == str_list_2) # check if lists contain equal values
# print("Lists are physically same?", str_list is str_list_2) # check if our variables reference the same list
# str_list_3 = str_list # so str_list_3 is a shortcut to same values as, NOT A COPY!
# print(str_list == str_list_3, str_list is str_list_3)
# str_list_copy = str_list.copy() # create a new list with same values
# print(str_list == str_list_copy, str_list is str_list_copy)
# print(id(str_list))
# print(id(str_list_3))
# print(id(str_list_copy))
# # #
# print(needle)
# # # # # # # # need needle of course
# # # # # so i can add if as filter to list comprehension
# beer_list = [item for item in str_list if needle in item]
# print(beer_list)
# beer_list = beer_list[1:] #get rid of Valdis (first element with index 0) in my beer list
# print(beer_list)
# # #
# beer_list += ["Užavas alus"] # we create a list on demand - list literal beer_list = beer_list + ["Užavas alus"]
# # # # # # similar to beer_list.append("Užavas alus")
# # print(beer_list)
# # #
# # # # # squares = [num*num for num in range(10)] # so we come up with num on the spot
# # # # # print(squares)
# # # # squares_matrix = [[num, "squared", num*num] for num in range(10)]
# # # # print(squares_matrix) # so list of lists (2d array basically)
# # # # print(squares_matrix[9][2], squares_matrix[-1][-1])
# # #
# # beer_list += ["Malējs"]  # same as new_list = new_list + ["Malējs"]
# # # # # # # new_list
# # #
# print(beer_list[-1])
# print(beer_list)
# last_beer = beer_list[-1]
# print(last_beer)
# print(beer_list)
# # beer_list = beer_list[:-1] #so i get rid of last element
# # print(last_beer, beer_list)
# beer_list.append("Malējs")
# print(beer_list)
# last_beer = beer_list.pop()  # also IN PLACE meaning i destroyed the last value
# print(last_beer, beer_list)

# beer_list.reverse() # so i reverse the list IN PLACE
# print(beer_list)
# beer_list.reverse() # so i reverse the list IN PLACE
# print(beer_list)
# # #
# # # # # # print(f"We took out {last_beer}")
# # # # # # print(beer_list)
# # # # # # beer_list.append(last_beer)
# # # # # # print(beer_list)
# # #
# beer_count = 0
# for el in beer_list:
#     if "alus" in el:
#     # if "alus" == el: # so count will be for exact matches
#         beer_count += 1
# print(beer_count)
# # #
# # # # # # so above count can be done with count method
# print(beer_list.count("alus")) # only exact matches
# print(beer_list.index("alus")) # will be 0 since we start counting with 0
# # # # print(beer_list.find("Mālenīetis")) # find does not exist for lists, unlike string
# beer_list.extend(["Labietis", "Mālpils alus"]) # again in place similar to +=
# print(beer_list)
# print(beer_list.index("Mālpils alus"))
# # beer_with_zh = [el for el in beer_list if "ža" in el]
# # print(beer_with_zh)
# # # # # print(len(beer_with_zh))
# # # # # beer_in_description = [el for el in beer_list if "alus" in el]
# # # # # print(beer_in_description)
# # # # # # has_alus_count = len([el for el in beer_list if "alus" in el])
# # # # # # print(has_alus_count)
# # #
# beer_list.insert(2, "Cēsu sula") # so it will insert BEFORE index 2 (meaning before 3rd element)
# print(beer_list)
# beer_list.insert(5, "Cēsu sula") # in general we want append instead of insert for speed
# print(beer_list)
# beer_list.remove("Cēsu sula") # removes first occurance IN PLACE
# print(beer_list)
# # # we could keep removing, but easier is to use a list comprehension to make a new list
# clean_beers = [el for el in beer_list if el != "Cēsu sula"]
# print(clean_beers)
# #
# # while "Cēsu sula" in beer_list.copy(): # careful with looping and changing element size
# #     print("found Cēsu sula")
# #     beer_list.remove("Cēsu sula")
# # # print(beer_list)
# # #
# # # # # # # # # # beer_list.remove("Cēsu sula") # again in place first match
# # # # # # # # # # print(beer_list)
# # # # # # # # # # beer_list.remove("alus")
# # # # # # # # # # print(beer_list)
# # # # # # # # # # beer_list.remove("alus")
# # # # # # # # # # print(beer_list)
# # #
# # # beer_list.reverse() # in place reversal
# # # print(beer_list)
# new_beer_list = beer_list[::-1]  # so i save the reversed list but keep the original
# print(new_beer_list)
# # #
# # # # # # # # # # # so if we have comparable data types inside (so same types)
# new_beer_list.sort() # in place sort, modifies existing
# print(new_beer_list)
# # num_list = [1,2,3,0, -5.5, 2.7, True, False, 0.5, 0] # we can compare int, float and bool
# # print(num_list)
# # print(num_list.sort()) # returns None! because IN PLACE
# # print(num_list)
# # #
# # # sorted_by_len = sorted(new_beer_list, key=len) # out of place meaning returns new list
# # # print(sorted_by_len)
# # # # # # sorted_by_len_rev = sorted(new_beer_list, key=len, reverse=True) # out of place meaning returns new list
# # # # # # print(sorted_by_len_rev)
# # # # # # print( min(beer_list), max(beer_list)) # by alphabet
# # #
# numbers = [1, 4, -5, 3.16, 10, 9000, 5]
# print(min(numbers),max(numbers), sum(numbers), sum(numbers)/len(numbers))
# my_sorted_numbers = sorted(numbers)  # OUT OF PLACE sort we need to save it in new variable
# print(my_sorted_numbers)
# # # avg = round(sum(numbers)/len(numbers), 2)
# # # print(avg)
# # #
# # saved_sort_asc = sorted(numbers)  # out of place does not modify numbers
# # print(saved_sort_asc)
# # # # # # # # # # # sorted(numbers, reverse=True)  # out of place does not modify numbers
# # # # # # print(numbers)
# # # # # # print(numbers.sort()) # in place meaning it modifies the numbers
# # # # # # print(numbers)
# # # # # # # # # # # numbers.remove(9000)  # will remove in place first 9000 found in the list
# # # # # # # # # # # numbers
# # # # # # # # # # # min(numbers), max(numbers)
# # # # print(sum(my_numbers), min(my_numbers), max(my_numbers))
# # # # # # # # # # our own sum
# # # # total = 0
# # # # for n in my_numbers:
# # # #     total += n
# # # #     # useful if we want to do more stuff with individual elements in list
# # # # print(total)
# # #
# # # # # sentence = "Quick brown fox jumped   over a    sleeping dog"
# # # # # words = sentence.split() # default split is by whitespace convert into a list of words
# # # # # print(words)
# # # # # words[2] = "bear" # i can a modify a list
# # # # # print(words)
# # # # # # # # # # # so str(words) will not work exactly so we need something else
# # # # # print(str(words)) # not what we want)
# # # # # new_sentence = " ".join(words) # we will lose any double or triple whitespace
# # # # # print(new_sentence)
# # # # # compressed_sent = "".join(words) # all words together
# # # # # print(compressed_sent)
# # # # # funky_sentence = "*:*".join(words) # we will lose any double or triple whitespace
# # # # # print(funky_sentence)
# # #
# # # # # # # # # # # we can create a list of letters
# # # # # food = "kartupelis"
# # # # # letters = list(food)  # list with all letters
# # # # # print(letters)
# # # # # letters[5] = "m"
# # # # # new_word = "".join(letters) # we join by nothing so no spaces in the new word
# # # # # print(new_word)
# # #
# # # print(words)
# # # new_list = []
# # # for word in words:
# # #     new_list.append(word.capitalize())
# # # print(new_list)
# # # # # # # # # # # # list comprehension same as above
# # # new_list_2 = [w.capitalize() for w in words]
# # # print(new_list_2)
# # # # # filtered_list = [w for w in words if w.startswith("b")]
# # # # # print(filtered_list)
# # # # # filtered_list = [w.upper() for w in words if w.startswith("b")]
# # # # # print(filtered_list)
# # # # # # # # # # # filtered_list_2 = [w for w in words if w[0] == "b"]
# # # # # # # # # # # filtered_list_2
# # # # # # # # # # # filtered_list_3 = [w.upper() for w in words if w[0] == "b"]
# # # # # # # # # # filtered_list_3
# # #
# # # # # print("Hello")
# # #
# # # # # # # # # # numbers = list(range(10)) # we cast to list our range object
# # # # # # # # # # print(numbers)
# # # # # squares = []
# # # # # for n in range(10):  # could also use range(10)
# # # # #     squares.append(n*n)
# # # # # print(squares)
# # # # # squares_2 = [n*n for n in range(10)] # list comprehension of the above
# # # # # print(squares_2)
# # # # # even_squares = [n*n for n in range(10) if n % 2 == 0]
# # # # # print(even_squares)
# # #
# # # # # # # # # # print("Whew we need a beer now don't we ?")
# # #
# # # # # # # # # # # food
# # # # # # print(food)
# # # # # # char_codes = [ord(c) for c in food]
# # # # # # print(char_codes)
# # # # # # char_codes_list = [[f"Char:{c}", ord(c)] for c in food]
# # # # # # print(char_codes_list)
# # # # # # # # # # # print(char_codes_list[0])
# # # # # # # # # # # print(char_codes_list[0][0])
# # # # # # # # # # # print(char_codes_list[-1])
# # # # # # # # # # # print(char_codes_list[-1][-1])
# # # # # # # # # so list of lists of characters
# # # # # # # # chars = [[c for c in list(word)] for word in sentence.split()]
# # # # # # # # print(chars)
# #
