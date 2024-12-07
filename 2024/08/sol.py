#!/usr/bin/env python3

import time

def get_input(filename):
    f = open(filename, 'r')
    f.close()
    return {}


def sol1(filename):
    _ = get_input(filename)
    return 0


def sol2(filename):
    _ = get_input(filename)
    return 0


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    # print(f'Solution: {sol1("input.txt")}')
    end1 = time.time()
    # print('--- Part 2 ---')
    # print(f'Test: {sol2("test.txt")}')
    # print(f'Solution: {sol2("input.txt")}')
    end2 = time.time()
    print(f'Part 1: {end1 - start:.3f}s, Part 2: {end2 - end1:.3f}s, Tot: {end2 - start:.3f}s')
