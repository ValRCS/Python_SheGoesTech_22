# my_string = input("Input as many values as you want separated by whitespace: ")
# my_list = my_string.split(" ")
# my_numbers = [int(element) for element in my_list]
# print(my_numbers, sum(my_numbers), min(my_numbers), max(my_numbers))

# one liner as above but maybe a bit too dense
my_nums = [int(t) for t in input("Enter values separated by whitespace").split(" ")]
print(my_nums)