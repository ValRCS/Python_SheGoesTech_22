# Exercise 1

temperature = float(input("What's your temperature?"))
if temperature < 35:
    print("not too cold")
elif temperature <= 37:  # so  inclusive same
    print("all right")
else:
    print("possible fever")
