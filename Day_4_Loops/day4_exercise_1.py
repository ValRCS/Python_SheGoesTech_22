# # 1. FizzBuzz 

# Print a string 1,2,3,4, Fizz, 6, Buzz, 8, ..... 34, FizzBuzz, 36, .... to 97, Buzz, 99, Fizz 

# So if number divided by 5 then Fizz If divided by 7 then Buzz,
#  If divided by 5 AND 7 then FizzBuzz otherwise the same number

#  Note: such a task became popular as the first task to ask to determine 
#  whether a person knows about programming at all smile

# start = 1
# stop = 100
final_list = ""

# for i in range(start,end+1):

#     if i%5==0:
#         final_list += "FIZZ"
#     if i%7==0:
#         final_list += "BUZZ"
#     if not (i%5==0 or i%7==0):
#         final_list += str(i)
#     if i!=end:
#         final_list += "," #any other way to add comma?
#     # alternative would be to use list and join at the end but that is another lecture
# print(final_list)

# for i in range(1, 101):
#     if i % 5 == 0:
#         if i % 7 == 0:
#             print("FizzBuzz, ", end = "")
#         else:
#             print("Fizz, ", end = "")
#     elif i % 7 == 0:
#         print("Buzz, ", end = "")
#     else:
#         print(f"{i}, ", end = "")

start = 1
stop = 50
fizz = 3
buzz = 5
fizz_message = "Fizz"
buzz_message = "Buzz"

for n in range(start,stop+1):
    end = ", "
    if n == stop: # this is the last number
        end = ""

    if n%fizz == 0 and n%buzz == 0:
        print(fizz_message+buzz_message, end = end)
    elif n%fizz == 0:
        print(fizz_message,  end = end)
    elif n%buzz == 0:
        print(buzz_message, end = end)
    else:
        print(n, end = end)