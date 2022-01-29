import pytest
from src import card


def test_suit():
    test_card = card.Card('H', 1)
    assert card.Card.suit(test_card) == 'H'

def test_number():
    test_card = card.Card('H', 1)
    assert card.Card.number(test_card) == 1

def test_show():
    pass
