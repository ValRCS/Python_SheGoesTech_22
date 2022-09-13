# 3. Primes Check if entered positive number is a prime number.

#  A prime number is a number that divides without remainder only by itself and 1.

# Hint: what numbers do we have to check?

 # 3. Primes Check if entered positive number is a prime number.

#  A prime number is a number that divides without remainder only by itself and 1.

# Hint: what numbers do we have to check?

n=int(input("Please enter a positive number to check if it is prime "))
# is_prime=True # so flag based approach

# for i in range(2,n):
#     if n%i == 0 and i !=n:
#         print(f"Sorry {n} is not a prime number because it divides by {i}")
#         is_prime=False
#         break # no need to check further

# if is_prime is False:
#     print(f"{n} is not a prime number")
# else:  
#     print(f"{n} is a prime number")


# for i in range(2, n): # so n-1 is clearly sufficient but can we do better?
for i in range(2, int(n**0.5)+1): # so we check only up to and including square root of n
    if n % i == 0:
        print(f"{n} is not a prime number.")
        print(f"Sorry {n} is not a prime number because it divides by {i}")
        break
else: # this is executed if the for loop is not broken out of with break
    print(f"I am sure that {n} is a prime number!")
