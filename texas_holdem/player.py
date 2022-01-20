import deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()


def main():
    game_deck = deck.Deck()
    print("----- bob ----------")
    bob = Player("Bob")
    bob.draw(game_deck)
    bob.show_hand()
    print("----- bob ----------")

if __name__ == '__main__':
    main()
