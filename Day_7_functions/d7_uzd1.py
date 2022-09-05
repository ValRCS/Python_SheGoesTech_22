def add_mult (a, b, c):
    num_list = [a, b, c]  # local list variable

    print(f"My list: {num_list}")
    # num_list = sorted(num_list)  # OUT OF PLACE sort would work too
    num_list.sort()  # INPLACE sort, changes the list
    print(f"After sorting: {num_list}")
    print(f"({num_list[0]}+ {num_list[1]}) * {num_list[2]}")
    return (num_list[0] + num_list[1]) * num_list[2]


result = add_mult(20, 5, 3)
print (f"result is: {result}")