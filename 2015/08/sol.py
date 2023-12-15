#!/usr/bin/env python3


def get_input(filename):
    f = open(filename, 'r').read()
    return f.split('\n')


def sol1(filename):
    strings = get_input(filename)
    res = 0
    for s in strings:
        dec = bytes(s, 'utf-8').decode('unicode-escape')
        res += len(s) - len(dec) + 2
    return res


def sol2(filename):
    strings = get_input(filename)
    res = 0
    for s in strings:
        res += s.count("\"") + s.count("\\") + 2
    return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
