import random


def shuffle(cards):
    for i in range(len(cards)):
        k = random.sample(range(i), 1)
        cards[k], cards[i] = cards[i], cards[k]

