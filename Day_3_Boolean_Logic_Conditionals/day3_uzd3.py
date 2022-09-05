# a = float(input("Enter number: "))
while True:
    first_number = input(f"Please enter first number: ")
    try:
        a = float(first_number)  # will throw exception if not a number
    except ValueError:
        print(f"Wrong number {first_number} format. Please enter in format xx.x")
        continue
    else:
        break

b = float(input("Enter number: "))
c = float(input("Enter number: "))

if a <= b <= c:
    print(a, b, c)
elif b <= c <= a:
    print(b, c, a)
elif b <= a <= c:
    print(b, a, c)
elif c <= a <= b:
    print(c, a, b)
elif c <= b <= a:
    print(c, b, a)
else:
    print(a, c, b)