import collections


# フィールドカード5枚と手札2枚の7枚から一番強い役になるように5枚を選択する
class JudgeHand:
    # flush
    def judge_flush(mark, number):
        mark_collection = collections.Counter(mark)
        max_mark_num = max(mark_collection.values())
        print(max_mark_num)
        if max_mark_num >= 5:
        # flush フラグを立てる
        # flush 同士の勝敗のために数字を取得する
            pass

    # straight
    def judge_straight(unique_number):
        pass

    # straight flush
    def judge_straight_flush():
        pass

    # four of a kind
    def judge_four_of_kind():
        pass

    # three of a kind
    def judge_three_of_kind():
        pass

    # full house
    def judge_full_house():
        pass

    # a pair
    # two pair
    def judge_pair():
        pass

    # royal flush
    def judge_royal_flush():
        pass

    # high card
    def judge_high():
        pass

    mark = [i[0] for i in hand]
    number = [j[1:] for j in hand]  # => ['1', '11', '10', '12', '13', '11', '5']
    unique_number = sorted(list(set(number)))   # => ['1', '10', '11', '12', '13', '5']
    print(number)
    print(unique_number)
    judge_flush(mark, number)


def main():
    player_card = ['C1', 'H11']
    field_card = ['H10', 'D12', 'D13', 'D11', 'C5']
    hand = player_card + field_card

    judge_hand(hand)

"""
param: ['C6', 'H11', 'H10', 'D12', 'D13', 'D11', 'C5']
"""

if __name__ == '__main__':
    main()
