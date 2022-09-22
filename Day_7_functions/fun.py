# # # # # # # # # # # # # formal https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# # # # # # # # # # # # # built in functions https://docs.python.org/3/library/functions.html
# # # # # # # # # # # # # DRY ! https://en.wikipedia.org/wiki/Don%27t_repeat_yourself
# # # #
# # # # # # # # # # # # # we can give our functions parameters and those parameters take arguments
# # # #
# # what is a function?
# # a function is a block of code that is designed to do one specific job
# # the above is a platonic ideal of a function - not always true

# # print("Go eat")
# # print("Let's order food")
# # # #
# # print("maybe i do something else")
# # # more code follows
# # print("Go eat")
# # print("Let's order food")
# # print("Go eat")
# # print("Let's order food")
# # # #
# # # # # # # # # defining simple function
# def go_eat():
#     # function block starts here
#     print("Calling function go_eat")
#     print("Go eat fast food")
#     print("Let's order food RIGHT Now!")
#     print("Pay and Leave")
#     # we could add more stuff for our function here include loops, ifs etc


# # #
# # #
# # # #
# # # # # # # # # # # # # calling function
# # #
# # #
# # go_eat()
# # go_eat()
# # print("Do something else")
# # for _ in range(4): # if we do not need the loop variable we use _, all that we care about is the loop
# #     go_eat()
# # # # # # # # go_eat()
# # # #
# # # # order_food("No bueno")  # can't call before defining
# # #
# # #
# # # dish = "pizza"  # this is outer scope, nothing to do with order_food parameter


# # # # # # # # # # # # # requirement that order_food is given an argument
# def order_food(dish):  # dish is a parameter, can be called anything
#     dish = str(dish)  # because we will be using capitalize later on, this is not required most of the time
#     print(f"I am ordering {dish}")
#     print(f"{dish.capitalize()} should be pretty tasty")
#     # so local dish stops working here


# # #
# # #
# # # # # # # # # # no dish here
# # # #
# # # #
# # order_food("potatoes")
# # order_food("ice cream")
# # # #
# # my_soup = "Beet soup"
# # order_food(my_soup)
# # print("Done with soup for now")

# # # so print is a built in function
# # # https://docs.python.org/3/library/functions.html

# # order_food(555)
# # # #
# # print(dish) # dish is not available globally because it is only inside function
# # # #
# # # #
# # # # # # # # # # # # # # go to restaurant
# # #
# # #


# def eat(food_list):
#     # everything after indent will be run by this function
#     print("Hello")
#     print("Let's order some food")
#     # could add a check if food_list is truly a list
#     for food_item in food_list:  # food item is local to function eat
#         order_food(food_item)
#     print("Lets eat")
#     print("Let's leave and be happy")


# # #
# food_list = ["soup", "potatoes", "ice cream"]
# # eat(food_list)
# # print("All done")
# # another_food_list = ["cabbage", "beans", "onions"]
# # eat(another_food_list)
# # # # # #
# # # # # # # # # # # # # # # # call the function 2 times
# # # # # # # # # # eat(["soup", "potatoes", "ice cream"])
# # # # # # # # # # eat(["Cabbage"]) # i need one argument for eat function
# # eat(["Kartupelis"])  # so we passed a list of one item
# # # # # # # # # # what happens if we pass our function a string...
# # eat("Kartupelis")  # turns out we will go through our food one letter at a time...
# # #
# # #
# def add(a, b):  # function with 2 parameters
#     print(f"Adding {a} + {b}")

#     # i can leave empty lines in between different operations
#     print(f"{a}+{b}={a + b}")
# #     # function definition ends here


# # #
# # #
# # add(3, 322)
# # add(5, 7)
# # add(25, 37)
# # my_result = add(10, 25)  # without return Python functions return None
# # print(my_result, type(my_result))
# # my_print_result = print(2+2)
# # print(my_print_result, type(my_print_result))  # print also returns None !!
# # # print is a function with side effects, in this case it returns None, but prints to output
# # #
# # #
# def mult(a, b):
#     result = a * b  # result could be another name
#     print(f"{a}*{b}={result}")  # print is not always needed in a function, print is heavy
#     return result  # we can return anything

