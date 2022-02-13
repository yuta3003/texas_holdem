import pytest

from src import (
    card,
    deck,
)


game_deck = deck.Deck()


def test_build():
    expected_deck = []
    for i in ["C", "D", "H", "S"]:
        for j in range(1, 14):
            expected_deck.append(card.Card(i, j))


def test_shuffle():
    game_deck.shuffle()
    assert True


def test_show(capfd):
    expected_out = []
    expected_out.append(card.Card('C', 2))
    expected_out.append(card.Card('C', 5))
    expected_out.append(card.Card('C', 7))
    expected_out.append(card.Card('C', 9))
    expected_out.append(card.Card('C', 12))
    game_deck.cards = expected_out

    game_deck.show()

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

def test_draw_card(capfd):
    expected_out = []
    expected_out.append(card.Card('C', 2))
    expected_out.append(card.Card('C', 5))
    expected_out.append(card.Card('C', 7))
    expected_out.append(card.Card('C', 9))
    expected_out.append(card.Card('C', 12))
    game_deck.cards = expected_out

    expected_out = ['C12\nNone\n', 'C9\nNone\n', 'C7\nNone\n', 'C5\nNone\n', 'C2\nNone\n']

    for i in range(len(expected_out)):
        test_draw_card = game_deck.draw_card()
        print(test_draw_card.show())
        out, err = capfd.readouterr()
        assert out == expected_out[i]
        assert err == ''
