import random

from src import (
    card,
)


class Deck:
    def __init__(self):
        self.__cards = []
        self.build()
        self.shuffle()

    def cards(self):
        return self.__cards

    def build(self):
        for i in ["C", "D", "H", "S"]:
            for j in range(1, 14):
                self.__cards.append(card.Card(i, j))

    def shuffle(self):
        random.shuffle(self.__cards)

    def show(self):
        for c in self.__cards:
            c.show()

    def draw_card(self):
        return self.__cards.pop()
