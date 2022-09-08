# print("Valdis")
# print("Valdis", "Zatlers")  # i can use comma to separate multiple objects
# print("Valdis", "Zatlers", "Python")
# # we can do math in Python
# print(2 + 2)
# # print(2 - 2)
# # print(2 * 3)
# # print(2 / 2) # result is float, decimal number with comma
# # print(2 ** 5)  # 2 to the power of 5
# # print(2 ** 0.5)  # 2 to the power of 0.5 that is square root
# # print(10 % 3)  # modulo operator, remainder of division, so here it is 1
# # print googol
# print(10 ** 100) # 10 to the power of 100, Python supports large numbers out of the box

# # why we had to move from 32 bits
# print(2 ** 32)  # 4294967296 so this is famous 32 bit limit
# print(2 ** 64)  # 18446744073709551616

# # for math we can use parenthesis
# print((2 + 3) * 4)  # 20

# print("beer " * 5)  # beer beer beer beer beer
# print("Valdis" + " likes " + "beer")  # Valdis likes beer
# # # # we declare variables in Python when we first use them
my_name = "Valdis"  # there are no types no val, no var no const nothing like that in Python
print(my_name) # this prints Valdis
print("my_name")  # this is not a variable, this string literal
print(my_name + " likes beer")  # Valdis likes beer
# i can keep using my_name
print(my_name + " likes beer" * 5)  # Valdis likes beer beer beer beer beer
# #
# # # variables do have data types in Python
print(type(my_name))
# # # so for any variables you can find out type with type(my_variable)
# # # there are primitive types and compound(collection) types
my_num = 42  #answer to everything
print(my_num)
print(type(my_num))  # should be int
a = 42
b = 42
c = 43
print(id(a), id(b), id(c), id(my_num))
print(id(c)-id(b)) # so storing int took 32 bits or 4 bytes
# id shows where in memory(virtual memory) the variable is stored

print(a, b, my_num)
# you can reassign variables
b = 9001  # b now points to a different memory location
c = 9_000  # you can use underscore _ for larger numbers just as a cosmetic , machine ignore it starting from python 3.6
print(a, b, c, my_num)
my_result = b + c  # new variable my_result is introduced
print(b, c, my_result)
# #
# print(id(b))  # this shows where in virtual memory the b points at
# print(id(c))  # this shows where in virtual memory the b points at
# #
print(my_name, type(my_name))  # my_name is a string
# you can change the type of variable, but generally it is best avoided
my_name = 7  # so here dynamically Python changed where my_name points at
print("I do not want ot be a number!", my_name, type(my_name))  # so now my_name points to different content
# # # but also my_name is now pointing to different data type all together
# #
# # # this is convenient at times
# # # it is using so called duck typing - if it quacks like a duck, walks like a duck it is duck
# #
# # # so data type is inferred from the data we give our variables
# # # this is so called dynamic typing
# # # there are languages with static types it takes more code to write with static language
# # # but for larger projects static languages are preferable for management reason
# #
# # # so Python really shines in prototypes, smaller projects
# #
# # # there are exceptions, like Dropbox which has those 3 million lines of Python :)
my_name = "Valdis"  # i am back to normal
president = "Valdis"
neighbor = "Valdis"
print(id(my_name), id(president), id(neighbor), sep="\n")  # sep is what to use between , in print
neighbor = "Voldemars"
print(id(my_name), id(president), id(neighbor), sep="\n***\n")
# #
# neighbor = "VisValdis"  # Voldemars is going to be garbage collected, otherwise we would get a memory leak
print(c)  #
c = c + 5000  # this is not algebra we are creating a new value on the left from the right
# so we added 5000 to c and assigned it to c
# # # evaluation happens from the right side , assignment to the left
# # # above is not an equality!! there is another symbol for equality (Day 3)
print(c)  # this should be 14000
# # this c = c + 5000 is so common that there is a shortcut
c += 10_000  # shorter way of writing c = c + 10000  # computer speed wise it is the same
print(c, type(c))

c -= 5_000  # shorter way of writing c = c - 5000
print(c, type(c))
# #
c = c + 3.1415926  # this is a float that we are adding to c
print(c, type(c))  # so c changed data type to float
# #
c -= 3.1415926  # this is a float that we are subtracting from c
print(c, type(c))  # still float

