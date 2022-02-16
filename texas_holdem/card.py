"""
Todo:
    - show()で表示するのを文字列から画像に変更する
"""
class Card:
    """class説明のタイトル
    classの説明文を記入

    Attributes:
        suit (string)   : cardオブジェクトのマークを保持します
        number (int)    : cardオブジェクトの数字を保持します
    """
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
        """関数説明のタイトル
        cardオブジェクトの数字を返します。

        Args:
            ace14 (bool)    : Trueなら14, FalseならA
        Returns:
            number (int)    : トランプの数字を返します
        """
        number = self.__number
        if ace14 and self.__number == 1:
            number = 14
        elif not ace14 and self.__number == 1:
            number = 1
        return number

    def show(self):
        print("{}{}".format(self.__suit, self.__number))
