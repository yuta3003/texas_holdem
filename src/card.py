class Card:
    def __init__(self, suit: str = 'N', number: int = 0):
        self.__suit = suit
        self.__number = number

    @property
    def suit(self):
        return self.__suit

    @suit.setter
    def suit(self, suit):
        self.__suit = suit

    def number(self, ace14=False):
        number = self.__number
        if ace14 and self.__number == 1:
            number = 14
        elif not ace14 and self.__number == 1:
            number = 1
        return number

    def show(self):
        print("{}{}".format(self.__suit, self.__number))
