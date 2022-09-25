#1. The Big Result

# Write an add_mult function that requires three parameters / arguments

# Returns the result that is the sum of the 2 smallest arguments multiplied by the largest argument value.

# PS Assume that numeric parameters will always be passed to the function, no need to check types

# Various solutions are possible (you are allowed to use other data structures inside function such as list).

# Example add_mult (2,5,4) -> will return (2 + 4) * 5 = 30

# PSS function should return the result, not print it.

# a = int(input("Please enter first integer: "))
# b = int(input("Please enter second integer: "))
# c = int(input("Please enter third integer: "))

# def add_mult(a, b, c):
#     arg_list = [a, b, c]
#     arg_list.sort() # IN PLACE SORTING ASCENDING is default
#     largest = arg_list[2] # max(arg_list)
#     smallest = arg_list[0] # min(arg_list)
#     middle = arg_list[1]

#     return (smallest + middle) * largest

# def add_mult(a,b,c):
#     biggest=max(a,b,c)
#     #return biggest
#     if a == biggest:
#         resultat=((b+c)*a)
#     elif b == biggest:
#         resultat=((a+c)*b)
#     else:
#         resultat=((a+b)*c)
#     return resultat

# most universal solution
def add_mult(*args):
    # number_list = []
    # for arg in args:
    #     number_list.append(arg)
    number_list = list(args) # no need for loop
    number_list.sort()
    first_element=number_list[0]
    second_element=number_list[1]
    last_element=number_list[-1]
    # print(first_element, second_element,last_element)
    calc=(first_element+second_element)*last_element
    return calc

result = add_mult(2, 2, 4)
print(result)
print("Testing should be all True")
print(add_mult(4,5,1) == 25)
print(add_mult(2, 2, 4) == 16)
print(add_mult(10,-5,2) == -30)
# in testing we use assert
# here we are performing so called unit test on our function
assert(add_mult(2, 2, 4) == 16)
assert(add_mult(10,-5,2) == -30)
assert(add_mult(4,5,1) == 25)
assert(add_mult(0,0,0) == 0) # wrong assertiong FIXME
# general rule for testing check edge cases, such as zero, negative numbers, etc.