import pytest

from texas_holdem import (
    games,
)


def test_deal():
    for i in range(2, 6):
        expected_out = i
        test_game = games.Game(i)
        test_game.deal()
        assert len(test_game.players) == expected_out

    for i in range(len(test_game.players)):
        assert len(test_game.players[i].hand) == 2



def test_preflop():
    assert True


def test_flop():
    test_game = games.Game()
    test_game.deal()
    test_game.preflop()
    assert len(test_game.game_field.community_card) == 0
    test_game.flop()
    assert len(test_game.game_field.community_card) == 3


def test_turn():
    test_game = games.Game()
    test_game.deal()
    test_game.preflop()
    test_game.flop()
    assert len(test_game.game_field.community_card) == 3
    test_game.turn()
    assert len(test_game.game_field.community_card) == 4


def test_river():
    test_game = games.Game()
    test_game.deal()
    test_game.preflop()
    test_game.flop()
    test_game.turn()
    assert len(test_game.game_field.community_card) == 4
    test_game.river()
    assert len(test_game.game_field.community_card) == 5


def test_showdown():
    assert True


def test_role_judge():
    assert True


def test_progress():
    assert True
