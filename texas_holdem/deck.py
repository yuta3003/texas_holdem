"""
Todo:
    - None
"""
import random

from texas_holdem import (
    card,
)


class Deck:
    """class説明のタイトル
    classの説明文を記入

    Attributes:
        cards (list)    : cardオブジェクトをリストで保持します
    """
    def __init__(self):
        self.__cards = []
        self.build()
        self.shuffle()

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, cards):
        self.__cards = cards

    def build(self):
        for i in ["C", "D", "H", "S"]:
            for j in range(1, 14):
                file_dir = "./images/"
                file_name = str(i) + str(j) + ".png"
                file_path = file_dir + file_name
                self.__cards.append(card.Card(i, j, file_path))

    def shuffle(self):
        random.shuffle(self.__cards)

    def show(self):
        for c in self.__cards:
            c.show()

    def draw_card(self):
        return self.__cards.pop()
