import random

import card


class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()

    def build(self):
        for i in ["C", "D", "H", "S"]:
            for j in range(1, 14):
                self.cards.append(card.Card(i, j))

    def shuffle(self):
        random.shuffle(self.cards)

    def show(self):
        for c in self.cards:
            c.show()

    def draw_card(self):
        return self.cards.pop()


def main():
    deck = Deck()
    deck.show()

if __name__ == '__main__':
    main()
