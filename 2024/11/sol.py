#!/usr/bin/env python3

import functools
import time


def get_input(filename):
    f = open(filename, 'r')
    stones_list = [int(x) for x in f.read().strip().split()]
    f.close()
    stones = {}
    for st in stones_list:
        if st in stones.keys():
            stones[st] += 1
        else:
            stones[st] = 1
    return stones


@functools.cache
def children(st):
    if st == 0:
        return [1]
    l = len(str(st))
    if l % 2 == 0:
        return [int(str(st)[int(l / 2):]), int(str(st)[:int(l / 2)])]
    return [st * 2024]


def sol(filename, steps):
    stones = get_input(filename)
    for i in range(steps):
        new_stones = {}
        for st, v in stones.items():
            for ch in children(st):
                if ch in new_stones.keys():
                    new_stones[ch] += v
                else:
                    new_stones[ch] = v
        stones = new_stones.copy()
    return sum(stones.values())


def sol1(filename):
    return sol(filename, 25)


def sol2(filename):
    return sol(filename, 75)


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    end1 = time.time()
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    end2 = time.time()
    print(f'Part 1: {end1 - start:.3f}s, Part 2: {end2 - end1:.3f}s, Tot: {end2 - start:.3f}s')
