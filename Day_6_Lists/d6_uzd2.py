while True:
    n1=int(input("enter integer start:"))
    n2=int(input("enter integer end:"))
    if n1>n2:
        print("n1 should be less then n1, Try again1")
        continue
    break

numbers=list(range(n1,n2+1))
# cubes=[n**3 for n in numbers] # list comprehension
# loop version of above list comprehension
cubes=[]
for n in numbers:
    cubes.append(n**3)
# use loop version when logic is more complex

for n,c in zip(numbers,cubes):
    print(f"{n} cubed:{c}")
print(cubes)