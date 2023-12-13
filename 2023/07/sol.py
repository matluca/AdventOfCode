#!/usr/bin/env python3
from collections import Counter
from functools import cmp_to_key


def get_input(filename):
    f = open(filename, 'r')
    bibs = {}
    for line in f:
        bibs[line.split(' ')[0]] = int(line.strip().split(' ')[1])
    f.close()
    return bibs


def card_value(c):
    if c.isdigit():
        return int(c)
    if c == 'T':
        return 10
    if c == 'J':
        return 11
    elif c == 'Q':
        return 12
    elif c == 'K':
        return 13
    elif c == 'A':
        return 14


def card_value_2(c):
    if c == 'J':
        return 1
    return card_value(c)


def hand_rank(hand_counter):
    c = len(hand_counter)
    if c == 5:
        return 0  # High card
    if c == 4:
        return 1  # One pair
    if c == 3:
        if 3 in hand_counter.values():
            return 3  # Three of a kind
        return 2  # Two pairs
    if c == 2:
        if 3 in hand_counter.values():
            return 4  # Full house
        return 5  # Four of a kind
    return 6  # Five of a kind


def compare(hand1, hand2):
    counters = [Counter(hand1), Counter(hand2)]
    rank = [0, 0]
    for i in range(len(counters)):
        rank[i] = hand_rank(counters[i])
    if rank[0] > rank[1]:
        return 1
    elif rank[0] < rank[1]:
        return -1
    for i in range(len(hand1)):
        if card_value(hand1[i]) == card_value(hand2[i]):
            continue
        if card_value(hand1[i]) > card_value(hand2[i]):
            return 1
        elif card_value(hand1[i]) < card_value(hand2[i]):
            return -1
    return 0


def compare2(hand1, hand2):
    counters = [Counter(hand1), Counter(hand2)]
    rank = [0, 0]
    for i in range(len(counters)):
        c = counters[i]
        sorted_dict = sorted(c.items(), key=lambda x: x[1])
        sorted_dict.reverse()
        keys = [i[0] for i in sorted_dict]
        top_card = keys[0]
        if top_card == 'J' and len(keys) > 1:
            top_card = keys[1]
        if 'J' in keys and len(keys) > 1:
            c[top_card] += c['J']
            del c['J']
        rank[i] = hand_rank(c)
    if rank[0] > rank[1]:
        return 1
    elif rank[0] < rank[1]:
        return -1
    for i in range(len(hand1)):
        if card_value_2(hand1[i]) == card_value_2(hand2[i]):
            continue
        if card_value_2(hand1[i]) > card_value_2(hand2[i]):
            return 1
        elif card_value_2(hand1[i]) < card_value_2(hand2[i]):
            return -1
    return 0


def sol(filename, comp_func):
    bibs = get_input(filename)
    sorted_hands = sorted(bibs.keys(), key=cmp_to_key(comp_func))
    res = 0
    for i in range(len(sorted_hands)):
        res += (i + 1) * bibs[sorted_hands[i]]
    return res


def sol1(filename):
    return sol(filename, compare)


def sol2(filename):
    return sol(filename, compare2)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
