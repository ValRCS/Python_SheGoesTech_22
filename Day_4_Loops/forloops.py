# # # # # # # for loops are for definite iteration
# # # # # # #
# so num is the name of the variable we are going to use to iterate through the list
# for num in range(5):  # range is sort of half ready number sequence , num is a variable created for each iteration
#     # range starts with 0 and ends with 4
#     print(num)
#     print("Hello there!")
#     print("Number is", num)
# print("out of loop", num)
# # # # # so range takes range(start(default 0), end(not included), step)
# #
# for i in range(4, 11): # so careful of off-by-one errors, remember range will stop at 10 not 11 here!
#     print(f"I like this {i} better")
# #
# # # we can also iterate/loop over strings
# my_name = "Valdis Saul"
# my_name = "Kaķis Ņauva" # Kaķis is a cat in Latvian
# # so string is just a sequence of characters, thus we can loop over it
# for c in my_name: # c could be also char, or my_c, c is just shorter
#     print("Letter ", c)
#     print(f"Letter {c} Unicode is {ord(c)}")
# # # # # #     if c < "a": # this would include digits space,etc
# #     if c.isupper():  #works  even on Latvian capital letters such as Ņ Ā etc
# #         print("You are using uppercase letter are you not?", c)
# #     else:
# #         print("not an uppercase character could be anything else", c)
# # # #
# # # # # #
# # # print("This happens after the loop is done")
# # # #
# # range with 2 parameters we have start inclusive and until end exclusive
# # for n in range(20,25):  # we loop until 24
# #     print(n)
# # # # # # #
# #
# # range allows us to add step parameter
# for my_num in range(100,111,2): # i can add step to range, I added +1 to make it inclusive
#     print(my_num)

# # we can use decrementing range
# for i in range(10, 4, -2):  # we go from 10 to 6 (not 4)
#     print(i)
# # # # #
# start = 10
# end = 37
# step = 4
# early_break = 128
# for my_num in range(start,end+1,step): # i can add step to range
#     print(my_num)
#     if my_num > early_break:
#         print(f"Reached our early break threshold {early_break}")
#         break

# print("This happens after the loop is done", my_num)
# #
# # # #
# # # #
# # # # # # #
# # # # # # #
# for _ in range(4):  # _ means that we do not care about the variable, i just want to do something 23 times
#     print("We do not need the number in this case")
#     print("We just want to do something 4 times")
# # # # # #
# # # #

# # we can nest loops

big_total = 0
even_number_count = 0
for i in range(1,5): # outer loop 1 to 4
    for j in range(1, 3):  #inner loop 1 to 2
        result = i * j
        print(f"{i}x{j}={result}")
        big_total += result
        if result % 2 == 0: # evenness check
            print("oh even number", result)
            even_number_count += 1

print("Total is", big_total)
print("Even number count is", even_number_count)
# # # # # # #
# # # # # # # my_name = "Valdis"
# # # # # # # for c in my_name:
# # # # # # #     print("Letter ", c)
# # # # # # #
# # # # # # my_list = [1,2,100,105,"Valdis","potatoes", 9000, 107.35]
# # # # # # total = 0
# # # # # # big_items = 0
# # # # # # for item in my_list:
# # # # # #     print("Working with item: ", item)
# # # # # #     if type(item) == int or type(item) == float:
# # # # # #         total += item
# # # # # #         if item > 100:
# # # # # #             big_items += 1
# # # # # # #
# # # # # my_num_list = [1,6,17,7,-6,49,642,6,2,-5555] # this is a list
# # # # # # #
# # # # # my_max = None
# # # # # for num in my_num_list:
# # # # #     print("Checking", num)
# # # # #     if my_max is None: # this will happen with first item
# # # # #         my_max = num
# # # # #     if num > my_max:
# # # # #         print("New max is", num)
# # # # #         my_max = num
# # # # # # #
# # # # # print("My max is", my_max)
# # # # # print(max(*my_num_list)) # short way of finding max in list
# # # # # #
# # # # # # # So what do we do when we need and index
# # # # # # my_name = "Valdis Saulespurēns"
# # # # # # print(f"{my_name} is {len(my_name)} characters long")
# # # # # # print(my_name[0])
# # # # # # print(my_name[5])
# # # # # # # anti-pattern do not write this way in Python
# # # # # # for n in range(0, len(my_name)):
# # # # # #     print(n, my_name[n])
# # # # # # #
# # # # # # # more Pythonic is using enumerate:
# # # # # # # use this if you need index
# # # # #
# my_name = "Valdis"
# for index, c in enumerate(my_name): # i could have used i instead of index
#     print(f"Letter {index} is {c}")
#     print("Letter", index, "is",c)
# # # # #
# # for index, c in enumerate(my_name,start=1):
# #     print("Letter", index, "is",c)
# # # # # # #
# # # # # # # if i do not like 0 i can start with any number
# # # # # # for i, c in enumerate(my_name, start=101):
# # # # # #     print("Letter", i, "is",c)
# # # # # #
# # # # # #
# # # # # # my_num = 20
# # # # # # for n in range(1,11):
# # # # # #     reminder = my_num % n
# # # # # #     result = my_num // n # whole number
# # # # # #     print(f"{my_num} divided by {n} gives {result} with {reminder} as reminder")
# # # # #
for n in range(1,21):  # from 1 until 20
    if n%2 == 0: # even numbers have no reminder when divided by 2
        print(f"{n} is even")
    else:
        print(f"{n} is odd")
# # # # #
# # # # # print by default has end value \n - newline
# # # # # we can change this
# # # print("Fizz", end=",")
# # # print("Buzz", end=",")
# # # print("342", end="****")
# # # #
print(" "*10+"*"*6)
# # # #same as above
for _ in range(10):
    print(" ", end="") # end="" means do not add newline
for _ in range(6):
    print("*", end="")
# # # print() # prints new line