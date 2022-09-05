# Martins KLavins
# day-11
import random
import itertools


def get_shuffled_cards():
    symbols = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    symbols = [str(t) for t in symbols]
    suits = ["diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"]
    # cards = list(itertools.product(symbols, suits))
    # classical double loop approach
    # cards = []
    # for symbol in symbols:
    #     for suit in suits:
    #         cards.append((symbol, suit))
    # 3rd approach
    cards = [(value, suit) for value in symbols for suit in suits]

    random.shuffle(cards)
    return cards


if __name__ == '__main__':
    cards = get_shuffled_cards()
    print(cards[:5])
    print(cards[-5:])
