# entered_numbers = input("Enter several numbers (comma separated):")
# if entered_numbers == "q":
#     print("You decided to quit")
# else:
#     numbers_list = entered_numbers.split(",")
#     summa = 0
#     for i in numbers_list:
#         summa += float(i.strip()) # now you can enter numbers with as much whitespace as you want
#
#     average = summa / len(numbers_list)
#     saraksts = ", ".join(numbers_list)
#     print(f"You did enter these numbers: {saraksts} and average of those is: {average}")
#     print(numbers_list.sort()) # THIS is INPLACE sorts returns None this will be alphabetical not numeric sort!
#     print(numbers_list)


list_numbers = []

while True:
    user_input = input("Input a number or 'q' to quit: ")
    if user_input.lower() == 'q':
        print("Thank you! Exiting")
        break
    else:
        list_numbers.append(float(user_input))
        print(f"All numbers: {list_numbers}\nAverage is {sum(list_numbers) / len(list_numbers):.2f}")
        print(f"BOTTOM 3 {sorted(list_numbers)[:3]}")
        print(f"TOP 3 {sorted(list_numbers)[-3:]}")
