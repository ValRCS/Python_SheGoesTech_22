# list_num = []
# while True:
#     number = input("Please input a number or quit by entering 'q': ")
#     if number == "q":
#         print("Quit")
#         break
#     elif number == "":
#         continue
#     number = float(number)
#     list_num.append(number)
#     print(f"Current number {list_num[-1]}")
#     average = sum(list_num) / len(list_num)
#     average = round(average, 2)
#     print(f"Average: {average}")
#     print(f"List of numbers so far {list_num}")

# 1a. Average value
# Write a program that prompts the user to enter numbers (float).
# The program shows the average value of all entered numbers after each entry.
# PS. 1a can do without a list
# 1b. The program shows both the average value of the numbers and ALL the numbers entered
# PS Exit the program  by entering "q"
# 1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.
print("1.Uzd_Vidējais starp skaitļiem")
numbers = input("Ievadi numurus katru atdalot ar "+'","'+"q-lai izzietu"+":")
if numbers == "q":
    print("You decided to quit")
else:
    number_list = numbers.split(",") # we have a list of strings here
    number_list = [float(i.strip()) for i in number_list] # we have a list of floats now
    # possibly strip is not needed we can use float(i)
    # total = 0
    # for n in number_list:
    #     total += float(n.strip())
    total = sum(number_list)
    average = total / len(number_list) # we could have used sum(number_list) directly here
print("1b. The program shows both the average value of the numbers and ALL the numbers entered")
print(f"{average} šis ir vidējais skaitlis")
print(f"Tevis ievadītie skaitļi: {number_list}")
print("1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.")
# preferably we would have used sorted() here and save it to a variable
sorted_list = sorted(number_list)  # i could have also overwritten the original list
print(f"Augšējie 3 {sorted_list[:3]}")
print(f"Apakšējie 3 {sorted_list[-3:]}")
print(f"{average} šis ir vidējais skaitlis")