# print FizzBuzz
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# 02.03.2022

print("\n___________Exercise 1 ________________\n")

# if number divided by 5 then Fizz If divided by 7 then Buzz,
# If divided by 5 AND 7 then FizzBuzz otherwise the same number

# for i in range(1, 101):
#     if i % 5 == 0 and i % 7 == 0:
#         print("FizzBuzz", end=",")
#     elif i % 5 == 0:
#         print("Fizz", end=",")
#     elif i % 7 == 0:
#         print("Buzz", end=",")
#     else:
#         print(i, end=",")

FIZZ = 5
BUZZ = 7
start = 1
the_end = 100
# for n in range(start, the_end):
#     print(n,end="")
fizz_buzz = ""  # we start with an empty string
# so fizz_buzz will be a buffer
for i in range(1,101):
    if i%5==0:
        fizz_buzz += "Fizz"
    if i%7==0:
        fizz_buzz += "Buzz"
    if not (i%5==0 or i%7==0):
        fizz_buzz += str(i)
    if i!=100:
        fizz_buzz += ","
print(fizz_buzz)