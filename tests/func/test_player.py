import pytest

from texas_holdem import (
    card,
    deck,
    player,
)


game_deck = deck.Deck()
game_player = player.Player(game_deck)


def test_draw():
    pre_test_hand_len = len(game_player.hand)
    pre_test_deck_len = len(game_deck.cards)

    game_player.draw(game_deck)

    post_test_hand_len = len(game_player.hand)
    post_test_deck_len = len(game_deck.cards)

    assert pre_test_hand_len + 1 == post_test_hand_len
    assert pre_test_deck_len - 1 == post_test_deck_len



def test_show_hand(capfd):
    expected_hand = []
    expected_hand.append(card.Card('C', 2))
    expected_hand.append(card.Card('C', 5))
    expected_hand.append(card.Card('C', 7))
    expected_hand.append(card.Card('C', 9))
    expected_hand.append(card.Card('C', 12))
    game_player.hand = expected_hand

    game_player.show_hand()

    expected_out = 'C2'
    expected_out += '\n'
    expected_out += 'C5'
    expected_out += '\n'
    expected_out += 'C7'
    expected_out += '\n'
    expected_out += 'C9'
    expected_out += '\n'
    expected_out += 'C12'
    expected_out += '\n'

    out, err = capfd.readouterr()
    assert out == expected_out
    assert err == ''
