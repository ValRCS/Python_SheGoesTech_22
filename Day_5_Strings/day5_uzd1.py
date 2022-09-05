# exercise 1

username = input("What is your name? ")
name_reversed_capitalized = username[::-1].capitalize()
first_letter = username[0].upper() # or capitalize() or even title()
print(f"{name_reversed_capitalized}, a thorough mess is it not {first_letter}?")