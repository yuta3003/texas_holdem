import pytest

from src import (
    deck,
    field,
)


game_deck = deck.Deck()
game_field = field.Field()


def test_flop():
    game_field.flop(game_deck)
    assert True


def test_turn():
    game_field.turn(game_deck)
    assert True


def test_river():
    game_field.river(game_deck)
    assert True


def test_show_card():
    # game_field.show_card()
    assert True
