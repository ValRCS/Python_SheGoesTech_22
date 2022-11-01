# nim is an ancient game of strategy in which two players take turns removing objects from distinct heaps.
# wiki on nim
# https://en.wikipedia.org/wiki/Nim

# first we will make a simple game of nim

# we need to keep track of two states
# 1. the number of objects in each heap - for now just one heap
# 2. the current player
match_count = 21
is_player_a_turn = True

# first implementation is a simple while loop
# game loop is very typical
# also could be a infinite loop with a break statement
while match_count > 0:
    if is_player_a_turn:
        print("Player A's turn")
    else:
        print("Player B's turn")
    # current match count
    print(f"There are {match_count} matches left")
    # for now there is no limit on how many matches can be removed
    # we will add that later
    match_count -= int(input("How many matches do you want to remove? "))
    # we use negation to switch the turn
    is_player_a_turn = not is_player_a_turn

if is_player_a_turn:
    print("Player A wins!")
else:
    print("Player B wins!")

# plenty of improvements can be made
# 1. add a limit on how many matches can be removed
# 1.b ask players for their names
# 2. use multiple heaps
# 3. add a computer player
# 4. add a GUI
# 5. add a computer player that uses a strategy
# 6. save data on the number of wins for each player in a database

# coding style wise we will need some more functions
# we could also use class based approach

