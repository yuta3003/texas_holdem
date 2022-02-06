import pytest

from src import (
    card,
    role,
)

@pytest.fixture
def one_pair():
    test = role.Role()

    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('C', 3))
    test_card.append(card.Card('H', 3))
    test_card.append(card.Card('S', 6))
    test_card.append(card.Card('H', 7))
    test_card.append(card.Card('D', 8))
    test_card.append(card.Card('S', 12))

    test.judge(test_card)
    return test

@pytest.fixture
def two_pair():
    test = role.Role()

    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('D', 1))
    test_card.append(card.Card('H', 3))
    test_card.append(card.Card('S', 3))
    test_card.append(card.Card('S', 6))
    test_card.append(card.Card('S', 12))
    test_card.append(card.Card('H', 13))

    test.judge(test_card)
    return test

@pytest.fixture
def three_pair():
    test = role.Role()

    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('D', 1))
    test_card.append(card.Card('H', 3))
    test_card.append(card.Card('S', 3))
    test_card.append(card.Card('S', 6))
    test_card.append(card.Card('S', 12))
    test_card.append(card.Card('H', 12))

    test.judge(test_card)
    return test

@pytest.fixture
def three_of_kind():
    test = role.Role()

    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('D', 2))
    test_card.append(card.Card('H', 2))
    test_card.append(card.Card('S', 2))
    test_card.append(card.Card('D', 3))
    test_card.append(card.Card('C', 4))
    test_card.append(card.Card('H', 12))

    test.judge(test_card)
    return test

@pytest.fixture
def straight1():
    test = role.Role()

    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('S', 2))
    test_card.append(card.Card('D', 3))
    test_card.append(card.Card('H', 4))
    test_card.append(card.Card('D', 5))
    test_card.append(card.Card('H', 9))
    test_card.append(card.Card('C', 13))

    test.judge(test_card)
    return test

@pytest.fixture
def straight2():
    test = role.Role()

    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('S', 5))
    test_card.append(card.Card('D', 6))
    test_card.append(card.Card('H', 7))
    test_card.append(card.Card('D', 8))
    test_card.append(card.Card('H', 9))
    test_card.append(card.Card('C', 13))

    test.judge(test_card)
    return test

@pytest.fixture
def straight3():
    test = role.Role()

    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('S', 5))
    test_card.append(card.Card('D', 6))
    test_card.append(card.Card('H', 10))
    test_card.append(card.Card('D', 11))
    test_card.append(card.Card('H', 12))
    test_card.append(card.Card('C', 13))

    test.judge(test_card)
    return test

@pytest.fixture
def flush():
    test = role.Role()

    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('C', 2))
    test_card.append(card.Card('C', 5))
    test_card.append(card.Card('C', 7))
    test_card.append(card.Card('C', 8))
    test_card.append(card.Card('C', 9))
    test_card.append(card.Card('C', 13))

    test.judge(test_card)
    return test

@pytest.fixture
def fullhouse():
    test = role.Role()

    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('S', 1))
    test_card.append(card.Card('D', 1))
    test_card.append(card.Card('H', 7))
    test_card.append(card.Card('D', 7))
    test_card.append(card.Card('C', 7))
    test_card.append(card.Card('C', 13))

    test.judge(test_card)
    return test

@pytest.fixture
def four_of_kind():
    test = role.Role()

    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('D', 2))
    test_card.append(card.Card('H', 2))
    test_card.append(card.Card('S', 2))
    test_card.append(card.Card('C', 2))
    test_card.append(card.Card('C', 4))
    test_card.append(card.Card('H', 12))

    test.judge(test_card)
    return test

@pytest.fixture
def straight_flush():
    test = role.Role()

    test_card = []
    test_card.append(card.Card('H', 1))
    test_card.append(card.Card('C', 2))
    test_card.append(card.Card('C', 6))
    test_card.append(card.Card('C', 7))
    test_card.append(card.Card('C', 8))
    test_card.append(card.Card('C', 9))
    test_card.append(card.Card('C', 10))

    test.judge(test_card)
    return test

@pytest.fixture
def royal_flush():
    test = role.Role()

    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('C', 2))
    test_card.append(card.Card('C', 6))
    test_card.append(card.Card('C', 10))
    test_card.append(card.Card('C', 11))
    test_card.append(card.Card('C', 12))
    test_card.append(card.Card('C', 13))

    test.judge(test_card)
    return test

@pytest.fixture
def same_number1():
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('C', 3))
    test_card.append(card.Card('H', 5))
    test_card.append(card.Card('S', 6))
    test_card.append(card.Card('H', 7))
    test_card.append(card.Card('D', 8))
    test_card.append(card.Card('S', 12))

    return test_card

@pytest.fixture
def same_number2():
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('C', 3))
    test_card.append(card.Card('H', 3))
    test_card.append(card.Card('S', 6))
    test_card.append(card.Card('H', 6))
    test_card.append(card.Card('D', 8))
    test_card.append(card.Card('S', 12))

    return test_card

@pytest.fixture
def same_number3():
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('C', 3))
    test_card.append(card.Card('H', 3))
    test_card.append(card.Card('S', 6))
    test_card.append(card.Card('H', 6))
    test_card.append(card.Card('D', 6))
    test_card.append(card.Card('S', 8))

    return test_card

@pytest.fixture
def same_number4():
    test_card = []
    test_card.append(card.Card('C', 1))
    test_card.append(card.Card('C', 3))
    test_card.append(card.Card('H', 6))
    test_card.append(card.Card('S', 6))
    test_card.append(card.Card('H', 6))
    test_card.append(card.Card('D', 6))
    test_card.append(card.Card('S', 8))

    return test_card
