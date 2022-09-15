# # 1. Confusion

# # The user enters a name.

# # You print user name in reverse (should begin with capital letter)
# #  then extra text: ",a thorough mess is it not ", then the first name of the user name then "?"

# # Example:

# # Enter: Valdis -> Output: Sidlav, a thorough mess is it not V?

# my_name = input("What is your name?")
# my_name_backwards = my_name[::-1]
# print(my_name_backwards.capitalize(),", a thorough mess is it not ",my_name[0]) # default separator is space

# name = input("Please enter your name: ")
# print(name[::-1].capitalize() + ", a thorough mess is it not, " + name[0] + "?")

name=input("Enter your name: ")
extra = ",a thorough mess is it not"

reversed_cap_name=name[::-1].capitalize() 
# print(reversed_name)
print(f"{reversed_cap_name} {extra} {name[0]}?")