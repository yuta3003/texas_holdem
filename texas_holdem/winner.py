"""
Todo:
    - None
"""
class Winner:
    """class説明のタイトル
    classの説明文を記入

    Attributes:
        players (list)  : Playerオブジェクトを持つリスト
        players_role_list (list)    : 役の強さを保持します
    """
    def __init__(self, players):
        self.players = players
        self.players_role_list = []

    def check_rank(self, same_role_index_list):
        winner_index = 0
        for i in range(len(same_role_index_list)-1):
            for j in range(5):
                if self.players[same_role_index_list[i]].hand[j].number(ace14=True) < self.players[same_role_index_list[i+1]].hand[j].number(ace14=True):
                    winner_index = same_role_index_list[i+1]
                    break
                elif self.players[same_role_index_list[i]].hand[j].number(ace14=True) > self.players[same_role_index_list[i+1]].hand[j].number(ace14=True):
                    winner_index = same_role_index_list[i]
                    break
                else:
                    winner_index = -1
        return winner_index

    def judge(self):
        for i in range(len(self.players)):
            self.players_role_list.append(self.players[i].role)

        winner_index = -1
        max_role_index = self.players_role_list.index(max(self.players_role_list))
        number_of_max_index = self.players_role_list.count(self.players[max_role_index].role)
        if number_of_max_index == 1:
            """
            役だけで勝敗がつくパターン
            """
            winner_index = max_role_index
        else:
            """
            役の数字を見ないと勝敗がつかないパターン
            """
            same_role_index_list = []
            for i in range(len(self.players)):
                if self.players[i].role == self.players[max_role_index].role:
                    same_role_index_list.append(i)
            winner_index = self.check_rank(same_role_index_list)
        return winner_index
