# Exercise 1
import datetime

username = input("What is your username? ")
print(f"your username is: {username}")
age = int(input(f"{username}, what is your age? "))
left_till_100 = 100 - age
current_year = datetime.datetime.now().year
year_when_100 = current_year + left_till_100
print(f"{username}, you have {left_till_100} years left until 100")
print(f"You will be 100 years old in year {year_when_100}")
