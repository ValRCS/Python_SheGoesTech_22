# this time we will make a nim game using class based approach

# we will use a class to keep track of the state

# we will call our game class NimGame

# we create a class (a blueprint) using the class keyword
# this game class will store the state of the game
# and will provide methods to interact with the game

# with class based approach
# functions are called methods and live inside the class

# TODO we could use more classes to store data about the players for one
# we could have a class to manage database interactions

import random
# we could have created a general Player class

# for now we will add a ComputerPlayer class
class ComputerPlayer:
    # constructor


    def __init__(self, name):
        self.name = name

    # we will add a method to get the number of matches to remove
    # for now we will just return a random number
    def get_move(self, match_count, min_remove, max_remove):
        # this is a very random computer player :) does not care about match_count...
        # TODO come up with a better strategy for the computer player
        # hint there is a winning strategy for nim 
        # in case you are interested in learning more about nim
        # https://en.wikipedia.org/wiki/Nim
        # if computer is losing it should try to make a random move to confuse the player
        return random.randint(min_remove, max_remove)


class HumanPlayer:
    def __init__(self, name):
        self.name = name
    
    def get_move(self, match_count, min_remove, max_remove):
                # notice we immediately cast to integer
        # TODO handle errors - it is very typical to add TODOS when writing code
        # so we enter an infinite loop
        # forcing the user to enter a valid input
        # we could also offer an option to quit
        while True:
            try:
                removed_matches = int(input("How many matches do you want to remove? "))
                # TODO get rid of magic numbers
                if removed_matches >= min_remove and removed_matches <= max_remove:
                    return removed_matches
                else:
                    # this is a candidate for another method once it starts growin beyond a few lines
                    allowed_moves = f"between {min_remove} and {max_remove}"
                    move_list = list(range(min_remove, max_remove + 1))
                    print(f"Allowed moves are {allowed_moves} or {move_list}")
                    print(f"Current match count is {match_count}")
            except ValueError: # means our conversion to int failed
                print("Please enter a number")

    # TODO save move history

class NimGame:
    # constructor
    # we will use some default values as well
    # if you expect more than two players
    # you would use a tuple or list to store the names
    def __init__(self, player_a, player_b, match_count=21, player_a_starts=True, min_matches=1, max_matches=3):
        self.match_count = match_count
        # TODO add heap functionality - that is keep track of multiple heaps and allow players to remove from any heap
        self.is_player_a_turn = player_a_starts
        self.min_matches = min_matches
        self.max_matches = max_matches
        self.player_a = player_a
        self.player_b = player_b
        print("Player A is", self.player_a.name)
        print("Player B is", self.player_b.name)
        print("Ready to play Nim!")

    # we will use a method to get the player name
    def get_player_name(self):
        if self.is_player_a_turn:
            return self.player_a.name
        else:
            return self.player_b.name

    # we will use a method to get the player input
    def get_player_input(self):
        if self.is_player_a_turn:
            # we could pass a whole NimGame object to the player if you have too many arguments
            return self.player_a.get_move(self.match_count, self.min_matches, self.max_matches) # we need to pass some data to the player
        else:
            return self.player_b.get_move(self.match_count, self.min_matches, self.max_matches)  # we need to pass some data to the player

    # we will use a method to update the state
    def update_state(self, removed_matches):
        self.match_count -= removed_matches
        self.is_player_a_turn = not self.is_player_a_turn

    # we will use a method to print the state
    def print_state(self):
        print(f"There are {self.match_count} matches left")

    # we will use a method to print the player turn
    def print_player_turn(self):
        print(f"{self.get_player_name()}'s turn")

    # we will use a method to print the winner
    def print_winner(self):
        if self.is_player_a_turn:
            print(f"{self.player_a.name} wins!") # a because we already switched the turn
            # TODO add a method to save the winner to the database
        else:
            print(f"{self.player_b.name} wins!") 

    # we will use a method to play the game
    def play(self):
        # main game loop
        while self.match_count > 0:
            self.print_player_turn()
            self.print_state()
            removed_matches = self.get_player_input()
            self.update_state(removed_matches)

        self.print_winner()

# main guard - our main entry point
if __name__ == "__main__":
    # we create an instance (object) of the class
    # we call the constructor
    # we pass the arguments to the constructor
    # game = NimGame(21, True) # those are the defaults so we don't need to pass them
    # TODO create players
    # player_a = HumanPlayer("Valdis")
    # player_b = HumanPlayer("Vitautas")

    player_a = HumanPlayer("Valdis")
    player_b = ComputerPlayer("Alpha Nim") # Google made AlphaGo and AlphaZero for chess and Go

    game = NimGame(player_a=player_a, player_b=player_b) # using default values
    game.play()
    # we could clean up by using del game
    # but python will clean up for us since we are closing the program anyway

# so for medium size application functions are a good choice
# for large applications classes are a good choice
# of course you can mix and match

# sometimes functionality does not fit into a class so easily