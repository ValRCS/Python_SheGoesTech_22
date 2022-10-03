# # # # # # # using Python standard library
# # # # # # # https://docs.python.org/3/library/
# # # # # # # Extensive - Batteries Included - just import!
# # # # # # # Available across most OSes
# #
# # # # # # # 4 ways of importing modules
# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.today())
from datetime import datetime as dt  # datetime has datetime submodule!
# print(dt.now()) # we using renamed datetime as dt
# from datetime import datetime
# print(datetime.now()) # we are using the original datetime
# print(datetime.now().year)
import string # mostly useful constants
# print(string.ascii_letters)
# print(string.digits)
import math
# # # # # # # import math as mth # Python likes these short names but not for standard library!
# print(math.cos(3.1415926), math.sin(math.pi), math.pi)
# from math import floor # i could import floor alone but beware name collission
# print(floor(3.15)) # we could have used int here instead, TODO is there different between floor and int?
# # so floor will be different from int if we have a negative number
# print(floor(-3.15), int(-3.15)) # so floor rounds down and int rounds to nearest integer
# from math import factorial as fact # in math it is !
# print(fact(5)) # so 5! = 5*4*3*2*1 = 120
# from collections import Counter # so i only want Counter from collections package
from statistics import mean
from statistics import median
from statistics import mode
from statistics import pstdev
from statistics import stdev
# mylist = [1,2,3,10,4,5,6,7,8,9,10]
# print(mean(mylist), median(mylist), mode(mylist), pstdev(mylist), stdev(mylist)) # so pstdev is population standard deviation
import random
# random_list = [random.randint(1,100) for _ in range(10_000)] # so i am creating a list of 20 random integers between 1 and 100
# # print statistics of random_list
# print(mean(random_list), median(random_list), mode(random_list), pstdev(random_list), stdev(random_list))

import itertools
# permutations
# so permutations is a generator that will generate all possible permutations of a list
# my_permutations = list( itertools.permutations([1,2,3,4]))
# print(my_permutations)
# # combinations
# # so combinations is a generator that will generate all possible combinations of a list
# # so in combinations order does not matter
# # wiki for combinations https://en.wikipedia.org/wiki/Combination
# my_combinations = list( itertools.combinations([1,2,3,4], 2))
# print(my_combinations)
# # product
# # so product is a generator that will generate all possible products of a list
# # so in product order does matter
# # wiki for product https://en.wikipedia.org/wiki/Product_(mathematics)
# my_products = list( itertools.product([1,2,3,4], "Val"))
# print(my_products) # should be 16 items

# all of the above you could write some loops and do  yourself but itertools is more efficient

# #
# # # import mat_lib # this library comes from my own PYTHONPATH
# #
# # # print(mat_lib.add(3,76))
# #
# # # print(string.punctuation)
# throws = 100_000
# # before = datetime.datetime.now() # now() is a method of datetime class from datetime module
# before = dt.now()
# print(before)
# # for i in range(100_000):
# #     t = i*3
# rand_dice = [random.randint(1, 6) for _ in range(throws)]  # _ because we do not need the variable
# after = dt.now()  # now() returns a datetime object
# print(after)
# delta = after - before  # so this means time oject have __sub__ overloaded
# print(delta)
# #
# print("Average of throws", sum(rand_dice) / throws)
# print(mean(rand_dice))  # mean is from statistics import mean
# # print(after)
# # delta = after - before # so this means time oject have __sub__ overloaded
# print(delta)
# print("Just seconds and microseconds of delta", delta.seconds, delta.microseconds)
# print(after.year, after.month, after.day, after.weekday(), after.hour, after.minute, after.second, after.microsecond)
# # https://stackoverflow.com/questions/8380389/how-to-get-day-name-from-datetime
# print(dt.today().strftime("%A"))  # today returns a date object
# print(after.strftime("%A"))
# print(dt.now().time())
# print(string.ascii_lowercase)
# print(string.digits)
# print(string.punctuation)
# print(math.factorial(5))
# # # # # # print(mth.factorial(4))
# print(floor(3.98))
# print(fact(6))
# my_count = Counter("abracadabra")
# print(my_count)  # this will be dictionary
# print(my_count.most_common())
# print(my_count.most_common(3))
# # # print(my_count.keys())
# # # print(list(my_count.keys()))
# # # print(my_count.values())
# # #
# # # # # # # # # print(type(my_count.most_common()))
# # # # # # # # print(my_count['a'])
# a simple way of timing something
dice_throws = 100_000
beg = dt.now()
# print(beg)  # print takes time by itself so measurement will be imprecise
ran_nums = [random.randint(1, 6)+random.randint(1, 6)
            for _ in range(dice_throws)]
end = dt.now()
print(beg)

print(end)
print(f"Took {end-beg} seconds")
# print(sum(ran_nums)/len(ran_nums))
# print(mean(ran_nums))
# # # # so i put all the throws in buckets (presumably from 2 to 12)
# num_count = Counter(ran_nums)
# print(num_count.most_common())
# #
# first = "ABC"
# second = "01234"
# third = ['ābols','bumbieris']
# cartesian_product = list(itertools.product(first, second))  # so like double loop for all x all
# print(cartesian_product)
# # i can create product from all the above
# another_cartesian_product = list(itertools.product(first, second, third))
# print(another_cartesian_product)


# #
numbers = list(range(10))
# so sample will give you a random sample of the list without replacement - meaning uniques
new_shuffled = random.sample(numbers, len(numbers))
print("Sample: no duplicates", new_shuffled)
# # # choices is not going to work here Return a k sized list of elements chosen from the population with replacement.
print("Choices: expect duplicates", random.choices(numbers, k=10))  # so choices will give us duplicates, with replacement
print(numbers)
random.shuffle(numbers)  # IN PLACE so returns nothing
print(numbers)
numbers.sort() # again IN PLACE
print(numbers)
