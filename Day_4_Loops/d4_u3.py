num=input("Please write a number:")
num=int(num)
not_prime = False
if num > 1:
    # check for factors
    for i in range(2, num):  # TODO optimize this part a bit you could go to int(num**0.5)+1
        if num % i == 0:
            # if factor is found, set flag to True
            not_prime = True
            print(f"{num} dividies by {i}, thus not a prime")
            # break out of loop
            break # we do not need check, if say 21 divides by 3 we do not need to check if it divides by 7

    # check if flag is True
if not_prime:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")