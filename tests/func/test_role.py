import collections

import pytest

from src import (
    card,
    role,
)


def test_judge_pair():
    pass


def test_judge_three_of_kind():
    pass


def test_judge_straight():
    pass


def test_judge_flush():
    pass


def test_judge_full_house():
    pass


def test_judge_four_of_kind():
    pass


def test_judge_straight_flush():
    pass


def test_how_many_same_numbers():
    """
    ----------------------------------
     same number = 1
    ----------------------------------
    """
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('C', 3))
    test_card.append(card.Card('H', 5))
    test_card.append(card.Card('S', 6))
    test_card.append(card.Card('H', 7))
    test_card.append(card.Card('D', 8))
    test_card.append(card.Card('S', 12))

    test = role.RoleJudge()
    test_number = test.how_many_same_numbers(test_card)
    expected_number = 1

    assert test_number == expected_number


    """
    ----------------------------------
     same number = 2
    ----------------------------------
    """
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('C', 3))
    test_card.append(card.Card('H', 3))
    test_card.append(card.Card('S', 6))
    test_card.append(card.Card('H', 6))
    test_card.append(card.Card('D', 8))
    test_card.append(card.Card('S', 12))

    test = role.RoleJudge()
    test_number = test.how_many_same_numbers(test_card)
    expected_number = 2

    assert test_number == expected_number

    """
    ----------------------------------
     same number = 3
    ----------------------------------
    """
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('C', 3))
    test_card.append(card.Card('H', 3))
    test_card.append(card.Card('S', 6))
    test_card.append(card.Card('H', 6))
    test_card.append(card.Card('D', 6))
    test_card.append(card.Card('S', 8))

    test = role.RoleJudge()
    test_number = test.how_many_same_numbers(test_card)
    expected_number = 3

    assert test_number == expected_number

    """
    ----------------------------------
     same number = 4
    ----------------------------------
    """
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('C', 3))
    test_card.append(card.Card('H', 6))
    test_card.append(card.Card('S', 6))
    test_card.append(card.Card('H', 6))
    test_card.append(card.Card('D', 6))
    test_card.append(card.Card('S', 8))

    test = role.RoleJudge()
    test_number = test.how_many_same_numbers(test_card)
    expected_number = 4

    assert test_number == expected_number


def test_judge():
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

    test = role.RoleJudge()
    test.judge(test_card)
    test_role = test.role
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

    test = role.RoleJudge()
    test.judge(test_card)
    test_role = test.role
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
    test_role = test.role

    assert test_role == 2

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
    test_role = test.role

    assert test_role == 3

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
    test_role = test.role

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
    test_role = test.role

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
    test_role = test.role

    assert test_role == 4

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
    test_role = test.role

    assert test_role == 5

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
    test_role = test.role

    assert test_role == 6

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
    test_role = test.role

    assert test_role == 7

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
    test_role = test.role

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
    test_role = test.role

    assert test_role == 9
