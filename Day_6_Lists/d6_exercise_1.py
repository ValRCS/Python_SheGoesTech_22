# 1a. Average value

# Write a program that prompts the user to enter numbers (float).


# The program shows the average value of all entered numbers after each entry.
# PS. 1a can do without a list

# 1b. The program shows both the average value of the numbers and ALL the numbers entered

# PS Exit the program  by entering "q"

# 1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.

# numbers = input("Input numbers: ")
# # numbers_list = numbers.split(" ")
# numbers_list = numbers.split() # this will split string into substrings by any whitespace
# print(numbers_list) # technically not a numbers list, but a list of strings
# # we need to convert each string to a float
# # numbers_list = [int(i) for i in numbers_list]
# numbers_list = [float(i) for i in numbers_list]
# print(numbers_list)
# # a = 0
# # for i in numbers_list:
# #     a = a + i
# # easier would be
# total = sum(numbers_list)  # so do not use sum as a variable name!
# result = total / len(numbers_list)
# print("Average",result)

# so idea is to have a blank list, and then append to it
# use a while loop and quit when user enters q
# numbers = []
# while True:
#     number = input("Input number: ")
#     if number == "q":
#         print("Quitting time!")
#         break
#     numbers.append(float(number))
#     # print(numbers)
#     total = sum(numbers)
#     result = total / len(numbers)
#     print("Average",result)
# print("All numbers",numbers)

# num_list = []

# a = 0  #not a good name for a variable unless it is related to something a like
# while a != "q":
#     a = input("Please enter a number, including decimals, or 'q' to quit: ")
#     if a != "q":
#         num_list.append(float(a))
#         # sumsum = 0
#         # for i in num_list:
#         #     sumsum += float(i)
#         sumsum = sum(num_list)
#         div = len(num_list)
#         aver = sumsum / div
#         print(f"Average of {num_list} is {aver}")

list_numbers = []


while True:
    user_input = input(
        "Please enter numbers(separated by comma) or 'q' to quit: ")
    if user_input == "q":
        print("You quit")
        break

    else:
        list_numbers.append(float(user_input))
        sorted_number_list = sorted(list_numbers) 
        # if we did not need original order
        # then we could have used list_numbers.sort() instead
        average_calculated = sum(list_numbers) / len(list_numbers)
        print(
            f"Numbers you entered are: {list_numbers} , average is: {average_calculated}")

        print(f"Top 3 values you enetered are: {sorted_number_list[-3:]}")
        print(f"Bottom 3 values you entered are: {sorted_number_list[:3]}")