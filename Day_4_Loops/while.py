# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# # we can use while loop to print the same line 5 times
# # this can heat up the computer ...
# while True:
#     print("Do you want to continue?")
#     print("Hello")

# so above infinite loop actually can be stopped by pressing Ctrl+C
# infinite loops are used in games, for example, or any application as the main loop

# i = 0  # so caller iterator, or index if you will
# while i < 5:  # while loops are for indeterminate time
#     print("Hello") # do not have to use i 
#     print("Hello No.", i)
#     print(f"Hello Number {i}")
#     print(f"{i} squared is {i**2}")
#     # it is crucial that we increment the iterator
#     # otherwise we will get an infinite loop
#     i += 1  # i = i + 1 # we will have a infinite loop without i += 1, there is no i++
# # while loop is finished here
# print("Always happens once loop is finished")
# print("i is now", i)
# # #
# i = 10
# while i >= 0:
#     print("Going down the floor:", i)
#     # i could do more stuff
#     if i == 0:
#         print("Cool we reached the garage")
#     i -= 5  # i = i - 1
# # once we are done with the above loop    
# print("Whew we are done with this i floor:", i)
# what will be the value of i at the end of the above loop?

# # # #
# total = 0 # do not use sum as name for variable, because sum is a built in function
# i = 20
# print(f"BEFORE loop i is {i} total is {total}")
# while i <= 30:
#     # we add current value of i to total
#     total += i # total = total + i 
#     print(f"After adding {i} total is {total}")
#     i += 2 # step will be 2 here
# print(f"i is {i} total is {total}")
# #
# # # # general loop with start, stop, step
# start = 50
# stop = 400
# step = 125  # we do have a for loop for this type of looping but step here can be a float
# i = start  # initialization
# while i <= stop:  # you could also stop before stop is reached then use  i < stop
#     print(i)
#     print(f"i is {i}")
#     i += step  # we add step to i
# # # # #
# print("After exiting loop i is ", i)
# #
# # # start = 10
# # # end = 500
# # # step = 1
# # # increase = 30
# # #
# # # i = start
# # # while i <= end:
# # #     print(f"i is {i}")
# # #     step += increase  # increasing the increase sort of like incrase in speed
# # #     print("Step is now", step)
# # #     i += step
# #
# # # in general while loops are best suited for loops when we are not 100 % sure of when they will end
# # # so sort of indeterminate
# #
# # # # #
# i = 10_000_000
# while True:  # so i am saying here that this loop should run forever .. unless I have something inside to break out
#     print("i is", i)  # this line will always happen at least once
#     # could add more lines which will run at least once
#     # in a while True loop it is typical to check for exit condition
#     if i >= 14:  # similar to while i < 28:
#         print("Ready to break out i is", i)
#         break  # with break we break out of inner loop (here we only have one loop)
#     i += 2
# # # # # above is simulating do while looping functionality
# print("Whew AFTER BREAK out", i)

# the above simulate a do while loop
# do while loops do something at least once and then check for exit condition
# do while loops are not in python but easily simulated with while True and break
# think of do while loops as shoot first ask questions later

# # # #
# # i = 20
# # is_active = True  # we will use this as a flag
# # is_raining = True
# # # while active or is_raining:  # careful here so for while loop to keep running here JUST ONE of the conditions here have to be true
# # while is_active and is_raining:  # so for while loop to keep running here BOTH conditions here have to be true
# #     print(f"Doing stuff with {i}")
# #     i += 3
# #     # TODO update weather conditions so update is_raining
# #     if i > 30:
# #         is_active = False
#         # I could have used break as well
#     # with flag set I can still do some work here
# # # # #
# # continue goes to the top of the loop
while True:
    res = input("Enter number or q to quit ")
#     if res.lower().startswith("q"): # more lenient any word starting with Q or q will work to quit
    if res == "q":
        print("No more calculations today. I am breaking out of the loop.")
        break
    elif len(res) == 0:  # so i had an empty string here...
        print("Hey! You just pressed Enter, please enter something...")
        continue # we go back to line 83 and start over
    # elif res == "a":  # TODO check if if the input is text
    elif res[0].isalpha():  # we are checking here for the first symbol of our input
        print("I can't cube a letter ")
        continue # means we are not going to try to convert "a" to float
        # in other words we are not going to do the below 4 instructions
    num = float(res)
    cube = num**3
    cube = round(cube, 2) # 2 digits after comma
    print(f"My calculator says cube of {num} is {cube}")
# # #
print("All done whew!")
# # #
# # # # outer_flag = True
# # # # inner_flag = True
# # # # i = 10
# # # # while outer_flag:
# # # #     print(i)
# # # #     while inner_flag:
# # # #         res = input("Enter q to quit")
# # # #         if res == 'q':
# # # #             print("got q lets break from inside")
# # # #             break
# # # #     i += 1
# # # #     if i > 14:
# # # #         print("outer break about to happen")
# # # #         break
# # # # #
# # # # #
# # # # #
# # # # #
# # #
# # i = 5
# # while i < 10:
# #     print(i)
# #     i += 1  # this will be bugged think about the even case....
# #     if i % 2 == 0:   # i am testing whether some number has a reminder of 0 when divided by 2
# #         print("Even number", i)
# #         # continue  # we skip the following loop instructions
# #     else:  # this will perform just like continue
# #         print("Doing something with odd number", i)
# #         # i += 1  # this will be bugged think about the even case...
# #     print("We do something here")   # with continue this would not run