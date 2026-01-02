#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    polymer = f.read().strip()
    f.close()
    return polymer


def reduce(polymer):
    new_polymer = ''
    i = 0
    while i < len(polymer) - 1:
        c = polymer[i]
        d = polymer[i + 1]
        if c == d or c.upper() != d.upper():
            new_polymer += c
            i += 1
        else:
            i += 2
    if (len(polymer) - len(new_polymer)) % 2 == 1:
        new_polymer += polymer[-1]
    return new_polymer


def len_reduced(polymer):
    while True:
        new_polymer = reduce(polymer)
        if len(new_polymer) == len(polymer):
            return len(polymer)
        polymer = new_polymer


def sol1(filename):
    polymer = get_input(filename)
    return len_reduced(polymer)


def sol2(filename):
    polymer = get_input(filename)
    min_len_reduced = len_reduced(polymer)
    for ord_l in range(ord('a'), ord('z') + 1):
        l = chr(ord_l)
        pol = polymer.replace(l, '').replace(l.upper(), '')
        min_len_reduced = min(min_len_reduced, len_reduced(pol))
    return min_len_reduced


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