# mult(2, 3) # but i did not save the result
# my_result = mult(20, 3) # now I have saved the result and can use later on
# print(my_result)
# # #
# # #
# def eco(a, b, c):
#     print(a, b, c)
#     d = a + b + c  # we can change the value of c, even though it is a parameter
#     print(a, b, c, d)
#     return d

# print(eco(5, 6, 7))
# # #
# # #
# my_result = eco(mult(2, 3), mult(5, 7), mult(2, 4))
# print(my_result)

# # maybe you want to make a function that checks if a number is prime
# # using functions to subdivide your code into smaller pieces
# def is_odd(number):
#     # i could write some code here of course
#     return number % 2 == 1 # notice I am not using if here, just returning a boolean

# print(is_odd(77))
# print(is_odd(78))

# # TODO explore multiple return values
# # TODO explore default values for parameters

# # #
# # # my_calc = mult(5, 8)
# # # print(my_calc)
# # # multi_calc_result = mult(mult(5, 10), mult(10, 2))  # with return I gain ability to apply result to next function
# # # print(multi_calc_result)


# # #
# # #
# # # #
# # #
# # # I can return multiple values from a function
def multi_calc(a, b):
    # could add check for 0
    print(f"{a}*{b}={a * b}")
    print(f"{a}/{b}={a / b}")
    return a * b, int(a / b)  # could return even more, multiple values are returned as tuples


# # #
# # # so i come up with two variable names
# my_mult, my_div = multi_calc(10, 2)  # technically this is so called tuple unpacking
# print(my_mult, my_div)
# # # #
# my_tuple = multi_calc(10, 2)  # in reality we are returning a collection data type called tuple
# print(my_tuple)

# if your values are similar then you can use a list and return it
def create_new_list(start, end):
    new_list = [] # so you create a list inside the function
    for i in range(start, end+1):
        new_list.append(i)
    return new_list

# new_list = create_new_list(1, 10)
# print(new_list)
# same_numbers_different_list = list(range(1,11))
# print(same_numbers_different_list)
# # #
# # #
# # # # print(multi_calc(9,2)) # parenthesis show up because we are returning a tuple(which is likea  fixed list)
# # #
# # # default arguments - we can predefine default values for parameters
# better name for function would be what it does, not how it does it
def big_calc(a=-500, b=1000, c=100, is_printing=True):  # so c will be 100 if not given as argument
    result = a + b + c
    if is_printing:
        print(f"{a}+{b}+{c}={result}")
    return result


# # #
# # # default values will not be used if all arguments are given
# my_big = big_calc(3, 4, 10)
# print(my_big)  # 22
# another_calc = big_calc(3, 5)  # notice we only need 2 arguments if we are lazy
# print(my_big, another_calc)  # should be 3+5+100=108
# # # # # #
# print(big_calc(5))  # only giving value for a, : b,c use defaults so 1105
# print(big_calc())  # this will use ALL 3 default values so negative -500+1000+100=600
# # # # # with named arguments we can use default values for some parameters and not others
# print(big_calc(c=1000, b=5, a=4))  # i can pass arguments in whichever order I want if i use named arguments
# # do not do above on purpose, it is confusing
# # # # # the above is a not a great example of good practice, because we are needlessly changing the order of arguments
# # # # print("Valdis", "Līga", end="*****\n", sep="::")
# calc_value = big_calc(10,20,40, False)  # i can also pass a boolean value
# print(calc_value)

# # TIP: use named parameters when using boolean parameters
# another_val = big_calc(30, 40, is_printing=False) # here it is required to use named parameter
# print(another_val)

# # named parameters are also useful when you have a lot of parameters
# print("Hello", "Valdis", "Līga", "and", "friends", sep="::", end="*****\n")
# print("Hello", "Valdis", "Līga", "and", "friends",  end="*****\n", sep="::") # order does not matter if named

