import pytest

from src import (
    card,
    deck,
)


test_deck = deck.Deck()


def test_build():
    expected_deck = []
    for i in ["C", "D", "H", "S"]:
        for j in range(1, 14):
            expected_deck.append(card.Card(i, j))


def test_shuffle():
    test_deck.shuffle()
    assert True


def test_show():
    test_deck.show()
    assert True


def test_draw_card():
    test_deck.draw_card()
    assert True
