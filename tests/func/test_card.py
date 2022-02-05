import pytest

from src import card


def test_suit():
    for i in ["C", "D", "H", "S"]:
        for j in range(1, 14):
            test_card = card.Card(i, j)
            assert test_card.suit == i


def test_number():
    for i in ["C", "D", "H", "S"]:
        for j in range(1, 14):
            test_card = card.Card(i, j)
            assert test_card.number(ace14=False) == j

    for i in ["C", "D", "H", "S"]:
        for j in range(2, 15):
            test_card = card.Card(i, j)
            assert test_card.number(ace14=True) == j


def test_show():
    assert True
