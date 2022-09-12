# 2. Xmas Bonus

# The company has promised a Christmas bonus in the amount of 
# 15% of the monthly salary for EVERY year of 
# service over 2 years.

# Task. Ask the user for the amount of the monthly salary and
#  the number of years worked.

# Calculate the bonus.

# Example1: 5 years of experience, 1000 Euro salary,
#  the bonus will be 450 Euro.

# Example2: 1.5 years of experience, 1500 Euro salary, 
# no bonus(0)

# salary = int(input("What is your salary?"))
# years = int(input("How many years did you work?"))
# if years > 2:
#     bonus = salary*0.15*(years-2)
#     print("your bonus is ", bonus)
# else:
#     print("no bonus")

# years_of_service = input("how many years are you working here? ")
# years_of_service = float(years_of_service)
# if years_of_service > 2:
#     salary = input("what is your monthly salary? ")
#     salary = float(salary)
#     # so cast bonus to int to get rid of decimal places
#     # alternatively you could use round() function maybe round to 2 decimal places
#     bonus = int((years_of_service - 2) * salary * 0.15)
#     print("your bonus is", bonus)
# else:
#     print("no bonus")

monthly_salary = float(input("What is your montly salary? "))
years_worked = float(input("How many years have you worked here? "))
# these two variables could be read from database or file
bonus_rate = 0.15 # 15% bonus
bonus_threshold = 2

if years_worked < bonus_threshold:
    print("Your bonus amount is 0! Don't be sad, your bonus is coming next year, keep up the good work!")
else:
    # bonus_amount = (years_worked - 2) * monthly_salary * bonus_rate
    # bonus_amount = round(bonus_amount, 2) # let's hope our employees like round numbers with cents
    bonus_amount = round((years_worked - bonus_threshold) * monthly_salary * bonus_rate, 2) # same as above two lines
    print("Your bonus amount is", bonus_amount)
    print(f"Your bonus amount is {bonus_amount}") # I pefer this syntax
    # print("Your bonus comes up to " + str(monthly_salary * bonus_rate * years_worked)) # not quite right