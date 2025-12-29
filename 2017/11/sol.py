#!/usr/bin/env python3

def get_input(filename):
    paths = []
    f = open(filename, 'r')
    for line in f.readlines():
        paths.append(line.strip().split(','))
    f.close()
    return paths


def move(p, d):
    a, r, c = p
    if d == 'sw':
        return a, r, c - 1
    if d == 'ne':
        return a, r, c + 1
    if d == 'nw':
        return 1 - a, r + a - 1, c + a - 1
    if d == 'se':
        return 1 - a, r + a, c + a
    if d == 'n':
        return 1 - a, r + a - 1, c + a
    if d == 's':
        return 1 - a, r + a, c + a - 1
    return p


def distance(p):
    return sum([abs(q) for q in p])


def sol1(filename):
    paths = get_input(filename)
    distances = []
    for path in paths:
        p = (0, 0, 0)
        for d in path:
            p = move(p, d)
        distances.append(distance(p))
    return distances


def sol2(filename):
    paths = get_input(filename)
    max_d = 0
    p = (0, 0, 0)
    for d in paths[0]:
        p = move(p, d)
        max_d = max(max_d, distance(p))
    return max_d


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
