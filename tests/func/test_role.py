import collections

import pytest

from src import (
    card,
    role,
)


def test_judge_pair():
    """
    ----------------------------------
     A Pair
    ----------------------------------
    """
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('C', 3))
    test_card.append(card.Card('H', 3))
    test_card.append(card.Card('S', 6))
    test_card.append(card.Card('H', 7))
    test_card.append(card.Card('D', 8))
    test_card.append(card.Card('S', 12))

    test_role_judge = role.RoleJudge()
    test_role_judge.judge(test_card)
    test_role = test_role_judge.role()
    assert test_role == 1


    """
    ----------------------------------
     Two Pairs
    ----------------------------------
    """
    two_pair_card = []
    two_pair_card.append(card.Card('C', 1))
    two_pair_card.append(card.Card('D', 1))
    two_pair_card.append(card.Card('H', 3))
    two_pair_card.append(card.Card('S', 3))
    two_pair_card.append(card.Card('S', 6))
    two_pair_card.append(card.Card('S', 12))
    two_pair_card.append(card.Card('H', 13))

    two_pair = role.RoleJudge()
    two_pair.judge(two_pair_card)
    two_pair_role = two_pair.role()

    assert two_pair_role == 2

    """
    ----------------------------------
     Three Pairs
    ----------------------------------
    """
    three_pair_card = []
    three_pair_card.append(card.Card('C', 1))
    three_pair_card.append(card.Card('D', 1))
    three_pair_card.append(card.Card('H', 3))
    three_pair_card.append(card.Card('S', 3))
    three_pair_card.append(card.Card('S', 6))
    three_pair_card.append(card.Card('S', 12))
    three_pair_card.append(card.Card('H', 12))

    three_pair = role.RoleJudge()
    three_pair.judge(three_pair_card)
    three_pair_role = three_pair.role()

    assert three_pair_role == 2


def test_judge_three_of_kind():
    """
    ----------------------------------
     three of kind
    ----------------------------------
    """
    three_of_card = []
    three_of_card.append(card.Card('C', 1))
    three_of_card.append(card.Card('D', 2))
    three_of_card.append(card.Card('H', 2))
    three_of_card.append(card.Card('S', 2))
    three_of_card.append(card.Card('D', 3))
    three_of_card.append(card.Card('C', 4))
    three_of_card.append(card.Card('H', 12))

    three_card = role.RoleJudge()
    three_card.judge(three_of_card)
    three_card_role = three_card.role()

    assert three_card_role == 3


def test_judge_straight():
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

    straight12345_card = role.RoleJudge()
    straight12345_card.judge(straight12345)
    straight12345_role = straight12345_card.role()

    assert straight12345_role == 4

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

    straight_card = role.RoleJudge()
    straight_card.judge(straight)
    straight_role = straight_card.role()

    assert straight_role == 4

    """
    ----------------------------------
     straight 10 11 12 13 1
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

    straight10JQKA_card = role.RoleJudge()
    straight10JQKA_card.judge(straight10JQKA)
    straight10JQKA_role = straight10JQKA_card.role()

    assert straight10JQKA_role == 4


def test_judge_flush():
    """
    ----------------------------------
     flush
    ----------------------------------
    """
    flush = []
    flush.append(card.Card('C', 1))
    flush.append(card.Card('C', 2))
    flush.append(card.Card('C', 5))
    flush.append(card.Card('C', 7))
    flush.append(card.Card('C', 8))
    flush.append(card.Card('C', 9))
    flush.append(card.Card('C', 13))

    flush_card = role.RoleJudge()
    flush_card.judge(flush)
    flush_role = flush_card.role()

    assert flush_role == 5


def test_judge_full_house():
    """
    ----------------------------------
     fullhouse
    ----------------------------------
    """
    fullhouse = []
    fullhouse.append(card.Card('C', 1))
    fullhouse.append(card.Card('S', 1))
    fullhouse.append(card.Card('D', 1))
    fullhouse.append(card.Card('H', 7))
    fullhouse.append(card.Card('D', 7))
    fullhouse.append(card.Card('C', 7))
    fullhouse.append(card.Card('C', 13))

    fullhouse_card = role.RoleJudge()
    fullhouse_card.judge(fullhouse)
    fullhouse_role = fullhouse_card.role()

    assert fullhouse_role == 6


def test_judge_four_of_kind():
    """
    ----------------------------------
     four of kind
    ----------------------------------
    """
    four_of_card = []
    four_of_card.append(card.Card('C', 1))
    four_of_card.append(card.Card('D', 2))
    four_of_card.append(card.Card('H', 2))
    four_of_card.append(card.Card('S', 2))
    four_of_card.append(card.Card('C', 2))
    four_of_card.append(card.Card('C', 4))
    four_of_card.append(card.Card('H', 12))

    four_card = role.RoleJudge()
    four_card.judge(four_of_card)
    four_card_role = four_card.role()

    assert four_card_role == 7


def test_judge_straight_flush():
    """
    ----------------------------------
     straight flush
    ----------------------------------
    """
    straightflush = []
    straightflush.append(card.Card('H', 1))
    straightflush.append(card.Card('C', 2))
    straightflush.append(card.Card('C', 6))
    straightflush.append(card.Card('C', 7))
    straightflush.append(card.Card('C', 8))
    straightflush.append(card.Card('C', 9))
    straightflush.append(card.Card('C', 10))

    straightflush_card = role.RoleJudge()
    straightflush_card.judge(straightflush)
    straightflush_role = straightflush_card.role()


    assert straightflush_role == 8

    """
    ----------------------------------
     royal flush
    ----------------------------------
    """
    rflush = []
    rflush.append(card.Card('C', 1))
    rflush.append(card.Card('C', 2))
    rflush.append(card.Card('C', 6))
    rflush.append(card.Card('C', 10))
    rflush.append(card.Card('C', 11))
    rflush.append(card.Card('C', 12))
    rflush.append(card.Card('C', 13))

    rflush_card = role.RoleJudge()
    rflush_card.judge(rflush)
    rflush_role = rflush_card.role()


    assert rflush_role == 9


def test_how_many_same_numbers():
    """
    ----------------------------------
     same number = 1
    ----------------------------------
    """
    same_number1 = role.RoleJudge()
    number = [1, 2, 3, 4, 5, 6, 7]
    number_collection = collections.Counter(number)
    same_number1.how_many_same_numbers(number_collection)

    """
    ----------------------------------
     same number = 2
    ----------------------------------
    """
    same_number2 = role.RoleJudge()
    number = [1, 2, 3, 4, 4, 5, 6]
    number_collection = collections.Counter(number)
    same_number2.how_many_same_numbers(number_collection)

    """
    ----------------------------------
     same number = 3
    ----------------------------------
    """
    same_number3 = role.RoleJudge()
    number = [1, 2, 3, 4, 4, 4, 5]
    number_collection = collections.Counter(number)
    same_number3.how_many_same_numbers(number_collection)

    """
    ----------------------------------
     same number = 4
    ----------------------------------
    """
    same_number4 = role.RoleJudge()
    number = [1, 2, 3, 4, 4, 4, 4]
    number_collection = collections.Counter(number)
    same_number4.how_many_same_numbers(number_collection)


def test_judge():
    pass
