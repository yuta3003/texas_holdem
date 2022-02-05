import collections

import pytest

from src import (
    card,
    role,
)


def test_update_role():
    pass


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



def test_how_many_same_numbers1(same_number1):
    test = role.RoleJudge()
    test_number = test.how_many_same_numbers(same_number1)

    expected_number = 1
    assert test_number == expected_number

def test_how_many_same_numbers2(same_number2):
    test = role.RoleJudge()
    test_number = test.how_many_same_numbers(same_number2)

    expected_number = 2
    assert test_number == expected_number

def test_how_many_same_numbers3(same_number3):
    test = role.RoleJudge()
    test_number = test.how_many_same_numbers(same_number3)

    expected_number = 3
    assert test_number == expected_number

def test_how_many_same_numbers4(same_number4):
    test = role.RoleJudge()
    test_number = test.how_many_same_numbers(same_number4)

    expected_number = 4
    assert test_number == expected_number

def test_judge_one_pair(one_pair):
    test_role = one_pair.role
    assert test_role == 1

def test_judge_two_pair(two_pair):
    test_role = two_pair.role
    assert test_role == 2

def test_judge_three_pair(three_pair):
    test_role = three_pair.role
    assert test_role == 2

def test_judge_three_of_kind(three_of_kind):
    test_role = three_of_kind.role
    assert test_role == 3

def test_judge_straight1(straight1):
    test_role = straight1.role
    assert test_role == 4

def test_judge_straight2(straight2):
    test_role = straight2.role
    assert test_role == 4

def test_judge_straight3(straight3):
    test_role = straight3.role
    assert test_role == 4

def test_judge_flush(flush):
    test_role = flush.role
    assert test_role == 5

def test_judge_fullhouse(fullhouse):
    test_role = fullhouse.role
    assert test_role == 6

def test_judge_four_of_kind(four_of_kind):
    test_role = four_of_kind.role
    assert test_role == 7

def test_judge_straight_flush(straight_flush):
    test_role = straight_flush.role
    assert test_role == 8

def test_judge_royal_flush(royal_flush):
    test_role = royal_flush.role
    assert test_role == 9
