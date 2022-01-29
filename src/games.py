from src import deck
from src import field
from src import player
from src import role


class Game:
    """
    メインゲーム

    Examples
    --------
    >>> game = Game()
    >>> game.progress() # ゲームスタート
    """

    def __init__(self, number_of_players=2):
        self.number_of_players = number_of_players
        self.players = []
        self.game_deck = deck.Deck()
        self.game_field = field.Field()
        self.game_role = role.RoleJudge()

    def deal(self):

        # プレイヤー作成
        for i in range(self.number_of_players):
            self.players.append(player.Player('player' + str(i+1)))

        for i in range(self.number_of_players):
            # TODO: スターティングハンド2を定数化
            for j in range(2):
                self.players[i].draw(self.game_deck)

    def preflop(self):
        pass

    def flop(self):
        self.game_field.flop(self.game_deck)

    def turn(self):
        self.game_field.turn(self.game_deck)

    def river(self):
        self.game_field.river(self.game_deck)

    def showdown(self):
        print(self.game_field.show_card())
        for i in range(self.number_of_players):
            print("Player Name: {}".format(self.players[i].name))
            print(self.players[i].show_hand())

    def role_judge(self):
        for i in range(self.number_of_players):
            hand = self.players[i].hand + self.game_field.community_card
            self.game_role.judge(hand)

    # ゲーム全体の進行
    def progress(self):
        self.deal()
        self.preflop()
        self.flop()
        self.turn()
        self.river()
        self.showdown()
        self.role_judge()


def main():
    game = Game()
    game.progress()


if __name__ == '__main__':
    main()
