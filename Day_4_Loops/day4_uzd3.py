######   3   #######
number = 0
is_prime_number = True # so default value is True
while True:
    a = input("Enter a positive number or q to quit: ")
    if a == "q":
        break

    try:
        number = int(a)
    except ValueError:
        print("Please enter a number")
        continue

    if number > 0:
        for i in range(2, number): # actually we only need to check to square root of number + 1
            if number % i == 0:  # so we check if number is divisible by i
                is_prime_number = False
                print("Number is not prime it is divisible by", i)
                break # no need to check anymore we break out of for loop
        if is_prime_number:
            print("Is a prime number")
            break
        else:
            print("Is not a prime number")
            break
