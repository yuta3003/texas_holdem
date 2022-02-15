"""
Todo:
    - None
"""
class Field:
    """class説明のタイトル
    classの説明文を記入

    Attributes:
        community_card (list)   : cardオブジェクトをリストで保持します
    """
    def __init__(self):
        self.community_card = []

    def flop(self, deck):
        self.community_card.append(deck.draw_card())
        self.community_card.append(deck.draw_card())
        self.community_card.append(deck.draw_card())

    def turn(self, deck):
        self.community_card.append(deck.draw_card())

    def river(self, deck):
        self.community_card.append(deck.draw_card())

    def show_card(self):
        for card in self.community_card:
            card.show()
