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


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def paint(memory, initial):
    intcode = Intcode(memory, [])
    grid = {}
    pos = (0, 0)
    grid[pos] = initial
    direction = 0
    while True:
        if pos not in grid.keys() or grid[pos] == '.':
            inp = 0
        else:
            inp = 1
        intcode.input.append(inp)
        while len(intcode.output) < 2 and not intcode.halted:
            intcode.execute()
        if intcode.halted:
            break
        col, move = intcode.output.pop(0), intcode.output.pop(0)
        if col == 0:
            grid[pos] = "."
        if col == 1:
            grid[pos] = '#'
        if move == 0:
            direction = (direction - 1) % 4
        if move == 1:
            direction = (direction + 1) % 4
        pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
    return grid


def sol1(filename):
    memory = get_input(filename)
    grid = paint(memory, ".")
    return len(grid)


def print_grid(grid):
    min_x = min([p[0] for p in grid.keys()])
    max_x = max([p[0] for p in grid.keys()])
    min_y = min([p[1] for p in grid.keys()])
    max_y = max([p[1] for p in grid.keys()])
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) not in grid.keys() or grid[(x, y)] == '.':
                print(' ', end='')
            else:
                print('#', end='')
        print()


def sol2(filename):
    memory = get_input(filename)
    grid = paint(memory, "#")
    print_grid(grid)
    return


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution:')
    sol2("input.txt")
