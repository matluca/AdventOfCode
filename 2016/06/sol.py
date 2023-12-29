#!/usr/bin/env python3
import time
from collections import Counter


def get_input(filename):
    f = open(filename, 'r').read()
    return f.split('\n')


def sol1(filename):
    f = get_input(filename)
    msg = ''
    for i in range(len(f[0])):
        msg += sorted(Counter([line[i] for line in f]).items(), key=lambda item: item[1])[-1][0]
    return msg


def sol2(filename):
    f = get_input(filename)
    msg = ''
    for i in range(len(f[0])):
        msg += sorted(Counter([line[i] for line in f]).items(), key=lambda item: item[1])[0][0]
    return msg


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
