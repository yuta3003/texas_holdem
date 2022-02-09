import collections


class Role:
    """役を判定

    役を判定しself.__roleに値をセットする。
    その際の手札をself.__handにセットする。
    self.__roleに設定する値
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
    def __init__(self):
        self.__hand = []    # 役成立時のハンド
        self.__role = -1

    @property
    def hand(self):
        return self.__hand

    @hand.setter
    def hand(self, hand):
        self.__hand = hand

    @property
    def role(self):
        return self.__role

    """
    self.__roleを外部から設定することがないのでコメントアウト
    """
    # @role.setter
    # def role(self, role):
    #     self.__role = role

    def update_role(self, role, hand):
        if self.__role < role:
            self.__role = role
            self.__hand = hand

    def judge_high_card(self, hand):
        current_role = 0
        current_hand = hand[:5]
        self.update_role(current_role, current_hand)

    def judge_pair(self, hand):
        # create number_collections
        number = []
        for i in range(len(hand)):
            number.append(hand[i].number(ace14=True))
        number_collection = collections.Counter(number)

        number_of_pair_list = [k for k, v in number_collection.items() if v == 2]
        number_of_pair_list.sort(reverse=True)
        try:
            number_of_pair_list[1]
            kicker_of_2pair_list = [k for k, v in number_collection.items() if v == 1]
            kicker_of_2pair_list.sort(reverse=True)

            current_role = 2
            current_hand = []

            # 役を優先して手札の先頭に置く
            for i in range(len(hand)):
                if hand[i].number(ace14=True) == number_of_pair_list[0]:
                    current_hand.append(hand[i])
                elif hand[i].number(ace14=True) == number_of_pair_list[1]:
                    current_hand.append(hand[i])

            for i in range(len(hand)):
                if hand[i].number(ace14=True) == kicker_of_2pair_list[0]:
                    current_hand.append(hand[i])
            self.update_role(current_role, current_hand)

        except IndexError:
            kicker_of_1pair_list = [k for k, v in number_collection.items() if v == 1]
            kicker_of_1pair_list.sort(reverse=True)

            current_role = 1
            current_hand = []

            # 役を優先して手札の先頭に置く
            for i in range(len(hand)):
                if hand[i].number(ace14=True) == number_of_pair_list[0]:
                    current_hand.append(hand[i])

            for i in range(len(hand)):
                if hand[i].number(ace14=True) in kicker_of_1pair_list:
                    current_hand.append(hand[i])
            self.update_role(current_role, current_hand)

    def judge_three_of_kind(self, hand):
        # create number_collections
        number = []
        for i in range(len(hand)):
            number.append(hand[i].number(ace14=True))
        number_collection = collections.Counter(number)

        number_of_3card_list = [k for k, v in number_collection.items() if v == 3]
        number_of_3card_list.sort(reverse=True)
        number_of_3card = number_of_3card_list[0]
        del number_collection[number_of_3card]

        try:    # Full House
            number_of_fullhouse_list = [k for k, v in number_collection.items() if v >= 2]
            number_of_fullhouse_list.sort(reverse=True)
            kicker_of_fullhouse = number_of_fullhouse_list[0]

            current_role = 6
            current_hand = []

            for i in range(len(hand)):
                if hand[i].number(ace14=True) == number_of_3card:
                    current_hand.append(hand[i])

            for i in range(len(hand)):
                if len(current_hand) == 5:
                    break
                if hand[i].number(ace14=True) == kicker_of_fullhouse:
                    current_hand.append(hand[i])
            self.update_role(current_role, current_hand)

        except IndexError:
            # create unique_number
            number = []
            for i in range(len(hand)):
                number.append(hand[i].number(ace14=True))
            unique_number = list(set(number))

            unique_number.remove(number_of_3card)
            unique_number.sort(reverse=True)
            kicker_of_3card_list = []
            kicker_of_3card_list = unique_number[:2]

            current_role = 3
            current_hand = []
            for i in range(len(hand)):
                if hand[i].number(ace14=True) == number_of_3card:
                    current_hand.append(hand[i])

            for i in range(len(hand)):
                if hand[i].number(ace14=True) in kicker_of_3card_list:
                    current_hand.append(hand[i])
            self.update_role(current_role, current_hand)

    def judge_straight(self, hand):
        """
        ace14=True
        2~14までのストレートを判定
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
            current_role = 4
            current_hand = []
            for i in range(len(hand)):
                if hand[i].number(ace14=True) in straight_num_list:
                    current_hand.append(hand[i])
            self.update_role(current_role, current_hand)
            return

        """
        ace14=False
        1~5のストレートを判定
        """
        consecutive_num = 0
        straight_num_list = []
        hand.sort(key=lambda x: x.number(ace14=False), reverse=False)

        for i in range(len(hand)-1):
            if hand[i+1].number(ace14=False) - hand[i].number(ace14=False) == 0:
                continue
            elif hand[i+1].number(ace14=False) - hand[i].number(ace14=False) == 1:
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
            current_role = 4
            current_hand = []
            for i in range(len(hand)):
                if hand[i].number(ace14=False) in straight_num_list:
                    current_hand.append(hand[i])
            current_hand.sort(key=lambda x: x.number(ace14=True), reverse=True)
            self.update_role(current_role, current_hand)
            return

    def judge_flush(self, hand):
        # create suit_collections
        suit = []
        for i in range(len(hand)):
            suit.append(hand[i].suit)
        suit_collection = collections.Counter(suit)

        number_of_max_suit = max(suit_collection.values())
        flush_mark = [k for k, v in suit_collection.items() if v == number_of_max_suit][0]

        if number_of_max_suit >= 5:
            current_role = 5
            current_hand = []
            for i in range(len(hand)):
                if len(current_hand) == 5:
                    break
                if hand[i].suit == flush_mark:
                    current_hand.append(hand[i])
            current_hand.sort(key=lambda x: x.number(ace14=True), reverse=True)
            self.update_role(current_role, current_hand)

    def judge_four_of_kind(self, hand):
        # create number_collections
        number = []
        for i in range(len(hand)):
            number.append(hand[i].number(ace14=True))
        number_collection = collections.Counter(number)

        unique_number = list(set(number))
        number_of_4card = [k for k, v in number_collection.items() if v == 4][0]
        unique_number.remove(number_of_4card)
        kicker_of_4card = max(unique_number)

        current_role = 7
        current_hand = []

        for i in range(len(hand)):
            if hand[i].number(ace14=True) == number_of_4card:
                current_hand.append(hand[i])

        for i in range(len(hand)):
            if hand[i].number(ace14=True) == kicker_of_4card:
                current_hand.append(hand[i])
        self.update_role(current_role, current_hand)

    def judge_straight_flush(self, hand):
        # create suit_collections
        suit = []
        for i in range(len(hand)):
            suit.append(hand[i].suit)
        suit_collection = collections.Counter(suit)

        judge_hand = []
        number_of_max_suit = max(suit_collection.values())
        flush_mark = [k for k, v in suit_collection.items() if v == number_of_max_suit][0]
        if number_of_max_suit >= 5:
            """
            Straight Flush
            """
            for i in range(len(hand)):
                if hand[i].suit == flush_mark:
                    judge_hand.append(hand[i])

            consecutive_num = 0
            straight_num_list = []
            judge_hand.sort(key=lambda x: x.number(ace14=False), reverse=False)

            for i in range(len(judge_hand)-1):
                if judge_hand[i+1].number(ace14=False) - judge_hand[i].number(ace14=False) == 0:
                    continue

                elif judge_hand[i+1].number(ace14=False) - judge_hand[i].number(ace14=False) == 1:
                    straight_num_list.append(judge_hand[i].number(ace14=False))
                    consecutive_num += 1
                    if consecutive_num >= 4:
                        straight_num_list.append(judge_hand[i+1].number(ace14=False))
                        break
                else:
                    if consecutive_num >= 4:
                        break
                    straight_num_list = []
                    consecutive_num = 0

            if consecutive_num >= 4:
                current_role = 8
                current_hand = []
                for i in range(len(judge_hand)):
                    if judge_hand[i].number(ace14=False) in straight_num_list:
                        current_hand.append(judge_hand[i])
                self.update_role(current_role, current_hand)
                return

            """
            Royal Flush
            """
            consecutive_num = 0
            straight_num_list = []
            judge_hand.sort(key=lambda x: x.number(ace14=True), reverse=True)

            for i in range(len(judge_hand)-1):
                if judge_hand[i].number(ace14=True) - judge_hand[i+1].number(ace14=True) == 0:
                    continue

                elif judge_hand[i].number(ace14=True) - judge_hand[i+1].number(ace14=True) == 1:
                    straight_num_list.append(judge_hand[i].number(ace14=True))
                    consecutive_num += 1
                    if consecutive_num >= 4:
                        straight_num_list.append(judge_hand[i+1].number(ace14=True))
                        break
                else:
                    if consecutive_num >= 4:
                        break
                    straight_num_list = []
                    consecutive_num = 0

            if consecutive_num >= 4:
                current_role = 9
                current_hand = []
                for i in range(len(judge_hand)):
                    if judge_hand[i].number(ace14=True) in straight_num_list:
                        current_hand.append(judge_hand[i])
                self.update_role(current_role, current_hand)
                return

    def how_many_same_numbers(self, hand) -> int:
        """
        同じカードが何枚あるのかを判断
        複数ペアある場合、最大値を返す
        """
        # create number_collections
        number = []
        for i in range(len(hand)):
            number.append(hand[i].number(ace14=True))
        number_collection = collections.Counter(number)

        number_of_same_number = max(number_collection.values())
        return number_of_same_number

    def judge(self, hand):
        """役を判定する関数

        役の強さとハンドを返す
        hand: List[card.Card()]
        """
        hand.sort(key=lambda x: x.number(ace14=True), reverse=True)

        self.judge_high_card(hand)
        number_of_same_number = self.how_many_same_numbers(hand)
        if number_of_same_number == 2:  # Pair
            self.judge_pair(hand)
        elif number_of_same_number == 3:    # three of kind or fullhouse
            self.judge_three_of_kind(hand)
        elif number_of_same_number == 4:    # four of kind
            self.judge_four_of_kind(hand)

        self.judge_flush(hand)
        self.judge_straight(hand)
        self.judge_straight_flush(hand)


def main():
    pass


if __name__ == '__main__':
    main()
