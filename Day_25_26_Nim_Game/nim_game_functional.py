# new verision of our game using functions and dictionary to keep track of the state
# in applications you will need to use some data structure to keep track of the state
# we could use multiple variables but that is not very flexible
# also it pollutes the global namespace 
# try to keep your global namespace as clean as possible

# note that there are other approaches , such as class based approach
# by using a single dictionary we can easily add more state variables
# and our functions are more flexible
# our global namespace is clean besides the state variable
# of course you can name it whatever you want
state = {
    "match_count": 21,
    "is_player_a_turn": True,
}

def get_player_name(is_player_a_turn):
    if is_player_a_turn:
        return "Player A"
    else:
        return "Player B"

def get_player_input():
    # notice we immediately cast to integer
    # TODO handle errors - it is very typical to add TODOS when writing code
    return int(input("How many matches do you want to remove? "))

# not a pure functional approach because we modify the state
def update_state(state, removed_matches):
    state["match_count"] -= removed_matches # same as state["match_count"] = state["match_count"] - removed_matches
    state["is_player_a_turn"] = not state["is_player_a_turn"] 
    # in a purely functional approach we would return a new state  

def print_state(state):
    print(f"There are {state['match_count']} matches left")

def print_player_turn(state):
    print(f"{get_player_name(state['is_player_a_turn'])}'s turn")

def print_winner(state):
    if state["is_player_a_turn"]:
        print("Player A wins!")
    else:
        print("Player B wins!")

def main():
    # by using functions we can easily add more functionality
    # we can also easily test our functions
    # we can also easily reuse our functions
    # we can also easily change our functions
    # we get documentation for free assuming our functions are well named
    while state["match_count"] > 0:
        print_player_turn(state)
        print_state(state)
        removed_matches = get_player_input()
        update_state(state, removed_matches)

    print_winner(state)

# main guard
if __name__ == "__main__":
    # we could add a config file and read the config file here
    main()
    # we could add a database and save the data here
    # and clean up any resources we used