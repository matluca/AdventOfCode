#!/usr/bin/env python3
import hashlib


def get_input(filename):
    f = open(filename, 'r')
    grid = []
    for line in f:
        grid.append(list(line.strip()))
    return grid


def move_north(grid):
    while True:
        new_grid = grid.copy()
        moves = 0
        for i in range(1, len(grid)):
            for j, c in enumerate(grid[i]):
                if c == 'O' and grid[i - 1][j] == '.':
                    new_grid[i - 1][j] = 'O'
                    new_grid[i][j] = '.'
                    moves += 1
        grid = new_grid.copy()
        if moves == 0:
            break
    return grid


def move_east(grid):
    while True:
        new_grid = grid.copy()
        moves = 0
        for i in range(len(grid)):
            for j, c in enumerate(grid[i][:-1]):
                if c == 'O' and grid[i][j + 1] == '.':
                    new_grid[i][j + 1] = 'O'
                    new_grid[i][j] = '.'
                    moves += 1
        grid = new_grid.copy()
        if moves == 0:
            break
    return grid


def move_south(grid):
    while True:
        new_grid = grid.copy()
        moves = 0
        for i in range(len(grid) - 1):
            for j, c in enumerate(grid[i]):
                if c == 'O' and grid[i + 1][j] == '.':
                    new_grid[i + 1][j] = 'O'
                    new_grid[i][j] = '.'
                    moves += 1
        grid = new_grid.copy()
        if moves == 0:
            break
    return grid


def move_west(grid):
    while True:
        new_grid = grid.copy()
        moves = 0
        for i in range(len(grid)):
            for j in range(1, len(grid[i])):
                c = grid[i][j]
                if c == 'O' and grid[i][j - 1] == '.':
                    new_grid[i][j - 1] = 'O'
                    new_grid[i][j] = '.'
                    moves += 1
        grid = new_grid.copy()
        if moves == 0:
            break
    return grid


def load(grid):
    res = 0
    for i, line in enumerate(grid):
        res += (len(grid) - i) * line.count('O')
    return res


def sol1(filename):
    grid = get_input(filename)
    grid = move_north(grid)
    return load(grid)


def get_hash(grid):
    one_liner = ''.join([''.join(line) for line in grid])
    return hashlib.sha1(one_liner.encode("utf-8")).hexdigest()[:20]


def sol2(filename):
    cache = {}
    results = []
    grid = get_input(filename)
    i = 0
    while True:
        grid = move_north(grid)
        grid = move_west(grid)
        grid = move_south(grid)
        grid = move_east(grid)
        key = get_hash(grid)
        if key in cache.keys():
            first = cache[key][1]
            diff = i - first
            return results[(1000000000 - first - 1) % diff + first]
        cache[key] = (load(grid), i)
        results.append(load(grid))
        i += 1


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
