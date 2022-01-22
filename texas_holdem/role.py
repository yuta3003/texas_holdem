import collections
from typing import List


# 役を判定するClass
class RoleJudge:
    def __init__(self, hand):
        self.hand = hand
        self.is_flush = False
        self.is_straight = False
        self.role = "High Card"

    # flush
    def judge_flush(self, mark: List[int], number: List[int]) -> None:
        mark_collection = collections.Counter(mark)
        max_mark_num = max(mark_collection.values())
        if max_mark_num >= 5:
        # TODO: flush 同士の勝敗のために数字を取得する
            self.is_flush = True

    # straight
    def judge_straight(self, unique_number: List[int]) -> None:
        consecutive_num = 0
        for i in range(len(unique_number)-1):
            if unique_number[i+1] - unique_number[i] == 1:
                consecutive_num += 1
            else:
                consecutive_num = 0
        if consecutive_num >= 4:
            self.is_straight = True

    # straight flush
    def judge_straight_flush(self):
        pass

    # four of a kind
    def judge_four_of_kind(self):
        pass

    # three of a kind
    def judge_three_of_kind(self):
        pass

    # full house
    def judge_full_house(self):
        pass

    # a pair
    # two pair
    def judge_pair(self):
        pass

    # royal flush
    def judge_royal_flush(self):
        pass

    # high card
    def judge_high(self):
        pass

    def how_many_same_numbers(self, number):
        pass

    def role_judge(self):
        mark = [i[0] for i in self.hand]
        number = [int(j[1:]) for j in self.hand]  # => [1, 11, 10, 12, 13, 11, 5]
        unique_number = sorted(list(set(number)))   # => [1, 5, 10, 11, 12, 13]
        self.judge_flush(mark, number)
        self.judge_straight(unique_number)
        print("is_flush:", self.is_flush)
        print("is_straight:", self.is_straight)
        number_of_pairs = self.how_many_same_numbers(number)



# haw many same numbers

# Python 3.9.5 (default, May 30 2021, 02:01:36)
# [Clang 12.0.5 (clang-1205.0.22.9)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> number = [1, 11, 10, 12, 13, 11, 5]
# >>> number
# [1, 11, 10, 12, 13, 11, 5]
# >>> import collections
# >>> num_col = collections.Counter(number)
# >>> num_col
# Counter({11: 2, 1: 1, 10: 1, 12: 1, 13: 1, 5: 1})
# >>> num_col_max = max(num_col.values())
# >>> num_col_max
# 2
# >>> num_col_max_2 = max(num_col)
# >>> num_col_max_2
# 13
# >>> exit()



def main():
    field_card = ['C10', 'C12', 'C13', 'D9', 'C5']
    player1_card = ['C1', 'C11']
    player2_card = ['D1', 'D10']
    player1_hand = player1_card + field_card
    player2_hand = player2_card + field_card

    print("player1")
    player1 = RoleJudge(player1_hand)
    player1.role_judge()

    print("player2")
    player2 = RoleJudge(player2_hand)
    player2.role_judge()


if __name__ == '__main__':
    main()
