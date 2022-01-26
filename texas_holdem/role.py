import collections
from typing import List


class RoleJudge:
    """
    役を判定

    """
    def __init__(self):
        self.hand = []
        self.is_flush = False
        self.is_straight = False
        self.role = "High Card"

    # flush
    def judge_flush(self, suit: List[int], number: List[int]) -> None:
        suit_collection = collections.Counter(suit)
        number_of_max_suit = max(suit_collection.values())
        if number_of_max_suit >= 5:
        # TODO: flush 同士の勝敗のために数字を取得する
            self.is_flush = True

    # straight
    # TODO: 10, 11, 12, 13, 1の時もストレートと判定するように
    def judge_straight(self, unique_number: List[int]) -> None:
        consecutive_num = 0
        for i in range(len(unique_number)-1):
            if unique_number[i] - unique_number[i+1] == 1:
                consecutive_num += 1
            else:
                if consecutive_num >= 4:
                    break
                consecutive_num = 0

        if consecutive_num >= 4:
            self.role = "Straight"
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

    def how_many_same_numbers(self, number_collection):
        number_of_same_number = max(number_collection.values())
        return number_of_same_number

    def judge(self, hand):
        suit = []
        number = []

        # TODO: 内包表記に変更する
        for i in range(len(hand)):
            # TODO: カードのインスタンス変数にアクセスできないようにする
            suit.append(hand[i].suit)

        for i in range(len(hand)):
            number.append(hand[i].number(ace14=True))
        unique_number = sorted(list(set(number)))
        # descending_unique_number = reversed(unique_number)
        descending_unique_number = unique_number[::-1]

        self.judge_flush(suit, number)
        self.judge_straight(descending_unique_number)

        number_collection = collections.Counter(number)
        number_of_same_number = self.how_many_same_numbers(number_collection)

        # pairs
        if number_of_same_number == 2:
            # TODO: 3ペアだった場合の2ペアの選択方法に問題あり
            self.role = "a pair"
            number_of_1pair = [k for k, v in number_collection.items() if v == 2][0]
            try:
                number_of_2pair = [k for k, v in number_collection.items() if v == 2][1]
                self.role = "two pairs"
                # TODO: 2ペアのキッカー1枚を取得
            except IndexError:
                # TODO: 1ペアのキッカー3枚を取得
                pass
        # three of kind or fullhouse
        elif number_of_same_number == 3:
            self.role = "three of kind"
            number_of_3card = [k for k, v in number_collection.items() if v == 3][0]

            try:
                # TODO: 3カードが2組あった場合の3カードの選択方法に問題あり
                number_of_fullhouse = [k for k, v in number_collection.items() if v >= 2][0]
                self.role = "fullhouse"
            except IndexError:
                # TODO: キッカーの選択方法に問題あり
                unique_number.remove(number_of_3card)
                kicker_of_3card_1 = max(unique_number)
                unique_number.remove(kicker_of_3card_1)
                kicker_of_3card_2 = max(unique_number)
                print("3カードのキッカー: ", kicker_of_3card_1, kicker_of_3card_2)
        # four of kind
        elif number_of_same_number == 4:
            self.role = "four of kind"
            number_of_4card = [k for k, v in number_collection.items() if v == 4][0]
            unique_number.remove(number_of_4card)
            kicker_of_4card = max(unique_number)

        # print("is_flush:", self.is_flush)
        # print("is_straight:", self.is_straight)
        # print("number_of_same_number:", number_of_same_number)
        print(self.role)