# # #
# # #
# # # # print(big_calc(b=25)) # i can pass only one named argument, the rest stay default
# # #
# # #
def talk(text, is_yelling=False, trim=False, verbose=True):
    """
    Prints text\n
    is_yelling capitalizes text\n
    trim - trims whitespace from both ends, takes False or True\n
    verbose - if you want to print something on screen\n
    returns transformed text
    """
    if trim:
        text = text.strip()
    if is_yelling:
        text = text.upper()
    if verbose:
        print(text)  # printing is considered a side effect inside a function
    return text


# # #
# # #
# talk("Hello there")  # basically a print
# talk("Hello there indeed", True)  # True refers to is_yelling but it might not be obvious with many flags
# talk("Hello there", is_yelling=True)  # this is more clear
# # # # talk("   Please   trim me   ", True)  # i wanted a trim not yell...
# talk("   Please   trim me   ", trim=True)  # so now i should get a trim
# # # trimmed_text = talk("   Please   trim me   ", trim=True, verbose=False)  # verbose=False means no printing
# # # print(trimmed_text)  # prints only trimmed text
# # # #
# # # #
# # # talk(is_yelling=True, text="some random text")  # with named arguments I can change order, but generally not recommended
# # # print(talk("Hello", is_yelling=True).lower())  # if function returns something i can chain it


# # # # # # talk("Aha", True)
# # # #
# # # # # # # add(b=10, a=3)
# # # #
# # # # # print("Valdis", "coding", end="\n\n\n!\n\n", sep="|||")
# # # #
# # #
# # # # # # # so in Python data types in function parameters are just hints! they do not affect function functionality
# # def diff(a: int, b: int) -> int:  # we defined a function signature , what data types should be used
# #     result = round(a - b, 2)
# #     print(f"{a}-{b}={result}")
# #     return a - b
# #     # return "badac"


# # #
# # #
# # # #
# # # diff(10, 3)
# # # diff(10.6, 3.7)  # even if the data types are wrong, Python will still run the program
# # # #
# # # # most IDE's will give you a warning if you pass wrong data types, but programs will run anyway
# # #
# # # diff("Valdis",35354)
# # # # # # it is only static type checking tool such as Pyright extension that will yell at us
# # # #
# # # #
# # # #
# # # #

# variable number of arguments function
def multi_sum(*args):  # *args is a tuple of all arguments
    print(args)  # args is a tuple, we can iterate/loop over it
    print(type(args))
    result = 0
    for arg in args:
        result += arg
    return result

# print(multi_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# print(multi_sum(1, 2))
# print(multi_sum())

# alternative would have been to use a list
def multi_sum2(my_list):  # *args is a tuple of all arguments
    return sum(my_list)
# # #
# # # # so preferred way to structure larger programs is to have some main function which calls everything else
def var_fun(required_n, *optional_arg_list, my_default=1000):
    print("Required", required_n)
    print("my_default", my_default)
    for n in optional_arg_list:
        print("optional", n)
    return required_n + sum(optional_arg_list) + my_default  # assuming we give parameters that are summable

# print(var_fun(10, 20, 30, 40, 50, my_default=100))
# print(var_fun(10, 20, 30, 40, 50)) # so 50 here is optional and my_default is default
# print(var_fun(10, 20, 30, 40, 50, 100)) # so 50 here is optional and my_default is default
# print(var_fun(200))

# # #
# # #
# # # var_fun(5) var_fun(10,30) var_fun(10,30,40,50) # optional arguments are always at the end, before default
# # # arguments,my_default is optional and still 1000 var_fun(10,30,40,50, my_default=2000) # my_default is optional and
# # # so now it is 2000

# # # # we call that main() from if guard
def main():  # can call other functions from here, main can be named anything
    print("Starting my main program")
    result = var_fun(100, 6, 10, 50, my_default=1_000_000)
    print(result)
    # can keep calling other functions here


# # #     result = var_fun(200)  # so only 200 was required rest were optional
# # #     print(result)
# # #     # init function here
# # #     # calling other functions
# # #     # maybe main loop here
# # #
# # #
# # # # this is used to check whether you started function as main or imported it as a library
if __name__ == "__main__":
    print("Starting main")
    main()
    # function_after_main() # will not work until we define it
# #     # I could also use this to check if you are running this file as a library
# #     # I can run more code here if i want to

def function_after_main():
    print("I am after main")