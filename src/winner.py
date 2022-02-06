from src import (
    player,
)

class Winner:
    def __init__(self, players):
        self.players = players

    def winner(self):
        max_role_player = self.players[0]
        for i in range(len(self.players)):
            if max_role_player.role < self.players[i].role:
                max_role_player = self.players[i]
        return max_role_player
