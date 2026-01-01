#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    ids = [line.strip() for line in f.readlines()]
    f.close()
    return ids


def counters(id):
    c = {}
    for letter in id:
        if letter not in c.keys():
            c[letter] = 0
        c[letter] += 1
    return c


def sol1(filename):
    ids = get_input(filename)
    n2, n3 = 0, 0
    for id in ids:
        c = counters(id)
        n2 += (2 in c.values())
        n3 += (3 in c.values())
    return n2 * n3


def match(id1, id2):
    res = ''
    for i in range(len(id1)):
        if id1[i] == id2[i]:
            res += id1[i]
    return res


def sol2(filename):
    ids = get_input(filename)
    for i, id1 in enumerate(ids):
        for id2 in ids[i + 1:]:
            m = match(id1, id2)
            if len(m) == len(id1) - 1:
                return m
    return 0


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
