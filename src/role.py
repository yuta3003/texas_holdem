import collections
from typing import (
    List,
    Tuple,
)


class RoleJudge:
    """役を判定


    """
    def __init__(self):
        self.hand = []
        self.number_collection = collections.Counter()
        self.is_flush = False
        self.is_straight = False
        self.__role = 0
        """
        0: High Card
        1: A Pair
        2: Two Pair
        3: Three of a Kind
        4: Straight
        5: Flush
        6: Full House
        7: Four of a Kind
        8: Straight Flush
        9: Royal Flush
        """

    def role(self):
        return self.__role

    # a pair
    # two pair
    def judge_pair(self) -> Tuple[int, List[int]]:
        number_of_pair_list = [k for k, v in self.number_collection.items() if v == 2]
        number_of_pair_list.sort(reverse=True)
        try:    # 2ペア
            number_of_2pair = number_of_pair_list[1]
            kicker_of_2pair_list = [k for k, v in self.number_collection.items() if v == 1]
            kicker_of_2pair_list.sort(reverse=True)
            kicker_of_2pair = []
            kicker_of_2pair.append(kicker_of_2pair_list[0])
            self.__role = 2   # Two Pair
            return number_of_2pair, kicker_of_2pair
        except IndexError:  # 1ペア
            number_of_1pair = number_of_pair_list[0]
            kicker_of_1pair_list = [k for k, v in self.number_collection.items() if v == 1]
            kicker_of_1pair_list.sort(reverse=True)
            kicker_of_1pair = []
            kicker_of_1pair.append(kicker_of_1pair_list[0])
            kicker_of_1pair.append(kicker_of_1pair_list[1])
            kicker_of_1pair.append(kicker_of_1pair_list[2])
            self.__role = 1   # A Pair
            return number_of_1pair, kicker_of_1pair

    # three of a kind
    def judge_three_of_kind(self, unique_number: List[int]) -> Tuple[int, List[int]]:
        number_of_3card_list = [k for k, v in self.number_collection.items() if v == 3]
        number_of_3card_list.sort(reverse=True)
        number_of_3card = number_of_3card_list[0]
        del self.number_collection[number_of_3card]
        try:    # Full House
            number_of_fullhouse_list = [k for k, v in self.number_collection.items() if v >= 2]
            kicker_of_fullhouse = []
            kicker_of_fullhouse.append(self.judge_full_house(number_of_fullhouse_list))
            return number_of_3card, kicker_of_fullhouse

        except IndexError:
            kicker_of_3card = []
            unique_number.remove(number_of_3card)
            kicker_of_3card_1 = max(unique_number)
            unique_number.remove(kicker_of_3card_1)
            kicker_of_3card_2 = max(unique_number)

            kicker_of_3card.append(kicker_of_3card_1)
            kicker_of_3card.append(kicker_of_3card_2)
            self.__role = 3   # Three of a Kind
            return number_of_3card, kicker_of_3card

    # straight
    def judge_straight(self, unique_number: List[int]) -> int:
        """
        ストレートかどうかを判断する
        parameters
        ----------

        return
        ------
        ストレートの最大値を返す
        """
        consecutive_num = 0
        max_number = 0
        for i in range(len(unique_number)-1):
            if unique_number[i] - unique_number[i+1] == 1:
                consecutive_num += 1
                max_number = unique_number[i+1]
            else:
                if consecutive_num >= 4:
                    break
                max_number = 0
                consecutive_num = 0

        if consecutive_num >= 4:
            self.is_straight = True
            self.__role = 4   # Straight
            return max_number

        comparison_list = [14, 2, 3, 4, 5]
        number_of_common_items = len(list(set(unique_number) & set(comparison_list)))
        if number_of_common_items >= 5:
            self.is_straight = True
            self.__role = 4   # Straight
            max_number = 14
            return max_number

        return max_number

    # flush
    def judge_flush(self, suit: List[int], number: List[int]) -> None:
        suit_collection = collections.Counter(suit)
        number_of_max_suit = max(suit_collection.values())
        if number_of_max_suit >= 5:
            # TODO: flush 同士の勝敗のために数字を取得する
            self.is_flush = True
            self.__role = 5   # Flush

    # full house
    def judge_full_house(self, number_of_fullhouse_list) -> int:
        number_of_fullhouse_list.sort(reverse=True)
        number_of_fullhouse = number_of_fullhouse_list[0]
        self.__role = 6   # Full House
        return number_of_fullhouse

    # four of a kind
    def judge_four_of_kind(self, unique_number: List[int]):
        number_of_4card = [k for k, v in self.number_collection.items() if v == 4][0]
        unique_number.remove(number_of_4card)
        kicker_of_4card = max(unique_number)
        self.__role = 7   # Four of a Kind
        return number_of_4card, kicker_of_4card

    # straight flush
    def judge_straight_flush(self):
        self.__role = 8

    # royal flush
    def judge_royal_flush(self):
        self.__role = 9

    def how_many_same_numbers(self, number_collection) -> int:
        """
        同じカードが何枚あるのかを判断
        複数ペアある場合、最大値を返す
        """
        number_of_same_number = max(number_collection.values())
        return number_of_same_number

    def judge(self, hand):
        suit = []
        number = []

        # TODO: 内包表記に変更する
        for i in range(len(hand)):
            suit.append(hand[i].suit())

        for i in range(len(hand)):
            number.append(hand[i].number(ace14=True))

        unique_number = sorted(list(set(number)))
        descending_unique_number = unique_number[::-1]

        self.judge_flush(suit, number)
        self.judge_straight(descending_unique_number)

        self.number_collection = collections.Counter(number)
        number_of_same_number = self.how_many_same_numbers(self.number_collection)

        if number_of_same_number == 2:  # Pair
            self.judge_pair()
        elif number_of_same_number == 3:    # three of kind or fullhouse
            self.judge_three_of_kind(unique_number)
        elif number_of_same_number == 4:    # four of kind
            self.judge_four_of_kind(unique_number)

        if self.is_flush & self.is_straight:
            self.judge_straight_flush()


def main():
    pass


if __name__ == '__main__':
    main()
