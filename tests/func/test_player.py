import pytest

from src import (
    deck,
    player,
)


game_deck = deck.Deck()
game_player = player.Player(game_deck)


def test_draw():
    game_player.draw(game_deck)


def test_show_hand():
    game_player.show_hand()
