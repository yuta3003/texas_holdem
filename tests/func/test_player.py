import pytest

from src import (
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



def test_show_hand():
    # game_player.show_hand()
    expected_hand = []
    expected_hand.append(card.Card('C', 2))
    expected_hand.append(card.Card('C', 5))
    expected_hand.append(card.Card('C', 7))
    expected_hand.append(card.Card('C', 9))
    expected_hand.append(card.Card('C', 12))

    game_player.hand = expected_hand
    for i in range(len(game_player.hand)):
        print(game_player.hand[i].number)
