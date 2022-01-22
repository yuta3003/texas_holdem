import deck
import field
import player

class Game:
    def __init__(self, number_of_players=2):
        self.number_of_players = number_of_players
        self.players = []

    def deal(self):
        game_deck = deck.Deck()
        game_field = field.Field()

        # プレイヤー作成
        for i in range(self.number_of_players):
            self.players.append(player.Player('player' + str(i+1)))

        for i in range(self.number_of_players):
            # TODO: スターティングハンド2を定数化
            for j in range(2):
                self.players[i].draw(game_deck)

    def preflop(self):
        pass

    def flop(self):
        pass

    def turn(self):
        pass

    def river(self):
        pass

    def show(self):
        for i in range(self.number_of_players):
            print(self.players[i].name)
            print(self.players[i].show_hand())

    # ゲーム全体の進行
    def progress(self):
        self.deal()
        self.preflop()
        self.flop()
        self.turn()
        self.river()
        self.show()

def main():
    game = Game()
    game.progress()

if __name__ == '__main__':
    main()
