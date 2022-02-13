import pytest

from texas_holdem import (
    card,
    deck,
    field,
)


game_deck = deck.Deck()
game_field = field.Field()


def test_flop():
    pre_test_field_len = len(game_field.community_card)
    pre_test_deck_len = len(game_deck.cards)

    game_field.flop(game_deck)

    post_test_field_len = len(game_field.community_card)
    post_test_deck_len = len(game_deck.cards)

    assert pre_test_field_len + 3 == post_test_field_len
    assert pre_test_deck_len - 3 == post_test_deck_len


def test_turn():
    pre_test_field_len = len(game_field.community_card)
    pre_test_deck_len = len(game_deck.cards)

    game_field.turn(game_deck)

    post_test_field_len = len(game_field.community_card)
    post_test_deck_len = len(game_deck.cards)

    assert pre_test_field_len + 1 == post_test_field_len
    assert pre_test_deck_len - 1 == post_test_deck_len


def test_river():
    pre_test_field_len = len(game_field.community_card)
    pre_test_deck_len = len(game_deck.cards)

    game_field.river(game_deck)

    post_test_field_len = len(game_field.community_card)
    post_test_deck_len = len(game_deck.cards)

    assert pre_test_field_len + 1 == post_test_field_len
    assert pre_test_deck_len - 1 == post_test_deck_len


def test_show_card(capfd):
    expected_out = []
    expected_out.append(card.Card('C', 2))
    expected_out.append(card.Card('C', 5))
    expected_out.append(card.Card('C', 7))
    expected_out.append(card.Card('C', 9))
    expected_out.append(card.Card('C', 12))
    game_field.community_card = expected_out

    game_field.show_card()

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
