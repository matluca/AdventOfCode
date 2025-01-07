#!/usr/bin/env python3
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
    max_x = max([p[0] for p in grid.keys()])
    max_y = max([p[1] for p in grid.keys()])
    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if (x, y) == (-1, 0):
                continue
            if (x, y) not in grid.keys() or grid[(x, y)] == 0:
                print('  ', end='')
            elif grid[(x, y)] == 1:
                print(chr(0x1F9F1), end='')
            elif grid[(x, y)] == 2:
                print(chr(0x1F4E6), end='')
            elif grid[(x, y)] == 3:
                print(chr(0x1F3D3), end='')
            elif grid[(x, y)] == 4:
                print(chr(0x26BD), end='')
        print()
    print()


def sol1(filename):
    memory = get_input(filename)
    grid = {}
    intcode = Intcode(memory)
    while True:
        while len(intcode.output) < 3:
            intcode.execute()
            if intcode.halted:
                break
        if intcode.halted:
            break
        x, y, tile = intcode.output[0], intcode.output[1], intcode.output[2]
        intcode.output = []
        grid[(x, y)] = tile
    tot = 0
    for k, v in grid.items():
        if v == 2:
            tot += 1
    return tot


def find_ball(grid):
    if 4 in grid.values():
        return [p for p, v in grid.items() if v == 4][0]

def find_paddle(grid):
    if 3 in grid.values():
        return [p for p, v in grid.items() if v == 3][0]


def move_paddle(grid):
    ball = find_ball(grid)
    paddle = find_paddle(grid)
    if paddle[0] < ball[0]:
        return 1
    if paddle[0] > ball[0]:
        return -1
    return 0


def sol2(filename):
    score = -1
    memory = get_input(filename)
    memory[0] = 2
    grid = {}
    intcode = Intcode(memory)
    while True:
        while len(intcode.output) < 3:
            if intcode.program[intcode.pointer] % 100 == 3:
                intcode.input = [move_paddle(grid)]
            intcode.execute()
            if intcode.halted:
                break
        if intcode.halted:
            break
        x, y, tile = intcode.output[0], intcode.output[1], intcode.output[2]
        if (x, y) == (-1, 0):
            score = tile
        intcode.output = []
        grid[(x, y)] = tile
    return score


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
