from src import (
    player,
)


class Winner:
    def __init__(self, players):
        self.players = players
        self.winner_player = self.players[0]

    def check_number(self, player, enemy):
        winner_player = player
        for i in range(len(player.hand)):
            if player.hand[i] > enemy.hand[i]:
                winner_player = player
            elif player.hand[i] < enemy.hand[i]:
                winner_player = enemy
        return winner_player



    def judge(self):
        for i in range(1, len(self.players)):
            if self.winner_player.role < self.players[i].role:
                self.winner_player = self.players[i]
            elif self.winner_player.role == self.players[i].role:
                self.winner_player = self.check_number(self.winner_player, self.players[i])
        return self.winner_player
