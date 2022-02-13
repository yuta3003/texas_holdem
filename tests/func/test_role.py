import collections

import pytest

from texas_holdem import (
    card,
    role,
)


def test_update_role():
    """
    UPDATE 実行
    """
    test_role = role.Role()
    dummy_role = 1
    test_role.role = dummy_role
    dummy_hand = []
    dummy_hand.append(card.Card('C', 1))
    dummy_hand.append(card.Card('C', 1))
    dummy_hand.append(card.Card('C', 1))
    dummy_hand.append(card.Card('C', 1))
    dummy_hand.append(card.Card('C', 1))
    test_role.hand = dummy_hand

    expected_hand = []
    expected_hand.append(card.Card('C', 2))
    expected_hand.append(card.Card('C', 2))
    expected_hand.append(card.Card('C', 2))
    expected_hand.append(card.Card('C', 2))
    expected_hand.append(card.Card('C', 2))
    expected_role = 2
    test_role.update_role(expected_role, expected_hand)

    assert test_role.role == expected_role
    assert test_role.hand == expected_hand

    """
    UPDATE 実行されない
    """
    test_role = role.Role()
    expected_role = 5
    test_role.role = expected_role
    expected_hand = []
    expected_hand.append(card.Card('C', 1))
    expected_hand.append(card.Card('C', 1))
    expected_hand.append(card.Card('C', 1))
    expected_hand.append(card.Card('C', 1))
    expected_hand.append(card.Card('C', 1))
    test_role.hand = expected_hand

    dummy_hand = []
    dummy_hand.append(card.Card('C', 2))
    dummy_hand.append(card.Card('C', 2))
    dummy_hand.append(card.Card('C', 2))
    dummy_hand.append(card.Card('C', 2))
    dummy_hand.append(card.Card('C', 2))
    dummy_role = 2
    test_role.update_role(dummy_role, dummy_hand)

    assert test_role.role == expected_role
    assert test_role.hand == expected_hand



def test_judge_pair():
    """
    A Pair
    """
    test_role = role.Role()
    test_role.role = 0
    expected_role = 1

    expected_hand = []
    expected_hand.append(card.Card('C', 1))
    expected_hand.append(card.Card('C', 1))
    expected_hand.append(card.Card('H', 10))
    expected_hand.append(card.Card('D', 5))
    expected_hand.append(card.Card('S', 2))

    test_role.judge_pair(expected_hand)

    assert test_role.role == expected_role
    assert test_role.hand == expected_hand


    """
    Two Pair
    """
    test_role = role.Role()
    test_role.role = 0
    expected_role = 2

    expected_hand = []
    expected_hand.append(card.Card('C', 1))
    expected_hand.append(card.Card('C', 1))
    expected_hand.append(card.Card('H', 10))
    expected_hand.append(card.Card('D', 10))
    expected_hand.append(card.Card('S', 2))

    test_role.judge_pair(expected_hand)

    assert test_role.role == expected_role
    assert test_role.hand == expected_hand


def test_judge_three_of_kind():
    test_role = role.Role()
    test_role.role = 0
    expected_role = 3

    expected_hand = []
    expected_hand.append(card.Card('C', 1))
    expected_hand.append(card.Card('C', 1))
    expected_hand.append(card.Card('H', 1))
    expected_hand.append(card.Card('D', 10))
    expected_hand.append(card.Card('S', 2))

    test_role.judge_three_of_kind(expected_hand)

    assert test_role.role == expected_role
    assert test_role.hand == expected_hand


def test_judge_straight():
    """
    1~5
    """
    test_role = role.Role()
    test_role.role = 0
    expected_role = 4

    expected_hand = []
    expected_hand.append(card.Card('C', 1))
    expected_hand.append(card.Card('C', 2))
    expected_hand.append(card.Card('H', 3))
    expected_hand.append(card.Card('D', 4))
    expected_hand.append(card.Card('S', 5))

    test_role.judge_straight(expected_hand)

    expected_hand.sort(key=lambda x: x.number(ace14=True), reverse=True)
    assert test_role.role == expected_role
    assert test_role.hand == expected_hand

    """
    10~1
    """
    test_role = role.Role()
    test_role.role = 0
    expected_role = 4

    expected_hand = []
    expected_hand.append(card.Card('C', 1))
    expected_hand.append(card.Card('C', 13))
    expected_hand.append(card.Card('H', 12))
    expected_hand.append(card.Card('D', 11))
    expected_hand.append(card.Card('S', 10))

    test_role.judge_straight(expected_hand)

    expected_hand.sort(key=lambda x: x.number(ace14=True), reverse=True)
    assert test_role.role == expected_role
    assert test_role.hand == expected_hand

    """
    5~9
    """
    test_role = role.Role()
    test_role.role = 0
    expected_role = 4

    expected_hand = []
    expected_hand.append(card.Card('C', 5))
    expected_hand.append(card.Card('C', 6))
    expected_hand.append(card.Card('H', 7))
    expected_hand.append(card.Card('D', 8))
    expected_hand.append(card.Card('S', 9))

    test_role.judge_straight(expected_hand)

    expected_hand.sort(key=lambda x: x.number(ace14=True), reverse=True)
    assert test_role.role == expected_role
    assert test_role.hand == expected_hand


