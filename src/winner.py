from src import (
    player,
)


class Winner:
    def __init__(self, players):
        self.players = players
        self.winner_player = player.Player()

    def judge(self):
        for i in range(len(self.players)):
            if self.winner_player.role < self.players[i].role:
                self.winner_player = self.players[i]
            elif self.winner_player.role == self.players[i].role:
                # 役が同じだった場合numberの強さとキッカーの強さを見る
                self.winner_player.name = 'Draw'
                pass
        return self.winner_player
