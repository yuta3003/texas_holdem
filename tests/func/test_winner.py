from texas_holdem import (
    card,
    player,
    winner,
)


def test_check_hand():
    """
    Player1 勝利
    """
    players = []
    player1_hand = []
    player1_hand.append(card.Card('C', 1))
    player1_hand.append(card.Card('H', 1))
    player1_hand.append(card.Card('C', 10))
    player1_hand.append(card.Card('D', 8))
    player1_hand.append(card.Card('S', 4))
    player1 = player.Player('Player1')
    player1.hand = player1_hand
    players.append(player1)

    player2_hand = []
    player2_hand.append(card.Card('C', 1))
    player2_hand.append(card.Card('H', 1))
    player2_hand.append(card.Card('C', 10))
    player2_hand.append(card.Card('D', 3))
    player2_hand.append(card.Card('S', 2))
    player2 = player.Player('Player2')
    player2.hand = player2_hand
    players.append(player2)

    player3_hand = []
    player3_hand.append(card.Card('C', 1))
    player3_hand.append(card.Card('H', 12))
    player3_hand.append(card.Card('C', 10))
    player3_hand.append(card.Card('D', 3))
    player3_hand.append(card.Card('S', 2))
    player3 = player.Player('player3')
    player3.hand = player3_hand
    players.append(player3)

    victory_player1 = winner.Winner(players)
    victory_player1.players_role_list = [1, 1, 0]
    same_role_index_list = [0, 1]
    test_winner_index = victory_player1.check_rank(same_role_index_list)
    expected_index = 0
    assert test_winner_index == expected_index

    """
    Player2 勝利
    """
    players = []
    player1_hand = []
    player1_hand.append(card.Card('C', 7))
    player1_hand.append(card.Card('H', 7))
    player1_hand.append(card.Card('C', 10))
    player1_hand.append(card.Card('D', 8))
    player1_hand.append(card.Card('S', 4))
    player1 = player.Player('Player1')
    player1.hand = player1_hand
    players.append(player1)

    player2_hand = []
    player2_hand.append(card.Card('C', 13))
    player2_hand.append(card.Card('H', 13))
    player2_hand.append(card.Card('C', 1))
    player2_hand.append(card.Card('D', 5))
    player2_hand.append(card.Card('S', 2))
    player2 = player.Player('Player2')
    player2.hand = player2_hand
    players.append(player2)

    victory_player2 = winner.Winner(players)
    victory_player2.players_role_list = [1, 1]
    same_role_index_list = [0, 1]
    test_winner_index = victory_player2.check_rank(same_role_index_list)
    expected_index = 1
    assert test_winner_index == expected_index

    """
    Draw
    """
    players = []
    player1_hand = []
    player1_hand.append(card.Card('C', 1))
    player1_hand.append(card.Card('H', 1))
    player1_hand.append(card.Card('C', 7))
    player1_hand.append(card.Card('D', 7))
    player1_hand.append(card.Card('S', 4))
    player1 = player.Player('Player1')
    player1.hand = player1_hand
    players.append(player1)

    player2_hand = []
    player2_hand.append(card.Card('C', 1))
    player2_hand.append(card.Card('H', 1))
    player2_hand.append(card.Card('C', 7))
    player2_hand.append(card.Card('D', 7))
    player2_hand.append(card.Card('S', 4))
    player2 = player.Player('Player2')
    player2.hand = player2_hand
    players.append(player2)

    draw = winner.Winner(players)
    draw.players_role_list = [2, 2]
    same_role_index_list = [0, 1]
    test_winner_index = draw.check_rank(same_role_index_list)
    expected_index = -1
    assert test_winner_index == expected_index


def test_judge():
    """
    Only Role
    """
    players = []
    player1_hand = []
    player1_hand.append(card.Card('C', 1))
    player1_hand.append(card.Card('H', 1))
    player1_hand.append(card.Card('C', 7))
    player1_hand.append(card.Card('D', 6))
    player1_hand.append(card.Card('S', 4))
    player1 = player.Player('Player1')
    player1.hand = player1_hand
    player1.role = 1
    players.append(player1)

    player2_hand = []
    player2_hand.append(card.Card('C', 1))
    player2_hand.append(card.Card('H', 1))
    player2_hand.append(card.Card('C', 7))
    player2_hand.append(card.Card('D', 7))
    player2_hand.append(card.Card('S', 4))
    player2 = player.Player('Player2')
    player2.hand = player2_hand
    player2.role = 2
    players.append(player2)

    player3_hand = []
    player3_hand.append(card.Card('C', 1))
    player3_hand.append(card.Card('H', 7))
    player3_hand.append(card.Card('C', 10))
    player3_hand.append(card.Card('D', 3))
    player3_hand.append(card.Card('S', 2))
    player3 = player.Player('player3')
    player3.hand = player3_hand
    player3.role = 0
    players.append(player3)

    only_role = winner.Winner(players)
    test_winner_index = only_role.judge()
    expected_index = 1
    assert test_winner_index == expected_index

    """
    Not Only Role
    """
    players = []
    player1_hand = []
    player1_hand.append(card.Card('C', 1))
    player1_hand.append(card.Card('H', 1))
    player1_hand.append(card.Card('C', 6))
    player1_hand.append(card.Card('D', 6))
    player1_hand.append(card.Card('S', 4))
    player1 = player.Player('Player1')
    player1.hand = player1_hand
    player1.role = 2
    players.append(player1)

    player2_hand = []
    player2_hand.append(card.Card('C', 1))
    player2_hand.append(card.Card('H', 1))
    player2_hand.append(card.Card('C', 7))
    player2_hand.append(card.Card('D', 7))
    player2_hand.append(card.Card('S', 4))
    player2 = player.Player('Player2')
    player2.hand = player2_hand
    player2.role = 2
    players.append(player2)

    player3_hand = []
    player3_hand.append(card.Card('C', 1))
    player3_hand.append(card.Card('H', 1))
    player3_hand.append(card.Card('C', 7))
    player3_hand.append(card.Card('D', 7))
    player3_hand.append(card.Card('S', 2))
    player3 = player.Player('player3')
    player3.hand = player3_hand
    player3.role = 2
    players.append(player3)

    only_role = winner.Winner(players)
    test_winner_index = only_role.judge()
    expected_index = 1
    assert test_winner_index == expected_index
