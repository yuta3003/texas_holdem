
class Card:
    def __init__(self, suit: str, number: int):
        self.suit = suit
        self.number = number

    def suit(self):
        return self.suit

    def number(self):
        return self.number

    def show(self):
        print("{}{}".format(self.suit, self.number))


def main():
    card = Card('H', 1)
    card.show()


if __name__ == '__main__':
    main()
