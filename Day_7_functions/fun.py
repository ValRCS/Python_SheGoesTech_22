# # # # # # # # # # # formal https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# # # # # # # # # # # built in functions https://docs.python.org/3/library/functions.html
# # # # # # # # # # # DRY ! https://en.wikipedia.org/wiki/Don%27t_repeat_yourself
# #
# # # # # # # # # # # we can give our functions parameters and those parameters take arguments
# #
# print("Go eat")
# print("Let's order food")
# # #
# print("maybe i do something else")
# # more code follows
# print("Go eat")
# print("Let's order food")
# print("Go eat")
# print("Let's order food")
# #
# # # # # # # defining simple function
def go_eat():
    # function block starts here
    print("Calling function go_eat")
    print("Go eat fast food")
    print("Let's order food RIGHT Now!")
    print("Pay and Leave")
    # we could add more stuff for our function here include loops, ifs etc


#
#
# #
# # # # # # # # # # # calling function
#
#
# go_eat()
# go_eat()
# print("Do something else")
# for _ in range(4): # if we do not need the loop variable we use _, all that we care about is the loop
#     go_eat()
# # # # # # go_eat()
# #
# # order_food("No bueno")  # can't call before defining
#
#
# dish = "pizza"  # this is outer scope, nothing to do with order_food parameter


# # # # # # # # # # # requirement that order_food is given an argument
def order_food(dish):  # dish is a parameter, can be called anything
    dish = str(dish)  # because we will be using capitalize later on, this is not required most of the time
    print(f"I am ordering {dish}")
    print(f"{dish.capitalize()} should be pretty tasty")
    # so local dish stops working here


#
#
# # # # # # # # no dish here
# #
# #
# order_food("potatoes")
# order_food("ice cream")
#
# my_soup = "Beet soup"
# order_food(my_soup)
# order_food(555)
# #
# print(dish) # dish is not available globally because it is only inside function
# #
# #
# # # # # # # # # # # # go to restaurant
#
#


def eat(food_list):
    # everything after indent will be run by this function
    print("Hello")
    print("Let's order some food")
    # could add a check if food_list is truly a list
    for food_item in food_list:  # food item is local to function eat
        order_food(food_item)
    print("Lets eat")
    print("Let's leave and be happy")


#
# food_list = ["soup", "potatoes", "ice cream"]
# eat(food_list)
# print("All done")
# another_food_list = ["cabbage", "beans", "onions"]
# eat(another_food_list)
# # #
# # # # # # # # # # # # # call the function 2 times
# # # # # # # eat(["soup", "potatoes", "ice cream"])
# # # # # # # eat(["Cabbage"]) # i need one argument for eat function
# eat(["Kartupelis"])  # so we passed a list of one item
# # # # # # # what happens if we pass our function a string...
# eat("Kartupelis")  # turns out we will go through our food one letter at a time...
#
#
def add(a, b):  # function with 2 parameters
    print(f"Adding {a} + {b}")

    # i can leave empty lines in between different operations
    print(f"{a}+{b}={a + b}")
    # function definition ends here


#
#
# add(3, 322)
# add(5, 7)
# add(25, 37)
# my_result = add(10, 25)  # without return Python functions return None
# print(my_result, type(my_result))
# my_print_result = print(2+2)
# print(my_print_result, type(my_print_result))  # print also returns None !!
# print is a function with side effects, in this case it returns None, but prints to output
#
#
def mult(a, b):
    result = a * b  # result could be another name
    print(f"{a}*{b}={result}")  # print is not always needed in a function, print is heavy
    return result  # we can return anything


#
#
def eco(a, b, c):
    print(a, b, c)
    c = a + b + c  # we can change the value of c, even though it is a parameter
    print(a, b, c)
    return c


#
#
# my_result = eco(mult(2, 3), mult(5, 7), mult(2, 4))
# print(my_result)


#
# my_calc = mult(5, 8)
# print(my_calc)
# multi_calc_result = mult(mult(5, 10), mult(10, 2))  # with return I gain ability to apply result to next function
# print(multi_calc_result)


#
#
# #
#
# I can return multiple values from a function
def multi_calc(a, b):
    # could add check for 0
    print(f"{a}*{b}={a * b}")
    print(f"{a}/{b}={a / b}")
    return a * b, int(a / b)  # could return even more, multiple values are returned as tuples


