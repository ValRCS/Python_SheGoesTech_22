precision = 2
bonus = 0.15
service_min = 2

salary = float(input("What is your monthly salary? "))
# depends how lenient human resources department is in your company :)
years_worked = float(input("For how many years have you worked in the company? "))

if years_worked > service_min:
    bonus_amount = round(salary * bonus * (years_worked - service_min), 2)
    unrounded_bonus = salary * bonus * (years_worked - service_min)
    print(f"Your bonus is {bonus_amount} \nMerry Christmas!")
    print(f"Your unrounded bonus is {unrounded_bonus} - {unrounded_bonus:.3f}") # so we keep the rough data
else:
    print("Sorry, no Xmas bonus")