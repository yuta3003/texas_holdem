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

    def show_hand(self):
        for i in range(len(self.__hand)):
            self.__hand[i].show()

    def role(self):
        return self.__role

    def judge_pair(self, hand):
        number_of_pair_list = [k for k, v in self.number_collection.items() if v == 2]
        number_of_pair_list.sort(reverse=True)
        try:
            number_of_pair_list[1]
            kicker_of_2pair_list = [k for k, v in self.number_collection.items() if v == 1]
            kicker_of_2pair_list.sort(reverse=True)
            self.__role = 2   # Two Pair
            for i in range(len(hand)):
                if hand[i].number(ace14=True) == number_of_pair_list[0]:
                    self.__hand.append(hand[i])
                elif hand[i].number(ace14=True) == number_of_pair_list[1]:
                    self.__hand.append(hand[i])
                elif hand[i].number(ace14=True) == kicker_of_2pair_list[0]:
                    self.__hand.append(hand[i])
        except IndexError:
            kicker_of_1pair_list = [k for k, v in self.number_collection.items() if v == 1]
            kicker_of_1pair_list.sort(reverse=True)
            self.__role = 1   # A Pair
            for i in range(len(hand)):
                if hand[i].number(ace14=True) == number_of_pair_list[0]:
                    self.__hand.append(hand[i])
                elif hand[i].number(ace14=True) in kicker_of_1pair_list:
                    self.__hand.append(hand[i])

    def judge_three_of_kind(self, unique_number: List[int], hand):
        number_of_3card_list = [k for k, v in self.number_collection.items() if v == 3]
        number_of_3card_list.sort(reverse=True)
        number_of_3card = number_of_3card_list[0]
        del self.number_collection[number_of_3card]
        try:    # Full House
            number_of_fullhouse_list = [k for k, v in self.number_collection.items() if v >= 2]
            kicker_of_fullhouse = self.judge_full_house(number_of_fullhouse_list)
            for i in range(len(hand)):
                if hand[i].number(ace14=True) == number_of_3card:
                    self.__hand.append(hand[i])

            for i in range(len(hand)):
                if len(self.__hand) == 5:
                    break
                if hand[i].number(ace14=True) == kicker_of_fullhouse:
                    self.__hand.append(hand[i])

        except IndexError:
            unique_number.remove(number_of_3card)
            unique_number.sort(reverse=True)
            kicker_of_3card_list = []
            kicker_of_3card_list = unique_number[:2]
            self.__role = 3   # Three of a Kind
            for i in range(len(hand)):
                if hand[i].number(ace14=True) == number_of_3card:
                    self.__hand.append(hand[i])
                elif hand[i].number(ace14=True) in kicker_of_3card_list:
                    self.__hand.append(hand[i])

    def judge_straight(self, hand):
        """
        ace14=True
        """
        consecutive_num = 0
        straight_num_list = []
        hand.sort(key=lambda x: x.number(ace14=True), reverse=True)

        for i in range(len(hand)-1):
            if hand[i].number(ace14=True) - hand[i+1].number(ace14=True) == 0:
                continue
            elif hand[i].number(ace14=True) - hand[i+1].number(ace14=True) == 1:
                straight_num_list.append(hand[i].number(ace14=True))
                consecutive_num += 1
                if consecutive_num >= 4:
                    straight_num_list.append(hand[i+1].number(ace14=True))
                    break
            else:
                if consecutive_num >= 4:
                    break
                straight_num_list = []
                consecutive_num = 0

        if consecutive_num >= 4:
            self.is_straight = True
            self.__role = 4   # Straight
            for i in range(len(hand)):
                if hand[i].number(ace14=True) in straight_num_list:
                    self.__hand.append(hand[i])
            self.show_hand()
            return

        """
        ace14=False
        """
        consecutive_num = 0
        straight_num_list = []
        hand.sort(key=lambda x: x.number(ace14=False), reverse=True)

        for i in range(len(hand)-1):
            if hand[i].number(ace14=False) - hand[i+1].number(ace14=False) == 0:
                continue
            elif hand[i].number(ace14=False) - hand[i+1].number(ace14=False) == 1:
                straight_num_list.append(hand[i].number(ace14=False))
                consecutive_num += 1
                if consecutive_num >= 4:
                    straight_num_list.append(hand[i+1].number(ace14=False))
                    break
            else:
                if consecutive_num >= 4:
                    break
                straight_num_list = []
                consecutive_num = 0

        if consecutive_num >= 4:
            self.is_straight = True
            self.__role = 4   # Straight
            for i in range(len(hand)):
                if hand[i].number(ace14=False) in straight_num_list:
                    self.__hand.append(hand[i])
            self.show_hand()
            return

    def judge_flush(self, hand: List[int]):
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
        self.__role = 6   # Full House
        return number_of_fullhouse_list[0]

    def judge_four_of_kind(self, unique_number: List[int], hand):
        number_of_4card = [k for k, v in self.number_collection.items() if v == 4][0]
        unique_number.remove(number_of_4card)
        kicker_of_4card = max(unique_number)
        self.__role = 7   # Four of a Kind
        for i in range(len(hand)):
            if hand[i].number(ace14=True) == number_of_4card:
                self.__hand.append(hand[i])
            elif hand[i].number(ace14=True) == kicker_of_4card:
                self.__hand.append(hand[i])

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
            self.judge_pair(hand)
        elif number_of_same_number == 3:    # three of kind or fullhouse
            self.judge_three_of_kind(unique_number, hand)
        elif number_of_same_number == 4:    # four of kind
            self.judge_four_of_kind(unique_number, hand)

        self.judge_flush(hand)
        self.judge_straight(hand)

        # if self.is_flush & self.is_straight:
        #     self.judge_straight_flush(descending_unique_number)


