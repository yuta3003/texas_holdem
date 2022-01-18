import collections

"""
param: ['C6', 'H11', 'H10', 'D12', 'D13', 'D11', 'C5']
"""
# フィールドカード5枚と手札2枚の7枚から一番強い役になるように5枚を選択する
class JudgeHand:
    def __init__(self):
        self.is_flush = False
        self.is_straight = False

    # flush
    def judge_flush(self, mark, number):
        mark_collection = collections.Counter(mark)
        max_mark_num = max(mark_collection.values())
        if max_mark_num >= 5:
        # flush 同士の勝敗のために数字を取得する
            self.is_flush = True

    # straight
    def judge_straight(self, unique_number):
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

    def judge_hand(self, hand):
        mark = [i[0] for i in hand]
        number = [int(j[1:]) for j in hand]  # => ['1', '11', '10', '12', '13', '11', '5']
        unique_number = sorted(list(set(number)))   # => ['1', '5', '10', '11', '12', '13']
        self.judge_flush(mark, number)
        self.judge_straight(unique_number)
        # print("is_flush:", self.is_flush)
        # print("is_straight:", self.is_straight)



def main():
    player_card = ['C1', 'C11']
    field_card = ['C10', 'C12', 'C13', 'D9', 'C5']
    hand = player_card + field_card

    player1 = JudgeHand()
    player1.judge_hand(hand)


if __name__ == '__main__':
    main()
