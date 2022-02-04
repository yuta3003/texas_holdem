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
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('D', 1))
    test_card.append(card.Card('H', 3))
    test_card.append(card.Card('S', 3))
    test_card.append(card.Card('S', 6))
    test_card.append(card.Card('S', 12))
    test_card.append(card.Card('H', 13))

    test_role_judge = role.RoleJudge()
    test_role_judge.judge(test_card)
    test_role = test_role_judge.role()
    assert test_role == 2

    """
    ----------------------------------
     Three Pairs
    ----------------------------------
    """
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('D', 1))
    test_card.append(card.Card('H', 3))
    test_card.append(card.Card('S', 3))
    test_card.append(card.Card('S', 6))
    test_card.append(card.Card('S', 12))
    test_card.append(card.Card('H', 12))

    test = role.RoleJudge()
    test.judge(test_card)
    test_role = test.role()

    assert test_role == 2


def test_judge_three_of_kind():
    """
    ----------------------------------
     three of kind
    ----------------------------------
    """
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('D', 2))
    test_card.append(card.Card('H', 2))
    test_card.append(card.Card('S', 2))
    test_card.append(card.Card('D', 3))
    test_card.append(card.Card('C', 4))
    test_card.append(card.Card('H', 12))

    test = role.RoleJudge()
    test.judge(test_card)
    test_role = test.role()

    assert test_role == 3


def test_judge_straight():
    """
    ----------------------------------
     straight 1 2 3 4 5
    ----------------------------------
    """
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('S', 2))
    test_card.append(card.Card('D', 3))
    test_card.append(card.Card('H', 4))
    test_card.append(card.Card('D', 5))
    test_card.append(card.Card('H', 9))
    test_card.append(card.Card('C', 13))

    test = role.RoleJudge()
    test.judge(test_card)
    test_role = test.role()

    assert test_role == 4

    """
    ----------------------------------
     straight 5 6 7 8 9
    ----------------------------------
    """
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('S', 5))
    test_card.append(card.Card('D', 6))
    test_card.append(card.Card('H', 7))
    test_card.append(card.Card('D', 8))
    test_card.append(card.Card('H', 9))
    test_card.append(card.Card('C', 13))

    test = role.RoleJudge()
    test.judge(test_card)
    test_role = test.role()

    assert test_role == 4

    """
    ----------------------------------
     straight 10 11 12 13 1
    ----------------------------------
    """
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('S', 5))
    test_card.append(card.Card('D', 6))
    test_card.append(card.Card('H', 10))
    test_card.append(card.Card('D', 11))
    test_card.append(card.Card('H', 12))
    test_card.append(card.Card('C', 13))

    test = role.RoleJudge()
    test.judge(test_card)
    test_role = test.role()

    assert test_role == 4


def test_judge_flush():
    """
    ----------------------------------
     flush
    ----------------------------------
    """
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('C', 2))
    test_card.append(card.Card('C', 5))
    test_card.append(card.Card('C', 7))
    test_card.append(card.Card('C', 8))
    test_card.append(card.Card('C', 9))
    test_card.append(card.Card('C', 13))

    test = role.RoleJudge()
    test.judge(test_card)
    test_role = test.role()

    assert test_role == 5


def test_judge_full_house():
    """
    ----------------------------------
     fullhouse
    ----------------------------------
    """
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('S', 1))
    test_card.append(card.Card('D', 1))
    test_card.append(card.Card('H', 7))
    test_card.append(card.Card('D', 7))
    test_card.append(card.Card('C', 7))
    test_card.append(card.Card('C', 13))

    test = role.RoleJudge()
    test.judge(test_card)
    test_role = test.role()

    assert test_role == 6


def test_judge_four_of_kind():
    """
    ----------------------------------
     four of kind
    ----------------------------------
    """
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('D', 2))
    test_card.append(card.Card('H', 2))
    test_card.append(card.Card('S', 2))
    test_card.append(card.Card('C', 2))
    test_card.append(card.Card('C', 4))
    test_card.append(card.Card('H', 12))

    test = role.RoleJudge()
    test.judge(test_card)
    test_role = test.role()

    assert test_role == 7


def test_judge_straight_flush():
    """
    ----------------------------------
     straight flush
    ----------------------------------
    """
    test_card = []
    test_card.append(card.Card('H', 1))
    test_card.append(card.Card('C', 2))
    test_card.append(card.Card('C', 6))
    test_card.append(card.Card('C', 7))
    test_card.append(card.Card('C', 8))
    test_card.append(card.Card('C', 9))
    test_card.append(card.Card('C', 10))

    test = role.RoleJudge()
    test.judge(test_card)
    test_role = test.role()

    assert test_role == 8

    """
    ----------------------------------
     royal flush
    ----------------------------------
    """
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('C', 2))
    test_card.append(card.Card('C', 6))
    test_card.append(card.Card('C', 10))
    test_card.append(card.Card('C', 11))
    test_card.append(card.Card('C', 12))
    test_card.append(card.Card('C', 13))

    test = role.RoleJudge()
    test.judge(test_card)
    test_role = test.role()

    assert test_role == 9


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
