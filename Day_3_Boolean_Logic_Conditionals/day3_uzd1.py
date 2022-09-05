#Exercise 1
temp = float(input("What is your temperature?"))
if temp < 35:
    print("not too cold")
elif 35 <= temp <= 37:
    print("all right")
else: # if a == 10
    print("possible fever")