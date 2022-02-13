from texas_holdem import (
    deck,
    field,
    player,
    role,
    winner,
)


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

    def deal(self):

        for i in range(self.number_of_players):
            self.players.append(player.Player('player' + str(i+1)))

        for i in range(self.number_of_players):
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

    def judge_role(self):
        for i in range(self.number_of_players):
            self.game_role = role.Role()
            hand = self.players[i].hand + self.game_field.community_card
            self.game_role.judge(hand)
            self.players[i].role = self.game_role.role
            self.players[i].hand = self.game_role.hand

    def result_draw(self):
        print('Draw')

    def judge_winner(self):
        game_winner = winner.Winner(self.players)
        winner_index = game_winner.judge()
        if winner_index == -1:
            self.result_draw()
        else:
            print(self.players[winner_index].name)

    # ゲーム全体の進行
    def progress(self):
        self.deal()
        self.preflop()
        self.flop()
        self.turn()
        self.river()
        self.showdown()
        self.judge_role()
        self.judge_winner()


def main():
    game = Game()
    game.progress()


if __name__ == '__main__':
    main()
