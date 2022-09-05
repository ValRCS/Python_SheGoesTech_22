# 4. Prime numbers -
# this could be a weekend assignment, there is hardly enough time in class
#
# Find and output the first 20 (even better option to choose how many first primes we want) prime numbers in the form
# of a list i.e. [2,3,5,7,11, ...]


def primes():
    prime_list = []
    max_num = int(input("Enter how many primes should be listed: "))
    current_number = 1

    while len(prime_list) < max_num:
        current_number += 1
        for i in range(2, int(current_number**0.5)+1):  # reused code from lesson 4 we only need to check until sqrt
            if (current_number % i) == 0:
                print(f"{current_number} divides by {i} thus it is not prime..")
                break
        else:  # this else is not for if bu it is for the for loop when it ends normally(without a break)
            prime_list.append(current_number)
    print(f"Primes: {prime_list}")


primes()
