#!/usr/bin/env python3
import numpy as np


def get_input(filename):
    f = open(filename, 'r')
    grid = []
    for line in f:
        grid.append(line.strip())
    f.close()
    source = (0, 0)
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == 'S':
                source = (i, j)
    return grid, source


def get_next(grid, plots):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    next_plots = set()
    for plot in plots:
        for direction in directions:
            p = (plot[0] + direction[0], plot[1] + direction[1])
            if 0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0]) and grid[p[0]][p[1]] != '#':
                next_plots.add(p)
    return next_plots


def get_next_2(grid, plots):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    next_plots = set()
    for plot in plots:
        for direction in directions:
            p = (plot[0] + direction[0], plot[1] + direction[1])
            if grid[p[0] % len(grid)][p[1] % len(grid[0])] != '#':
                next_plots.add(p)
    return next_plots


def sol1(filename, steps):
    grid, source = get_input(filename)
    plots = {source}
    for _ in range(steps):
        plots = get_next(grid, plots)
    return len(plots)


def sol2(filename, target, seq_length):
    grid, source = get_input(filename)
    plots = {source}
    x, y = [], []
    steps = 0
    while len(x) < seq_length:
        steps += 1
        plots = get_next_2(grid, plots)
        if steps % len(grid) == target % len(grid):
            x.append(steps)
            y.append(len(plots))
    pol = np.polyfit(x[-3:], y[-3:], 2)
    return target, round(np.poly1d(pol)(target))


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 6)}')
    print(f'Solution: {sol1("input.txt", 64)}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt", 100, 8)}')
    print(f'Test: {sol2("test.txt", 500, 8)}')
    print(f'Test: {sol2("test.txt", 1000, 8)}')
    print(f'Test: {sol2("test.txt", 5000, 8)}')
    print(f'Solution: {sol2("input.txt", 26501365, 3)}')
