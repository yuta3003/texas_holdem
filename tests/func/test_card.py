import pytest

from src import card


def test_suit():
    for i in ["C", "D", "H", "S"]:
        for j in range(1, 14):
            test_card = card.Card(i, j)
            assert card.Card.suit(test_card) == i


def test_number():
    for i in ["C", "D", "H", "S"]:
        for j in range(1, 14):
            test_card = card.Card(i, j)
            assert card.Card.number(test_card) == j


def test_show():
    assert True
