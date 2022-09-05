import datetime  # 1. Exercise - Age 100

#
# Write a program that asks for and saves a username
# Ask a question about the user's age, using the username in the question.
# Shows in how many years the user will be 100 years old smile
# BONUS: Let the program also show the year when the user will be 100 years old.
# It could use a variable with the current year.
# It would be even better to get the current year automatically
# then you will need two additional lines:
# import datetime # let's talk about imports separately
# currentYear = datetime.datetime.now (). year
username = input("What is your name?")
print(f"{username}, you have a nice name!")
age = int(input(f"{username}, how old are you?"))
target_age = 65
birthday = target_age - age
print(f"{age} years old! Nice! After {birthday} years you will be {target_age} years old :)")
currentYear = datetime.datetime.now().year  # you could write it by hand here 2021, but better to get it automatically
year = currentYear + birthday
print(f"You will be {target_age} in year: {year}")
