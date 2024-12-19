#!/usr/bin/env python3
import functools
import time


def get_input(filename):
    f = open(filename, 'r')
    towels, patterns = f.read().strip().split('\n\n')
    f.close()
    return towels.split(', '), patterns.split('\n')


@functools.cache
def possible(pattern, towels):
    for towel in towels:
        if len(pattern) < len(towel):
            continue
        if pattern == towel:
            return True
        if pattern.startswith(towel):
            if possible(pattern[len(towel):], towels):
                return True
    return False


def sol1(filename):
    towels, patterns = get_input(filename)
    tot = 0
    for pattern in patterns:
        if possible(pattern, tuple(towels)):
            tot += 1
    return tot


@functools.cache
def possible_ways(pattern, towels):
    tot = 0
    for towel in towels:
        if len(pattern) < len(towel):
            continue
        if pattern == towel:
            tot += 1
        if pattern.startswith(towel):
            tot += possible_ways(pattern[len(towel):], towels)
    return tot


def sol2(filename):
    towels, patterns = get_input(filename)
    tot = 0
    for pattern in patterns:
        tot += possible_ways(pattern, tuple(towels))
    return tot


if __name__ == '__main__':
    start_time = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    end1_time = time.time()
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    end2_time = time.time()
    print(
        f'Part 1: {end1_time - start_time:.3f}s, Part 2: {end2_time - end1_time:.3f}s, Tot: {end2_time - start_time:.3f}s')
