class Player:
    def __init__(self, name='default name'):
        self.__hand = []
        self.__name = name
        self.__role = 0

    @property
    def hand(self):
        return self.__hand

    @hand.setter
    def hand(self, hand):
        self.__hand = hand

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role

    def draw(self, deck):
        self.__hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for card in self.__hand:
            card.show()


def main():
    pass


if __name__ == '__main__':
    main()
