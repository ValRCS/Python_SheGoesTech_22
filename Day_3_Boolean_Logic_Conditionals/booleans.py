is_raining = False # this is a boolean variable
is_sunny = True
is_summer = False
# # # false = True # legal name for variable but not not recommended...
# # # False = False # not legal at all,
print(is_raining, is_sunny)
print(type(is_raining), type(is_sunny), type(is_summer))
print(2 * 2 == 4)  # notice  double == , this is comparison this is not assignment!
# # # #
# #
is_math_correct = 2 * 2 == 4  # we go from right to left, parenthesis are not required
# # #
print(is_math_correct)
a = 2
b = 4
print(a * a == b, a * a == 4, a * a == 5)  # more common
print(2 == 2.0, a == 2.0)  # two types but should be true
print(1 == True, True == 1, False == 0, 0 == False)  # True is represented by 1, we should actually use is to compare with False and True
# print(1 == True, True == 1, False == 0, 0 == False)  # True is represented by 1, we should actually use is to compare with False and True
print(True+True+True+False) # so 3 because this is just regular math with 1 and 0
# # # # # and False by 0
# # # # # there are some other falsy values, meaning values which equal to False when comparing
print("" == False)  # empty string is not the same as False but it will be used similarly in logical operations
print("" == '')  # True because it is same empty string, " and ' are interchangeable in Python
my_name = "Valdis"
print(my_name == my_name, my_name == "Valdis", my_name == "Voldis")
print("Valdis" == 55, my_name == 253253)  # False because different types
# # # #
# # # # # inequality
print(a,b)
print(a != b)  # if they are inequal then != will give True
print(2 != 2, a != 2, b != 2)  # this is a False statement because 2 is in fact equal to 2
is_not_equal = a * 2 != b  # a false statement because a * 2 is equal to 4
print(is_not_equal)
# # #
# print(a * 5 == b * 2.5)
# a = 10
# b = 20
# print(a * 5 == b * 2.5)
# a = 15
# print(a * 5 == b * 2.5)
# # # #
# # # # # greater >
print(a,b)
print(2 > 3, 3 > 2, 9001 > 9000) # False True True
print(a * a > 3, a * a > b, a * a > 5, a * a > b * 15)
# b = 10
# print(a * a > 3, a * a > b, a * a > 5, a * a > b * 15)
print(True > False)  # if True is 1 and False is 0 then this should be True :)
# # # # # we can compare other data types
print("Voldemars" > "Valdis")  # gives us True but why?
# # # # #
print("Voldis" > "Valdis")  # this is also true
print("Vol" > "Valdis")
print(ord("V"), ord("a"), ord("o"), ord("ā"), ord("😀"))  # we can get Unicode codes for characters
print(chr(86), chr(97), chr(256), chr(257), chr(18000), chr(128512))  # i can print from codes the symbols
# # # #
# # # # if we need by length - we can measure length of sequences , strings and many other types
print(len("Voldemārs") > len("Valdis"))
print(len("Voldemārs"))
print(len("Valdis"))
# # # less than <
print(a,b)
print(2 < 3, 3 < 3, a < b, b < a) # True False True False
# # # #
# # # # # less or equal
print(a,b)
print(2 <= 3, 3 <= 3, 3 <= 4, 5 <= 3)
print(a*2 <= 3, a*2 <= b, a*2 <= b*2, a*2 <= b*2.5) # False True True True
# print(a <= 14, a <= 15, b <= 16)
# # # #
# # # # # gt greater or equal
print(2 >= 3, 3 >= 3, 4 >= 3, a * 2 >= b * 3)
# # # #
# # #
c = 50
print(a,b,c,1000)
# so in Python we can compare multiple values at once
print(a < b < c < 1000)  # so 2 < 4 < 50 < 1000 is True
print(5000 < a < 8000)  # False
# a = 8
# # # we can compare more than two at once
# print(a,b,c,1000)
# print(a < b < c < 1000)  # four values at once
# print(a < -50 < b < c < 1000)  # false because first operation shortcircuits to False
# # # #
# # # # # is compares actual memory address
# # # # # used less
# you use is to compare if two variables point to the same object
print(a is b)  # really it is id(a) == id(b)
# print(2 is 2)  # should not really use instead use == AVOID!
print((2*2 == 4) is True) # use to compare something with True or False
print((2*3 == 4) is False) # True again
print((2*3 == 4) == False) # not recommended but works
# # # # # we use it when we need to see if both variables point to same object
# # # # is can be handy for finding whether you have same shopping cart
# # # or you have two different shopping carts with same items - just an analogy
# print(a,b,c)
# print(a + b == c - 32, a + b == c + 1 - 32)
# print("All Done")
