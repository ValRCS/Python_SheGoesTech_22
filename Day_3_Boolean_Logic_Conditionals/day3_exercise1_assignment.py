# 1. Health check

# Ask user for their temperature.

# If the user enters below 35, then output "not too cold"

# If 35 to 37 (inclusive), output "all right"

# If the temperature  over 37, then output  
# "possible fever

# remember about type conversion if needed

# UPPERCASE is used for constants, but those are not really constants in Python
COLD_TEMP = 35
NORMAL_TEMP = 37
# we can use input to get user input
# temp = float(input("What is your temperature? "))
temp = int(float(input("What is your temperature? "))) # if you want to be sure you get an integer
# temp = int(input("What is your temperature? ")) # it will throw error if we enter non-integer
# FIXME: add your code here
# if 35 < temp < 37:
#     print("All right!", temp)

# if 35 > temp:
#     print("Not too cold", temp) 
# else:
#     print("Possible fever!", temp)

# text = "possible fever" # so our default message is fever
# if temp < 35:
#     text= "not too cold"
# elif temp <= 37:   
#     text= "all right"
# else:
#     text= "possible fever" # this would work too

# print(f"Temperature:  {temp} : {text}")

# if temp < COLD_TEMP:
#     print("not too cold", temp)
# # elif temp >=35 and temp <=37: # would work as well
# elif COLD_TEMP <= temp <= NORMAL_TEMP:
# # elif 35 <= temp <= 37: # here we already know our temp is 35 or more
# # elif temp <= 37: # here we already know our temp is 35 or more
#     print("all right", temp)
# else:  # so temp is over 37
#     print("possible fever", temp)

# so this is what I would write
if temp < COLD_TEMP:
    print("not too cold", temp)
elif temp <= NORMAL_TEMP:  
    print("all right", temp)
else:  # so temp is over 37
    print("possible fever", temp) 

# if you did not know about elif and else
# you could do the task with 3 if statements
# they are not exclusive so you need to pay attention to conditions
if temp < 35:
    print("not too cold", temp)
if temp >= 35 and temp <= 37:
    print("all right", temp)
if temp > 37:
    print("possible fever", temp)

# for testing you would want to check
# temp = 0 # here zero is not imporant but often it is a crucial edge case
# temp = 34.9
# temp = 35
# temp = 35.1
# temp = 37
# temp = 37.1