# # what do to if we want an integer?
c = int(c)  # this is a conversion, so called type casting
print(c, type(c))  # back to integer


e = 2.718281828459045  # this is a float
print(e, type(e))
flat_e = int(e)  # this is a conversion, so called type casting
print(e, flat_e)
e_rounded = round(e)  # this is a rounding function default will be integer with no extre arguments
print(e_rounded, type(e_rounded))
e_rounded_to_2 = round(e, 2)  # this is a rounding function with 2 decimals
print(e_rounded_to_2, type(e_rounded_to_2))
# print(e_rounded_to_2)
# so 2.5 will be rounded to 2, 3.5 will be rounded to 4
print(round(2.49), round(2.5), round(2.50000000001), round(2.51))
print(round(3.5)) # so what is going on? 3.5 is halfway between 3 and 4
print(round(4.5))
print(round(5.5))
print(round(6.5))
print(round(7.5))
print(round(8.5))  # when we learn loops this will be easier to write :)
print(3.5 - 3 - 0.5)
# problem with floats is that they are not exact
print(0.1 + 0.2)  # 0.30000000000000004
my_round_3 = round(0.1 + 0.2, 6)  # 0.3
print(my_round_3)

print(round(e, 6))  # 2.718282
e = int(e)  # this is a conversion, so called type casting, here it works as floor function
print(e, type(e))  # back to integer, so we lose some information
# #
# # my_pi = 3.1415926
# # print(my_pi, type(my_pi))
# #
# # # Naming things are hard
# you can use letters, numbers and underscore _ but not at the beginning
# # #Function and Variable Names
# # # from https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions
# # # Function names should be lowercase, with words separated by underscores as necessary to improve readability.
# # #
# # # Variable names follow the same convention as function names.
# # #
my_cool_variable = 5555 # this is called snake_case, Python standard
myCoolVariable = 5555 # this is called camelCase, Java standard
# do not use BOTH in the same project
my_variable_2 = 5555 # so numbering is fine but if you have more than few numbers you might need 
# different data structure like list or tuple (explained later)
# # # mixedCase is allowed only in contexts where that's already the prevailing style (e.g. threading.py), to retain backwards compatibility.
# #
# # bad would be to have my_name and myName in a same project
# # do not make me think about it !
# # # d = a # d points to the same value as a
# # # print(a,d)
# # #
# # # a2 = 50 # we can do this but generally this smells of improvement
# # # a3 = 51
# # # a4 = 52 # there are better data structures
# # #
# # # # one of the hardest things in programming is naming variables
# # #
# # launch_codes_to_nuclear_weapons = "GoodBEEF" # a bit long
# # # takes too long to type even on a good IDE
# # # launch_codes should be better assuming your program a nuclear weapons program...
# # #
# # # # short variables which are fine
# # # # x,y,z  would be fine when dealing with coordinates
# #
# # # i for iterator,
# # # # t for temporary
# # # # c for characters
# # # # f for file
# # #
# # # # h for height
# # # w - width would be okay
# # # # l for length is a bit iffy, use of l is discouraged
# # # # why? because l can be confused with 1 and I on some systems
# # #
# # # # all capital variable means that it really is a constant
RTU = "Riga Technical University"
print(RTU)
RTU = "Accenture" # no body is going to stop you here but you should not do this if you have capital letters
print(RTU)
# # # # we shouldn't change this
# # #
# # # # we use English
kaķis = "my cat"  # please do not do this :)
print(kaķis)
my_cat = "mans kaķis Muris murrā" # that is fine
print(my_cat)
smiley_msg = "AHmm ! 😀 -> \u1F600" # this is 16bit Unicode and 0
print(smiley_msg)
smiley_again = "Aha 😆 ! 😀 -> \U0001F600" # for Unicode encoded with more than 4 Hex symbols you need to use 32
print(smiley_again)
# #
# # # so we have str, int, and float so far
# # # there is also boolean (Day 3), None -> which is specific type for representing nothing
# # # then we have more complext collections
# #
my_str = "888.67" # this is str
my_float = float(my_str) # this is forced type casting we want to cast our text string into a number
my_int = int(my_float) # here I cast float to integer so naturally I lose everything after comma

print(my_str, my_float, my_int)
# #
# # # not everthin will cast to number
print(my_name)
# will_fail = int(my_name) # this will fail with an ValueError # there are ways of checking
# we will need to handle Exceptions later in the course