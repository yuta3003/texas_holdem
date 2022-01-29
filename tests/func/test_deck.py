import pytest
from src import(
    deck,
)


game_deck = deck.Deck()


def test_build():
    game_deck.build()

def test_shuffle():
    game_deck.shuffle()

def test_show():
    game_deck.show()

def test_draw_card():
    game_deck.draw_card()
