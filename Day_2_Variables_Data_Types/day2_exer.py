import datetime  # generally import statements go at the top of the file
print("Today is", datetime.datetime.now())
# username = input("What is your username?")
# print(f"Nice to meet you {username}!")
# current_age = int(input(f"What is your age, {username}?"))
# b = 100
# c = b - current_age
# print(f"in {c} years you will be 100 years old \U0001F606")
# year_now = 2022
# year = year_now + c
# print(f"By {year} You will be {b}, Congrats!")


target_age = 100  # you could even make this uppercased to indicate it is a constant
# you could also ask user for target age

# Write a program that asks for and saves a username
username = input("what is your name? ")
# Ask a question about the user's age, using the username in the question.
age_now = input(f"what is {username} age ")
# age_now = float(age_now)
age_now = int(age_now)  #round would be another possibility
# Shows in how many years the user will be target_age years old smile

years_to_go = target_age - age_now
age_after = print(f"{username} will be {target_age} years old after",
                  years_to_go, "years")
# BONUS:
# then you will need two additional lines:
# import datetime # let's talk about imports separately


current_year = datetime.datetime.now().year
target_year = current_year + years_to_go

# currentYear = datetime.datetime.now (). yearLet the program also show the year when the user will be 100 years old.
print(f"{username} will be {target_age} years old in the year {target_year} 🤩")
