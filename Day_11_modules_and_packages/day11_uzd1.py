# UZD 1
import random


def shuffling():
    symbols = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    suits = ["♦", "♥", "♠", "♣"]
    # extra = ["Joker"]
    [str(c) for c in symbols]
    cards = []
    for deck in symbols:
        for suit in suits:
            cards.append((deck, suit))
    random.shuffle(cards)
    return cards


cards = shuffling()
print(f"Full card deck:", cards[:52])
print(cards[:5])
