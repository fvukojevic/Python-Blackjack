import random


class Deck:

    def __init__(self):
        self.cards = []

    def shuffle(self):
        random.shuffle(self.cards)

    def hit(self):
        return self.cards.pop()
