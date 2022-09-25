# Find and output the first 20 
# (even better option to choose how many first primes we want) 
# prime numbers in the form of a list i.e. [2,3,5,7,11, ...
# so remember we already know how to find a single prime number 
# from previous exercise
# https://github.com/ValRCS/Python_SheGoesTech_22/blob/main/Day_4_Loops/day4_exercise_3.py

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# # ask for how many primes we want to find
# # we need to convert string to integer
# # we need to use int() function

# number_of_primes = int(input("How many primes do you want to find? "))

# # we need to create a list to store our primes
# prime_list = []

# # we need to create a counter to keep track of how many primes we have found
# # we need to start from 2 because 1 is not a prime number
# counter = 0
# number = 2
# while counter < number_of_primes:
#     if is_prime(number):
#         prime_list.append(number)
#         counter += 1
#     number += 1

# print(prime_list)

# prime_range = int(input("Enter how many prime numbers want in your list: "))
# start=int(input("Enter the start number for range: "))


def get_primes_list(prime_range=100, current=2):
    prime_list=[]
    counter=0
    while counter<prime_range:
        if is_prime(current):
            prime_list.append(current)
            counter+=1
        current+=1 
    return prime_list

# print(get_primes_list(prime_range, start))
primes_100 = get_primes_list()
print(primes_100)

print(get_primes_list(prime_range=1000))