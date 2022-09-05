height = int(input("Enter the height of the tree: "))
for i in range(height):
    print(' ' * (height - i - 1) + '*' * (2 * i + 1))  # x2 is always rounded up

a=height-1

for i in range(height):
  print(" "*a, end="")  # end here is nothing so we can continue printing
  print("*"*(2*i+1))
  a-=1 