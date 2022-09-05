# Exercise 1


# def add_mult(*my_nums):
#     # my_nums = [int(t) for t in input("Enter three values separated by whitespace: ").split(" ")]
#     my_nums = list(my_nums)
#     my_nums.sort()
#     result = (my_nums[0] + my_nums[1]) * my_nums[-1] # as long as we have two values or more
#     print(result)
#     return result


def add_mult(a, b, c):
    # if a > b:
    #     a, b = b, a
    # if a > c:
    #     a, c = c, a
    # if b > c:
    #     b, c = c, b
    a, b, c = sorted([a, b, c])
    print(f"equation: ({a} + {b}) * {c}")
    return (a + b) * c


my_result = add_mult(4, 7, 2)
print(my_result)
my_result = add_mult(4, -7, 2)
print(my_result)
