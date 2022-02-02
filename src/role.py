import collections
from typing import (
    List,
)

from src import (
    card,
)


class RoleJudge:
    """役を判定


    """
    def __init__(self):
        self.__hand = []
        self.number_collection = collections.Counter()
        self.suit_collection = collections.Counter()
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

    def hand(self):
        return self.__hand

    def role(self):
        return self.__role

    def judge_pair(self):
        number_of_pair_list = [k for k, v in self.number_collection.items() if v == 2]
        number_of_pair_list.sort(reverse=True)
        try:
            number_of_2pair2 = number_of_pair_list[1]
            number_of_2pair1 = number_of_pair_list[0]
            kicker_of_2pair_list = [k for k, v in self.number_collection.items() if v == 1]
            kicker_of_2pair_list.sort(reverse=True)
            kicker_of_2pair = []
            kicker_of_2pair.append(kicker_of_2pair_list[0])
            self.__role = 2   # Two Pair
        except IndexError:
            number_of_1pair = number_of_pair_list[0]
            kicker_of_1pair_list = [k for k, v in self.number_collection.items() if v == 1]
            kicker_of_1pair_list.sort(reverse=True)
            self.__role = 1   # A Pair

    def judge_three_of_kind(self, unique_number: List[int]):
        number_of_3card_list = [k for k, v in self.number_collection.items() if v == 3]
        number_of_3card_list.sort(reverse=True)
        number_of_3card = number_of_3card_list[0]
        del self.number_collection[number_of_3card]
        try:    # Full House
            number_of_fullhouse_list = [k for k, v in self.number_collection.items() if v >= 2]
            kicker_of_fullhouse = []
            kicker_of_fullhouse.append(self.judge_full_house(number_of_fullhouse_list))
        except IndexError:
            unique_number.remove(number_of_3card)
            kicker_of_3card_1 = max(unique_number)
            unique_number.remove(kicker_of_3card_1)
            kicker_of_3card_2 = max(unique_number)

            self.__role = 3   # Three of a Kind

    def judge_straight(self, unique_number: List[int]):
        consecutive_num = 0
        for i in range(len(unique_number)-1):
            if unique_number[i] - unique_number[i+1] == 1:
                if consecutive_num >= 4:
                    break
                consecutive_num += 1
            else:
                if consecutive_num >= 4:
                    break
                consecutive_num = 0

        if consecutive_num >= 4:
            self.is_straight = True
            self.__role = 4   # Straight

        comparison_list = [14, 2, 3, 4, 5]
        number_of_common_items = len(list(set(unique_number) & set(comparison_list)))

        if number_of_common_items >= 5:
            self.is_straight = True
            self.__role = 4   # Straight

    def judge_flush(self, number: List[int], hand: List[int]):
        number_of_max_suit = max(self.suit_collection.values())
        flush_mark = [k for k, v in self.suit_collection.items() if v == number_of_max_suit][0]
        if number_of_max_suit >= 5:
            self.is_flush = True
            self.__role = 5   # Flush

            for i in range(len(hand)):
                if len(self.__hand) == 5:
                    break
                if hand[i].suit() == flush_mark:
                    self.__hand.append(hand[i])

    def judge_full_house(self, number_of_fullhouse_list) -> int:
        number_of_fullhouse_list.sort(reverse=True)
        number_of_fullhouse = number_of_fullhouse_list[0]
        self.__role = 6   # Full House
        return number_of_fullhouse

    def judge_four_of_kind(self, unique_number: List[int]):
        number_of_4card = [k for k, v in self.number_collection.items() if v == 4][0]
        unique_number.remove(number_of_4card)
        kicker_of_4card = max(unique_number)
        self.__role = 7   # Four of a Kind

    def judge_straight_flush(self, unique_number: List[int]):
        self.__role = 8

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
        """役を判定する関数

        役の強さとハンドを返す
        hand: List[card.Card()]
        """
        suit = []
        number = []
        hand.sort(key=lambda x: x.number(), reverse=True)

        for i in range(len(hand)):
            suit.append(hand[i].suit())

        for i in range(len(hand)):
            number.append(hand[i].number(ace14=True))

        unique_number = sorted(list(set(number)))
        descending_unique_number = unique_number[::-1]

        self.number_collection = collections.Counter(number)
        number_of_same_number = self.how_many_same_numbers(self.number_collection)

        self.suit_collection = collections.Counter(suit)

        if number_of_same_number == 2:  # Pair
            self.judge_pair()
        elif number_of_same_number == 3:    # three of kind or fullhouse
            self.judge_three_of_kind(unique_number)
        elif number_of_same_number == 4:    # four of kind
            self.judge_four_of_kind(unique_number)

        self.judge_flush(number, hand)
        self.judge_straight(descending_unique_number)

        # if self.is_flush & self.is_straight:
        #     self.judge_straight_flush(descending_unique_number)


def main():
    import card

    a_pair_card = []
    a_pair_card.append(card.Card('D', 8))
    a_pair_card.append(card.Card('C', 1))
    a_pair_card.append(card.Card('C', 3))
    a_pair_card.append(card.Card('H', 7))
    a_pair_card.append(card.Card('S', 12))
    a_pair_card.append(card.Card('S', 6))
    a_pair_card.append(card.Card('H', 3))

    a_pair = RoleJudge()
    a_pair.judge(a_pair_card)
    a_pair_role = a_pair.role()
    a_pair_hand = a_pair.hand()

    # print(a_pair_role)
    # print(a_pair_hand)

    """
    ----------------------------------
     flush
    ----------------------------------
    """
    flush = []
    flush.append(card.Card('C', 8))
    flush.append(card.Card('C', 1))
    flush.append(card.Card('C', 13))
    flush.append(card.Card('C', 2))
    flush.append(card.Card('C', 5))
    flush.append(card.Card('C', 9))
    flush.append(card.Card('C', 7))

    flush_card = RoleJudge()
    flush_card.judge(flush)
    flush_role = flush_card.role()


if __name__ == '__main__':
    main()
