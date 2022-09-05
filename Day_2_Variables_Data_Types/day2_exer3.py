# Write a program that asks user for temperature in Celsius and prints out this same temperature in Farenheit
# formula is: fahrenheit = 32+celsius*(9/5)
# PS Remember about data type conversion, also consider precision
precision = 4
# t = input("What is the temperature in Celsius?\n")
# t = float(t) # so we are using float because
t = float(input("What is the temperature in Celsius?\n")) # same as above two lines

t_fahrenheit = 32 + t * (9 / 5)
print("Current temperature in Celsius is", round(t, precision), sep=": ")
print(f"Current temperature in Celsius is: {round(t, precision)}")
# so three ways of formatting results here
print("Current temperature in Fahrenheit is", round(t_fahrenheit, precision), sep=": ")
print("Current temperature in Fahrenheit is: " + str(round(t_fahrenheit, precision))) #need to cast to str
print(f"Current temperature in Fahrenheit is: {round(t_fahrenheit, precision)}") # my favorite
# also there is a way to format inside strings without round
