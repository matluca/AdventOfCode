#!/usr/bin/env python3

def get_input(filename):
    lines = open(filename, 'r').readlines()
    return [[int(n) for n in line.split(' ')] for line in lines]


def get_next(history):
    res = 0
    current = history
    while set(current) != {0}:
        res += current[-1]
        current = [current[i+1] - current[i] for i in range(len(current)-1)]
    return res


def get_previous(history):
    i, res = 0, 0
    current = history
    while set(current) != {0}:
        res += current[0] * pow(-1, i)
        current = [current[i+1] - current[i] for i in range(len(current)-1)]
        i += 1
    return res


def sol1(filename):
    histories = get_input(filename)
    return sum([get_next(h) for h in histories])


def sol2(filename):
    histories = get_input(filename)
    return sum([get_previous(h) for h in histories])


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