def main():
    import card

    # a_pair_card = []
    # a_pair_card.append(card.Card('D', 7))
    # a_pair_card.append(card.Card('C', 1))
    # a_pair_card.append(card.Card('C', 3))
    # a_pair_card.append(card.Card('H', 13))
    # a_pair_card.append(card.Card('S', 12))
    # a_pair_card.append(card.Card('S', 3))
    # a_pair_card.append(card.Card('H', 3))

    # a_pair = RoleJudge()
    # a_pair.judge(a_pair_card)
    # a_pair_role = a_pair.role()
    # a_pair_hand = a_pair.hand()

    # print(a_pair_role)
    # print(a_pair_hand)

    """
    ----------------------------------
     flush
    ----------------------------------
    """
    # flush = []
    # flush.append(card.Card('C', 8))
    # flush.append(card.Card('C', 1))
    # flush.append(card.Card('C', 13))
    # flush.append(card.Card('C', 2))
    # flush.append(card.Card('C', 5))
    # flush.append(card.Card('C', 9))
    # flush.append(card.Card('C', 7))

    # flush_card = RoleJudge()
    # flush_card.judge(flush)
    # flush_role = flush_card.role()

    """
    ----------------------------------
     fullhouse
    ----------------------------------
    """
    # fullhouse = []
    # fullhouse.append(card.Card('C', 1))
    # fullhouse.append(card.Card('S', 1))
    # fullhouse.append(card.Card('D', 1))
    # fullhouse.append(card.Card('H', 7))
    # fullhouse.append(card.Card('D', 7))
    # fullhouse.append(card.Card('C', 7))
    # fullhouse.append(card.Card('C', 13))

    # fullhouse_card = RoleJudge()
    # fullhouse_card.judge(fullhouse)
    # fullhouse_role = fullhouse_card.role()

    """
    ----------------------------------
     three of kind
    ----------------------------------
    """
    # three_of_card = []
    # three_of_card.append(card.Card('C', 1))
    # three_of_card.append(card.Card('D', 2))
    # three_of_card.append(card.Card('H', 2))
    # three_of_card.append(card.Card('S', 2))
    # three_of_card.append(card.Card('D', 3))
    # three_of_card.append(card.Card('C', 4))
    # three_of_card.append(card.Card('H', 12))

    # three_card = RoleJudge()
    # three_card.judge(three_of_card)
    # three_card_role = three_card.role()

    """
    ----------------------------------
     straight 1 2 3 4 5
    ----------------------------------
    """
    straight12345 = []
    straight12345.append(card.Card('C', 1))
    straight12345.append(card.Card('S', 2))
    straight12345.append(card.Card('D', 3))
    straight12345.append(card.Card('H', 4))
    straight12345.append(card.Card('D', 5))
    straight12345.append(card.Card('H', 9))
    straight12345.append(card.Card('C', 13))

    print("-----------1234---------------")
    straight12345_card = RoleJudge()
    straight12345_card.judge(straight12345)
    straight12345_role = straight12345_card.role()

    """
    ----------------------------------
     straight 5 6 7 8 9
    ----------------------------------
    """
    straight = []
    straight.append(card.Card('C', 1))
    straight.append(card.Card('S', 5))
    straight.append(card.Card('D', 6))
    straight.append(card.Card('H', 7))
    straight.append(card.Card('D', 8))
    straight.append(card.Card('H', 9))
    straight.append(card.Card('C', 13))

    print("----------56789----------------")
    straight_card = RoleJudge()
    straight_card.judge(straight)
    straight_role = straight_card.role()

    """
    ----------------------------------
     straight
    ----------------------------------
    """
    straight10JQKA = []
    straight10JQKA.append(card.Card('C', 1))
    straight10JQKA.append(card.Card('S', 5))
    straight10JQKA.append(card.Card('D', 6))
    straight10JQKA.append(card.Card('H', 10))
    straight10JQKA.append(card.Card('D', 11))
    straight10JQKA.append(card.Card('H', 12))
    straight10JQKA.append(card.Card('C', 13))

    print("-----------10JQKA---------------")
    straight10JQKA_card = RoleJudge()
    straight10JQKA_card.judge(straight10JQKA)
    straight10JQKA_role = straight10JQKA_card.role()

    """
    ----------------------------------
     four of kind
    ----------------------------------
    """
    # four_of_card = []
    # four_of_card.append(card.Card('C', 1))
    # four_of_card.append(card.Card('D', 2))
    # four_of_card.append(card.Card('H', 2))
    # four_of_card.append(card.Card('S', 2))
    # four_of_card.append(card.Card('C', 2))
    # four_of_card.append(card.Card('C', 4))
    # four_of_card.append(card.Card('H', 12))

    # four_card = RoleJudge()
    # four_card.judge(four_of_card)
    # four_card_role = four_card.role()

if __name__ == '__main__':
    main()