def test_judge_flush():
    test_role = role.Role()
    test_role.role = 0
    expected_role = 5

    expected_hand = []
    expected_hand.append(card.Card('C', 2))
    expected_hand.append(card.Card('C', 5))
    expected_hand.append(card.Card('C', 7))
    expected_hand.append(card.Card('C', 9))
    expected_hand.append(card.Card('C', 12))

    test_role.judge_flush(expected_hand)

    expected_hand.sort(key=lambda x: x.number(ace14=True), reverse=True)
    assert test_role.role == expected_role
    assert test_role.hand == expected_hand


def test_judge_full_house():
    test_role = role.Role()
    test_role.role = 0
    expected_role = 6

    expected_hand = []
    expected_hand.append(card.Card('C', 1))
    expected_hand.append(card.Card('C', 1))
    expected_hand.append(card.Card('H', 1))
    expected_hand.append(card.Card('D', 10))
    expected_hand.append(card.Card('S', 10))

    test_role.judge_three_of_kind(expected_hand)

    assert test_role.role == expected_role
    assert test_role.hand == expected_hand


def test_judge_four_of_kind():
    test_role = role.Role()
    test_role.role = 0
    expected_role = 7

    expected_hand = []
    expected_hand.append(card.Card('C', 1))
    expected_hand.append(card.Card('C', 1))
    expected_hand.append(card.Card('H', 1))
    expected_hand.append(card.Card('D', 1))
    expected_hand.append(card.Card('S', 10))

    test_role.judge_four_of_kind(expected_hand)

    assert test_role.role == expected_role
    assert test_role.hand == expected_hand


def test_judge_straight_flush():
    """
    straight flush
    """
    test_role = role.Role()
    test_role.role = 0
    expected_role = 8

    expected_hand = []
    expected_hand.append(card.Card('C', 2))
    expected_hand.append(card.Card('C', 3))
    expected_hand.append(card.Card('C', 4))
    expected_hand.append(card.Card('C', 5))
    expected_hand.append(card.Card('C', 6))

    test_role.judge_straight_flush(expected_hand)

    expected_hand.sort(key=lambda x: x.number(ace14=True), reverse=True)
    assert test_role.role == expected_role
    assert test_role.hand == expected_hand

    """
    royal flush
    """
    test_role = role.Role()
    test_role.role = 0
    expected_role = 9

    expected_hand = []
    expected_hand.append(card.Card('C', 10))
    expected_hand.append(card.Card('C', 11))
    expected_hand.append(card.Card('C', 12))
    expected_hand.append(card.Card('C', 13))
    expected_hand.append(card.Card('C', 1))

    test_role.judge_straight_flush(expected_hand)

    expected_hand.sort(key=lambda x: x.number(ace14=True), reverse=True)
    assert test_role.role == expected_role
    assert test_role.hand == expected_hand



def test_how_many_same_numbers(
    same_number1,
    same_number2,
    same_number3,
    same_number4,
    ):
    """
    same_number1
    """
    test = role.Role()
    test_number = test.how_many_same_numbers(same_number1)
    expected_number = 1
    assert test_number == expected_number

    """
    same_number2
    """
    test = role.Role()
    test_number = test.how_many_same_numbers(same_number2)
    expected_number = 2
    assert test_number == expected_number

    """
    same_number3
    """
    test = role.Role()
    test_number = test.how_many_same_numbers(same_number3)
    expected_number = 3
    assert test_number == expected_number

    """
    same_number4
    """
    test = role.Role()
    test_number = test.how_many_same_numbers(same_number4)
    expected_number = 4
    assert test_number == expected_number


def test_judge_one_pair(
    one_pair,
    two_pair,
    three_pair,
    three_of_kind,
    straight1,
    straight2,
    straight3,
    flush,
    fullhouse,
    four_of_kind,
    straight_flush,
    royal_flush,
    ):
    """
    one pair
    """
    test_role = one_pair.role
    assert test_role == 1

    """
    two pair
    """
    test_role = two_pair.role
    assert test_role == 2

    """
    three pair
    """
    test_role = three_pair.role
    assert test_role == 2

    """
    three of kind
    """
    test_role = three_of_kind.role
    assert test_role == 3

    """
    straight1
    """
    test_role = straight1.role
    assert test_role == 4

    """
    straight2
    """
    test_role = straight2.role
    assert test_role == 4

    """
    straight3
    """
    test_role = straight3.role
    assert test_role == 4

    """
    flush
    """
    test_role = flush.role
    assert test_role == 5

    """
    full house
    """
    test_role = fullhouse.role
    assert test_role == 6

    """
    four of kind
    """
    test_role = four_of_kind.role
    assert test_role == 7

    """
    straight flush
    """
    test_role = straight_flush.role
    assert test_role == 8

    """
    royal flush
    """
    test_role = royal_flush.role
    assert test_role == 9