def main():
    import card

    #----------------------------------
    # A Pair
    #----------------------------------
    a_pair_card = []
    a_pair_card.append(card.Card('C', 1))
    a_pair_card.append(card.Card('C', 3))
    a_pair_card.append(card.Card('H', 3))
    a_pair_card.append(card.Card('S', 6))
    a_pair_card.append(card.Card('H', 7))
    a_pair_card.append(card.Card('D', 8))
    a_pair_card.append(card.Card('S', 12))

    print("-------------------------")
    print("a_pair_card")
    print("-------------------------")
    a_pair = RoleJudge()
    a_pair.judge(a_pair_card)
    print("")

    #----------------------------------
    # Two Pairs
    #----------------------------------
    two_pair_card = []
    two_pair_card.append(card.Card('C', 1))
    two_pair_card.append(card.Card('D', 1))
    two_pair_card.append(card.Card('H', 3))
    two_pair_card.append(card.Card('S', 3))
    two_pair_card.append(card.Card('S', 6))
    two_pair_card.append(card.Card('S', 12))
    two_pair_card.append(card.Card('H', 12))

    print("-------------------------")
    print("two_pair_card")
    print("-------------------------")
    two_pair = RoleJudge()
    two_pair.judge(two_pair_card)
    print("")

    #----------------------------------
    # three of kind
    #----------------------------------
    three_of_card = []
    three_of_card.append(card.Card('C', 1))
    three_of_card.append(card.Card('D', 2))
    three_of_card.append(card.Card('H', 2))
    three_of_card.append(card.Card('S', 2))
    three_of_card.append(card.Card('D', 3))
    three_of_card.append(card.Card('C', 4))
    three_of_card.append(card.Card('H', 12))

    print("-------------------------")
    print("three_of_kind")
    print("-------------------------")
    three_card = RoleJudge()
    three_card.judge(three_of_card)
    print("")

    #----------------------------------
    # four of kind
    #----------------------------------
    four_of_card = []
    four_of_card.append(card.Card('C', 1))
    four_of_card.append(card.Card('D', 2))
    four_of_card.append(card.Card('H', 2))
    four_of_card.append(card.Card('S', 2))
    four_of_card.append(card.Card('C', 2))
    four_of_card.append(card.Card('C', 4))
    four_of_card.append(card.Card('H', 12))

    print("-------------------------")
    print("four_of_kind")
    print("-------------------------")
    four_card = RoleJudge()
    four_card.judge(four_of_card)
    print("")

    #----------------------------------
    # flush
    #----------------------------------
    flush = []
    flush.append(card.Card('C', 1))
    flush.append(card.Card('C', 2))
    flush.append(card.Card('C', 5))
    flush.append(card.Card('C', 7))
    flush.append(card.Card('C', 8))
    flush.append(card.Card('C', 9))
    flush.append(card.Card('C', 13))

    print("-------------------------")
    print("flush")
    print("-------------------------")
    flush_card = RoleJudge()
    flush_card.judge(flush)
    print("")

    #----------------------------------
    # straight 1 2 3 4 5
    #----------------------------------
    straight12345 = []
    straight12345.append(card.Card('C', 1))
    straight12345.append(card.Card('S', 2))
    straight12345.append(card.Card('D', 3))
    straight12345.append(card.Card('H', 4))
    straight12345.append(card.Card('D', 5))
    straight12345.append(card.Card('H', 9))
    straight12345.append(card.Card('C', 13))

    print("-------------------------")
    print("straight12345")
    print("-------------------------")
    straight12345_card = RoleJudge()
    straight12345_card.judge(straight12345)
    print("")
    #----------------------------------
    # straight 5 6 7 8 9
    #----------------------------------
    straight = []
    straight.append(card.Card('C', 1))
    straight.append(card.Card('S', 5))
    straight.append(card.Card('D', 6))
    straight.append(card.Card('H', 7))
    straight.append(card.Card('D', 8))
    straight.append(card.Card('H', 9))
    straight.append(card.Card('C', 13))

    print("-------------------------")
    print("straight")
    print("-------------------------")
    straight_card = RoleJudge()
    straight_card.judge(straight)
    print("")
    #----------------------------------
    # straight 10 11 12 13 1
    #----------------------------------
    straight10JQKA = []
    straight10JQKA.append(card.Card('C', 1))
    straight10JQKA.append(card.Card('S', 5))
    straight10JQKA.append(card.Card('D', 6))
    straight10JQKA.append(card.Card('H', 10))
    straight10JQKA.append(card.Card('D', 11))
    straight10JQKA.append(card.Card('H', 12))
    straight10JQKA.append(card.Card('C', 13))

    print("-------------------------")
    print("straight10JQKA")
    print("-------------------------")
    straight10JQKA_card = RoleJudge()
    straight10JQKA_card.judge(straight10JQKA)
    print("")

    #----------------------------------
    # fullhouse
    #----------------------------------
    fullhouse = []
    fullhouse.append(card.Card('C', 1))
    fullhouse.append(card.Card('S', 1))
    fullhouse.append(card.Card('D', 1))
    fullhouse.append(card.Card('H', 7))
    fullhouse.append(card.Card('D', 7))
    fullhouse.append(card.Card('C', 7))
    fullhouse.append(card.Card('C', 13))

    print("-------------------------")
    print("fullhouse")
    print("-------------------------")
    fullhouse_card = RoleJudge()
    fullhouse_card.judge(fullhouse)
    print("")

    field_card = []
    field_card.append(card.Card('C', 2))
    field_card.append(card.Card('S', 2))
    field_card.append(card.Card('C', 1))
    field_card.append(card.Card('S', 1))
    field_card.append(card.Card('S', 3))

    player_card = []
    player_card.append(card.Card('H', 5))
    player_card.append(card.Card('S', 11))

    player_hand = player_card + field_card

    print("-------------------------")
    print("player")
    print("-------------------------")
    player = RoleJudge()
    player.judge(player_hand)


if __name__ == '__main__':
    main()
