# this time we will make a nim game using class based approach

# we will use a class to keep track of the state

# we will call our game class NimGame

# we create a class (a blueprint) using the class keyword
# this game class will store the state of the game
# and will provide methods to interact with the game

# with class based approach
# functions are called methods and live inside the class

# TODO have a class to manage database interactions

import random

# we could have created a general Player class

# for now we will add a ComputerPlayer class
class ComputerPlayer:
    # constructor


    def __init__(self, name, level=2):
        self.name = name
        self.level = level # how smart is our computer player?

    # i am using _ for our strategy methods
    # because we do not want to call them directly
    # we will call them from get_move method !
    # technically we could call them directly from outside the class
    # single _ is a convention to indicate that a method is private
    # if we really wanted to hide our methods we could use double __

    def _fixed_strategy(self):
        return 2 # really bad strategy

    def _random_strategy(self,min_remove, max_remove):
        return random.randint(min_remove, max_remove)

    def _smart_strategy(self, match_count, min_remove, max_remove):
        # https://en.wikipedia.org/wiki/Nim
        # so if we have one match left we can remove it and we lose
        # if we have two matches left we can remove one and we win!
        # if we have three matches left we can remove two and we win!
        # if we have four matches left we can remove three and we win!

        # so we will use module/remainder operator to check if we have a winning move
        # if we have a winning move we will take it
        # if we do not have a winning move we will take a random move
        reminder = match_count % (max_remove + 1)
                # let's refactor our strategy using match syntax in Python 3.10
        match reminder:
            case 0: # we win
                return max_remove # 3
            case 1: # we lose if we remove one match
                return random.randint(min_remove, max_remove)
            case 2: # we win
                return 1 # so opponent will be left with one match
            case 3: # we win
                return 2 # so opponent will be left with one match again
            # default case, here we do not need it because we covered all cases
            # case _: 
            #     return None # return someting in default case
        # match syntax is very useful for pattern matching
        # https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching
        # tutorial on pattern matching
        # https://realpython.com/python-3-10-new-features/#structural-pattern-matching-with-match

    # we will add a method to get the number of matches to remove
    # for now we will just return a random number
    def get_move(self, match_count, min_remove, max_remove):
        match self.level:
            case 1:
                return self._fixed_strategy()
            case 2:
                return self._random_strategy(min_remove, max_remove)
            case 3:
                return self._smart_strategy(match_count, min_remove, max_remove)
            # I could keep adding levels and strategies
        # so match syntax is just like using if elif else, but it is more readable
        # it is also more efficient because it does not evaluate all conditions
        # also it is more flexible because we can match on more than just numbers


class HumanPlayer:
    def __init__(self, name):
        self.name = name
    
    def get_move(self, match_count, min_remove, max_remove):
        while True:
            try:
                removed_matches = int(input("How many matches do you want to remove? "))
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


def return_players(default_computer_name="Alpha NIM"):
    # we will use a function to return the players
    # we will use a while loop to keep asking for input until we get a valid input
    while True:
        player_a_name = input("Enter player A name: ")
        player_b_name = input("Enter player B name or enter 'computer' for computer player: ")
        if player_a_name == player_b_name:
            print("Players must have different names")
        else:
            break
    # we will use a tuple to return multiple values
    if player_b_name == "computer":
        # TODO add prompt for computer level - Homework for Thursday
        return (HumanPlayer(player_a_name), ComputerPlayer(default_computer_name))
    else:
        return (HumanPlayer(player_a_name), HumanPlayer(player_b_name))

# main guard - our main entry point
if __name__ == "__main__":
    # we create an instance (object) of the class
    # TODO read settings from a file such as match count, player names, etc.
    player_a, player_b = return_players() # so we can have a human vs human or human vs computer
    # in other words PvP or PvC - in gamer terms
    game = NimGame(player_a=player_a, player_b=player_b,match_count=21) # using default values
    game.play()
    # we could clean up by using del game
    # but python will clean up for us since we are closing the program anyway
    # TODO add multiple game functionality - Homework for Thursday

# so for medium size application functions are a good choice
# for large applications classes are a good choice
# of course you can mix and match

# sometimes functionality does not fit into a class so easily