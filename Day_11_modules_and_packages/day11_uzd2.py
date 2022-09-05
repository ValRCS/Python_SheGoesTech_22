import itertools
import string
import random


def get_shuffled_cards():
    suits = ["clubs (♣)", "diamonds (♦)", "hearts (♥)", "spades (♠)"]
    ranks = list(string.digits)[2:] + ["10", "A", "J", "Q", "K"]
    card_deck = list(itertools.product(ranks, suits))
    card_deck_s = random.sample(card_deck, len(card_deck))
    return card_deck_s


class Deck:
    suits = ["clubs (♣)", "diamonds (♦)", "hearts (♥)", "spades (♠)"]
    ranks = list(string.digits)[2:] + ["10", "A", "J", "Q", "K"]

    def __init__(self):
        self.available = list(itertools.product(self.ranks, self.suits))
        self.shuffle()
        self.spent = []

    def __str__(self):
        return f"Available cards: {self.available}\nSpent cards: {self.spent}"

    def shuffle(self):
        self.available = random.sample(self.available, len(self.available))
        return self

    def get_cards(self, count=1):
        cards = self.available[:count]
        self.spent.extend(cards)
        self.available = self.available[count:]
        return cards


if __name__ == "__main__":
    print(get_shuffled_cards())
    my_deck = Deck()
    my_deck.shuffle()
    print(my_deck)
    print(my_deck.get_cards(2))
    print(my_deck.get_cards(6))
    print(my_deck)
