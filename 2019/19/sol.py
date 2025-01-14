#!/usr/bin/env python3
from cachetools import cached
from cachetools.keys import hashkey
import math
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from intcode import Intcode


def get_input(filename):
    f = open(filename, 'r')
    memory = [int(x) for x in f.read().strip().split(',')]
    f.close()
    return memory


def print_grid(grid):
    size = int(math.sqrt(len(grid)))
    for x in range(size):
        for y in range(size):
            print(grid[(x, y)], end='')
        print()


def sol1(filename):
    memory = get_input(filename)
    grid = {}
    for x in range(50):
        for y in range(50):
            inp = [x, y]
            intcode = Intcode(memory.copy(), inp)
            intcode.run()
            grid[(x, y)] = intcode.output[0]
    return list(grid.values()).count(1)


@cached(cache={}, key=lambda x, y, memory: hashkey((x, y)))
def get_value(x, y, memory):
    intcode = Intcode(memory.copy(), [x, y])
    intcode.run()
    return intcode.output[0]


def is_left_angle(x, y, memory, size):
    for i in range(size):
        for j in range(size):
            if get_value(x + i, y + j, memory) != 1:
                return False
    return True


def sol2(filename):
    memory = get_input(filename)
    d = 0
    min_x = 0
    while True:
        started = False
        for x in range(min_x, d):
            y = d - x
            if get_value(x, y, memory) != 1:
                if started:
                    break
                else:
                    continue
            if not started and x > min_x:
                min_x = x
            started = True
            if is_left_angle(x, y, memory,100):
                return 10000 * x + y
        d += 1


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
