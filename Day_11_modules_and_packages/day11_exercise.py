# 1. The Shuffle

# write  a function get_shuffled_cards()

# Inside the function create  a 52-card list of tuples [("2", "diamonds ♦"), ("2", "hearts ♥"), ....., ("A", "spades ♠"), ("A", "clubs ♣")]

# The function returns a shuffled set of cards - the same list with tuples but shuffled!

# Find the correct method from built in random library.

# you can use a loop or use something from the library

# BONUS: Something can be useful from here: https://docs.python.org/3/library/itertools.html



# 2. Deck - probably for homework, see how far you get

# write a class Deck with the following attributes(variables)

# available - contains list of card tuples that can be used

# spent - contains list of card tuples that have been used

# there should be following methods:

# constructor (__init__) method

# initializes available with full 52 card list of tuples

# initializes spent with empty list

# shuffle(self):

# # shuffles available cards - works just like 1st function but works on available

# get_cards(self, count=1):
# # gets some number(default 1) of cards from available 
# adds these cards to spent
# returns these cards

# # you can add other methods and/or attributes if you wish to Deck class

# example usage:
# my_deck = Deck()
# print(my_deck.available) # 52
# print(my_deck.spent) # 0
# my_deck.shuffle() # shuffles available
# print(my_deck.available) # 52
# print(my_deck.spent) # 0
# my_cards = my_deck.get_cards(5) # gets 5 cards from available
# print(my_cards) # 5 cards like (3, 'hearts ♥'), (6, 'diamonds ♦'), (3, 'spades ♠'), (5, 'clubs ♣'), (7, 'hearts ♥'
# single_card = my_deck.get_cards() # gets 1 card from available
# print(single_card) # 1 card like (4, 'diamonds ♦')
# print(my_deck.available) # 46 because we got 6 cards
# print(my_deck.spent) # 6 because we got 6 cards

# 3. create a new deck in a different .py file from where Deck() is located, that means use import !

# import random
# import itertools

# # def get_shuffled_cards():
# #     var1 = ["A", "Jack", "Queen","King"] + list(range(2,11))
# #     var2 = ["diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"]
# #     cards = list(itertools.product(var1, var2))
# #     # cards_random = random.sample(cards, len(var1)*len(var2))
# #     cards_random = random.sample(cards, len(cards))
# #     return cards_random

# # print(get_shuffled_cards())
# # my_cards = get_shuffled_cards() # this will be a different list than the one above
# # print(len(my_cards)) # should be 52
# # print(len(set(my_cards)))  # so this is a set of unique cards should be 52

# # def get_shuffled_cards():
# #     my_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
# #     my_cards = ["diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"]
# #     # product using list comprehension
# #     cards = [(value, suit) for value in my_values for suit in my_cards]
# #     random.shuffle(cards)
# #     return cards

# # def get_shuffled_cards():
# #     ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] 
# #     suits = ["diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"]
# #     # this approach would be useful if you needed to add some extra logic
# #     card_deck=[]
# #     for i in suits:
# #         for j in ranks:
# #             pair = (j, i)
# #             card_deck.append(pair)
    
# #     shuffled = random.sample(card_deck, len(card_deck))
# #     return shuffled # so we return a list of tuples

# def get_shuffled_cards():
#     symbol = [2,3,4,5,6,7,8,9,10,"J","Q","K", "A"]
#     colors = ['heart', 'diamonds', 'spades', 'clubs']
#     cards = [(s, c) for s in symbol for c in colors]
    
#     random.shuffle(cards) # this shuffles cards in place
#     return cards


# # if __name__ == "__main__": is useful when you want to offer a module for import
# #  but also want to be able to run it as a standalone program
# if __name__ == '__main__':
#     cards = get_shuffled_cards()
#     print(cards[:5])