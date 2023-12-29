#!/usr/bin/env python3
import time
from copy import deepcopy


def get_input(filename):
    f = open(filename, 'r').read()
    return f.split('\n')


def render(grid):
    for line in grid:
        print(' '.join(line).replace('.', ' '))


def sol1(filename, size_x, size_y):
    instructions = get_input(filename)
    grid = [['.'] * size_y for _ in range(size_x)]
    for instruction in instructions:
        if instruction.split()[0] == 'rect':
            a, b = [int(x) for x in instruction.split()[1].split('x')]
            for i in range(b):
                for j in range(a):
                    grid[i][j] = '#'
        else:
            if instruction.split()[1] == 'column':
                col = int(instruction.split()[2].split('=')[1])
                amount = int(instruction.split()[-1])
                new_grid = deepcopy(grid)
                for i in range(len(grid)):
                    new_grid[(i + amount) % len(grid)][col] = grid[i][col]
                grid = deepcopy(new_grid)
            if instruction.split()[1] == 'row':
                row = int(instruction.split()[2].split('=')[1])
                amount = int(instruction.split()[-1])
                new_grid = deepcopy(grid)
                for j in range(len(grid[0])):
                    new_grid[row][(j + amount) % len(grid[0])] = grid[row][j]
                grid = deepcopy(new_grid)
    res = 0
    for line in grid:
        res += line.count('#')
    render(grid)
    return res


def sol2(filename):
    _ = get_input(filename)
    return 0


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 3, 7)}')
    print(f'Solution: {sol1("input.txt", 6, 50)}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
