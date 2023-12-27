#!/usr/bin/env python3
import re


def get_input(filename):
    f = open(filename, 'r').read()
    replacements_raw, start = f.split('\n\n')
    replacements = []
    for line in replacements_raw.split('\n'):
        replacements.append(line.split(' => '))
    return replacements, start


def get_replacements(replacements, start):
    possibilities = set()
    for replacement in replacements:
        old, new = replacement
        for s in [m.start() for m in re.finditer(old, start)]:
            possibilities.add(start[:s] + new + start[s+len(old):])
    return possibilities


def sol1(filename):
    replacements, start = get_input(filename)
    return len(get_replacements(replacements, start))


def sol2(filename):
    _, start = get_input(filename)
    n_parentheses = start.count('Ar') + start.count('Rn')
    n_y = start.count('Y')
    n_upper = sum(1 for c in start if c.isupper())
    return n_upper - n_parentheses - 2 * n_y - 1


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
