#!/usr/bin/env python3
import math


def get_input(filename):
    f = open(filename, 'r')
    square = f.read().strip()
    f.close()
    return int(square)


def next_position(current):
    if current is None:
        return None
    x, y = current
    if 0 <= x == -y:
        return x + 1, y
    elif x > 0 and abs(y) < abs(x):
        return x, y + 1
    elif x == y > 0:
        return x - 1, y
    elif y > 0 and abs(x) < abs(y):
        return x - 1, y
    elif -x == y > 0:
        return x, y - 1
    elif x < 0 and abs(y) < abs(x):
        return x, y - 1
    elif x == y < 0:
        return x + 1, y
    elif y < 0 and abs(x) < abs(y):
        return x + 1, y
    return None


def sol1(filename):
    square = get_input(filename)
    pos = (0, 0)
    for i in range(1, square):
        pos = next_position(pos)
    return abs(pos[0]) + abs(pos[1])


def neighbours(pos):
    return [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1), (pos[0] - 1, pos[1] - 1), (pos[0] - 1, pos[1] + 1), (pos[0] + 1, pos[1] - 1), (pos[0] + 1, pos[1] + 1)]


def sol2(filename):
    inp = get_input(filename)
    pos = (0, 0)
    grid = {pos: 1}
    while True:
        pos = next_position(pos)
        grid[pos] = sum(grid[n] for n in neighbours(pos) if n in grid.keys())
        if grid[pos] > inp:
            return grid[pos]


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
