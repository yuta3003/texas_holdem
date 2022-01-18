import collections


def main():
    player_card = ['C1', 'C11']
    field_card = ['C10', 'C12', 'C13', 'D9', 'C5']
    hand = player_card + field_card

    judge_hand(hand)

"""
param: ['C6', 'H11', 'H10', 'D12', 'D13', 'D11', 'C5']
"""
# フィールドカード5枚と手札2枚の7枚から一番強い役になるように5枚を選択する
def judge_hand(hand):
    is_flush = False
    is_straight = False

    # flush
    def judge_flush(mark, number):
        mark_collection = collections.Counter(mark)
        max_mark_num = max(mark_collection.values())
        print(max_mark_num)
        if max_mark_num >= 5:
        # flush 同士の勝敗のために数字を取得する
            is_flush = True

    # straight
    def judge_straight(unique_number):
        consecutive_num = 0
        for i in range(len(unique_number)-1):
            if unique_number[i+1] - unique_number[i] == 1:
                consecutive_num += 1
            else:
                consecutive_num = 0
        if consecutive_num >= 5:
            is_straight = True

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
    number = [int(k) for k in number]
    unique_number = sorted(list(set(number)), key=int)   # => ['1', '5', '10', '11', '12', '13']
    judge_flush(mark, number)
    judge_straight(unique_number)
    print("is_flush:", is_flush)
    print("is_straight:", is_straight)



if __name__ == '__main__':
    main()