#
#
# my_mult, my_div = multi_calc(10, 2)  # technically this is so called tuple unpacking
# print(my_mult, my_div)
#
# my_tuple = multi_calc(10, 2)  # in reality we are returning a collection data type called tuple
# print(my_tuple)
#
#
# # print(multi_calc(9,2)) # parenthesis show up because we are returning a tuple(which is likea  fixed list)
#
# default arguments - we can predefine default values for parameters
def big_calc(a=-500, b=1000, c=100):  # so c will be 100 if not given as argument
    result = a * b + c
    print(f"a*b+c={result}")
    return result


#
#
# my_big = big_calc(3, 4, 10)
# print(my_big)  # 22
# another_calc = big_calc(3, 5)  # notice we only need 2 arguments if we are lazy
# print(my_big, another_calc)  # should be 3*5+100=115
# # #
# print(big_calc(5))  # only giving value for a, : b,c use defaults so 5100
# print(big_calc())  # this will use ALL 3 default values so negative -500*1000+100==-499900
# # with named arguments we can use default values for some parameters and not others
# print(big_calc(c=1000, b=5, a=4))  # i can pass arguments in whichever order I want if i use named arguments
# # the above is a not a great example of good practice, because we are needlessly changing the order of arguments
# print("Valdis", "Līga", end="*****\n", sep="::")


#
#
# # print(big_calc(b=25)) # i can pass only one named argument, the rest stay default
#
#
def talk(text, is_yelling=False, trim=False, verbose=True):
    """
    Prints text
    is_yelling capitalizes text
    trim - trims whitespace from both ends
    verbose - if you want to print something on screen
    returns transformed text
    """
    if trim:
        text = text.strip()
    if is_yelling:
        text = text.upper()
    if verbose:
        print(text)  # printing is considered a side effect inside a function
    return text


#
#
# talk("Hello there")  # basically a print
# talk("Hello there indeed", True)  # True refers to is_yelling but it might not be obvious with many flags
# talk("Hello there", is_yelling=True)  # this is more clear
# talk("   Please   trim me   ", True)  # i wanted a trim not yell...
# talk("   Please   trim me   ", trim=True)  # so now i should get a trim
# trimmed_text = talk("   Please   trim me   ", trim=True, verbose=False)  # verbose=False means no printing
# print(trimmed_text)  # prints only trimmed text
# #
# #
# talk(is_yelling=True, text="some random text")  # with named arguments I can change order, but generally not recommended
# print(talk("Hello", is_yelling=True).lower())  # if function returns something i can chain it


# # # # talk("Aha", True)
# #
# # # # # add(b=10, a=3)
# #
# # # print("Valdis", "coding", end="\n\n\n!\n\n", sep="|||")
# #
#
# # # # # so in Python data types in function parameters are just hints! they do not affect function functionality
def diff(a: int, b: int) -> int:  # we defined a function signature , what data types should be used
    result = round(a - b, 2)
    print(f"{a}-{b}={result}")
    return a - b
    # return "badac"


#
#
# #
# diff(10, 3)
# diff(10.6, 3.7)  # even if the data types are wrong, Python will still run the program
# #
# # most IDE's will give you a warning if you pass wrong data types, but programs will run anyway
#
# diff("Valdis",35354)
# # # # it is only static type checking tool such as Pyright extension that will yell at us
# #
# #
# #
# #
#
# # so preferred way to structure larger programs is to have some main function which calls everything else
def var_fun(required_n, *optional_arg_list, my_default=1000):
    print("Required", required_n)
    print("my_default", my_default)
    for n in optional_arg_list:
        print("optional", n)
    return required_n + sum(optional_arg_list) + my_default  # assuming we give parameters that are summable


#
#
# var_fun(5) var_fun(10,30) var_fun(10,30,40,50) # optional arguments are always at the end, before default
# arguments,my_default is optional and still 1000 var_fun(10,30,40,50, my_default=2000) # my_default is optional and
# so now it is 2000

# # we call that main() from if guard
def main():  # can call other functions from here, main can be named anything
    print("Starting my main program")
    result = var_fun(100, 6, 10, 50, my_default=1_000_000)
    print(result)


#     result = var_fun(200)  # so only 200 was required rest were optional
#     print(result)
#     # init function here
#     # calling other functions
#     # maybe main loop here
#
#
# # this is used to check whether you started function as main or imported it as a library
if __name__ == "__main__":
    main()
    # I could also use this to check if you are running this file as a library
    # I can run more code here if i want to
