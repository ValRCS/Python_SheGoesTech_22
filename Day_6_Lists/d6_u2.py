
first = int(input("first number: "))
last = int(input("last number: "))
if first < last:
    # list comprehension
    cubed = [n**3 for n in range(first, last+1)]
    # list comprehensions are great but it is a bit tricky to print while creating a list comprehension
    print(cubed)
else:
    print("not gonna happen")

optional_list = []
# regular loop is a bit easier to do extra work such as printing some output
for n in range(first, last+1):
    cube = n**3
    print(f"{n} cubed: {cube}")
    optional_list.append(cube)
print(optional_list)