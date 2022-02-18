"""
Todo:
    - None
"""
from texas_holdem import (
    deck,
    field,
    player,
    role,
    winner,
)


class Game:
    """class説明のタイトル
    classの説明文を記入

    Attributes:
        cards (list)    : cardオブジェクトをリストで保持します

    Examples:
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
        flop_card = self.game_field.community_card
        return flop_card

    def turn(self):
        self.game_field.turn(self.game_deck)
        turn_card = self.game_field.community_card[-1]
        return turn_card

    def river(self):
        self.game_field.river(self.game_deck)
        river_card = self.game_field.community_card[-1]
        return river_card

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
            return 'Draw'
        else:
            print(self.players[winner_index].name)
            return self.players[winner_index].name

    # ゲーム全体の進行
    def progress(self,
            preflop=False,
            flop=False,
            turn=False,
            river=False,
            winner=False):
        self.deal()
        self.preflop()
        flop_card = self.flop()
        turn_card = self.turn()
        river_card = self.river()
        self.showdown()
        self.judge_role()
        winner_player = self.judge_winner()
        if preflop:
            pass

        if flop:
            return flop_card

        if turn:
            return turn_card

        if river:
            return rever_card

        if winner:
            return winner_player


def main():
    game = Game()
    winner = game.progress(winner=True)
    print("勝者:", winner)


if __name__ == '__main__':
    main()
