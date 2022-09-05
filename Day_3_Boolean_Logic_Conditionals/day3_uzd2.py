bonus_percent = 0.15
years_without_bonus = 2
salary = float(input("enter your salary per month: "))
years_worked = float(input("enter number of years worked: "))

if years_worked > years_without_bonus:
    bonus = (years_worked - years_without_bonus) * salary * bonus_percent
    bonus = round(bonus, 2)
    print(years_worked, "years of experience", salary, "Euro salary, the bonus will be", bonus, "Euro")
else:
    print(years_worked, "years of experience", salary, "Euro salary, no bonus(0)")