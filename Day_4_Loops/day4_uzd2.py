c_symbol = "*"
height = 0
while True:
    a = input("Enter the height of the tree (positive number) or q for exit: ")
    if a == "q":
        break

    try:
        height = int(a)
    except ValueError:
        print("Please enter a number")
        continue

    for i in range(height):
        # print(c_symbol * (2 * i - 1))
        print(' ' * (height - i - 1) + c_symbol * (2 * i + 1))
