from src import deck

class Field:
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


def main():
    game_deck = deck.Deck()
    print("----- field ---- flop ------")
    field = Field()
    field.flop(game_deck)
    field.show_card()
    print("----- field ---- flop ------")
    print("----- field ---- turn ------")
    field.turn(game_deck)
    field.show_card()
    print("----- field ---- turn ------")
    print("----- field ---- river ------")
    field.river(game_deck)
    field.show_card()
    print("----- field ---- river ------")

if __name__ == '__main__':
    main()
