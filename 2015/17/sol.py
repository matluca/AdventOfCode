#!/usr/bin/env python3
import itertools


def get_input(filename):
    f = open(filename, 'r')
    containers = []
    for line in f:
        containers.append(int(line.strip()))
    f.close()
    return containers


def sol1(filename, target):
    containers = get_input(filename)
    res = 0
    for i in range(1, len(containers)+1):
        for comb in itertools.combinations(containers, i):
            if sum(comb) == target:
                res += 1
    return res


def sol2(filename, target):
    containers = get_input(filename)
    for i in range(1, len(containers)+1):
        res = 0
        for comb in itertools.combinations(containers, i):
            if sum(comb) == target:
                res += 1
        if res > 0:
            return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 25)}')
    print(f'Solution: {sol1("input.txt", 150)}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt", 25)}')
    print(f'Solution: {sol2("input.txt", 150)}')
