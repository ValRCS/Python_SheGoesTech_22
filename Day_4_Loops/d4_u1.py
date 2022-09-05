start = 1
end_num = 40
fizz = 5
buzz = 7
for n in range(start, end_num+1):
    end = ","
    if n == end_num:
        end = "\n"
    if n % (fizz*buzz) == 0:  # alternative would be if i%fizz ==0 and i%buzz ==0:
        print("FizzBuzz", end=end)  # default in print is "\n"
    elif n % fizz == 0:
        print("Fizz", end=end)
    elif n % buzz == 0:
        print("Buzz", end=end)
    else:
        print(n, end=end)