#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    moves = f.readlines()
    f.close()
    return [m.strip() for m in moves]


def cut(deck, amount):
    return deck[amount:] + deck[:amount]


def deal_with_increment(deck, amount):
    new_deck = deck.copy()
    size = len(deck)
    for i, c in enumerate(deck):
        new_deck[(i * amount) % size] = c
    return new_deck


def sol1(filename, n_cards, card):
    deck = list(range(n_cards))
    moves = get_input(filename)
    for move in moves:
        if move == 'deal into new stack':
            deck = list(reversed(deck))
        elif move.startswith('cut'):
            amount = int(move.split()[1])
            deck = cut(deck, amount)
        elif move.startswith('deal with increment'):
            amount = int(move.split()[3])
            deck = deal_with_increment(deck, amount)
    return deck.index(card)


def previous(moves, n_cards, position):
    for move in reversed(moves):
        if move == 'deal into new stack':
            position = n_cards - position - 1
        elif move.startswith('cut'):
            amount = int(move.split()[1])
            position = (position + amount) % n_cards
        elif move.startswith('deal with increment'):
            amount = int(move.split()[3])
            position = (pow(amount, -1, n_cards) * position) % n_cards
    return position


def sol2(filename, n_cards, repetitions, position):
    moves = get_input(filename)
    # solve y = f(a) = a * x + b, with x = position
    #       z = f(f(a)) = a * y + b
    y = previous(moves, n_cards, position)
    z = previous(moves, n_cards, y)
    a = (y - z) * pow(position - y, -1, n_cards) % n_cards
    b = (y - a * position) % n_cards
    # compute f^repetitions(x)
    return (pow(a, repetitions, n_cards) * position + (pow(a, repetitions, n_cards) - 1) * pow(a - 1, -1, n_cards) * b) % n_cards


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 10, 5)}')
    print(f'Solution: {sol1("input.txt", 10007, 2019)}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt", 119315717514047, 101741582076661, 2020)}')
