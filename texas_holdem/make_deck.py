import random

def main():
    deck = make_deck()
    print(deck)

def make_deck():
    deck = []
    for i in ["C", "D", "H", "S"]:
        for j in range(1, 14):
            deck.append(i + str(j))
    random.shuffle(deck)
    return deck

if __name__ == '__main__':
    main()
