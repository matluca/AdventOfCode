#!/usr/bin/env python3

def get_input(filename):
    grid = {}
    f = open(filename, 'r')
    for i, line in enumerate(f.readlines()):
        for j, c in enumerate(line[:-1]):
            grid[(i, j)] = c
    f.close()
    return grid


def rotate(pos, dd, grid):
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if d[0] == -dd[0] and d[1] == -dd[1]:
            continue
        if (pos[0] + d[0], pos[1] + d[1]) in grid.keys() and grid[(pos[0] + d[0], pos[1] + d[1])] != ' ':
            return (pos[0] + d[0], pos[1] + d[1]), d
    return None, None


def move(pos, d, grid):
    if (pos[0] + d[0], pos[1] + d[1]) in grid.keys() and grid[(pos[0] + d[0], pos[1] + d[1])] != ' ':
        return (pos[0] + d[0], pos[1] + d[1]), d
    elif grid[pos] == '+':
        return rotate(pos, d, grid)
    return None, None


def sol1(filename):
    grid = get_input(filename)
    pos = [p for p in grid.keys() if grid[p] != ' '][0]
    d = (1, 0)
    path = ''
    while pos is not None:
        if 'A' <= grid[pos] <= 'Z':
            path += grid[pos]
        pos, d = move(pos, d, grid)
    return path


def sol2(filename):
    grid = get_input(filename)
    pos = [p for p in grid.keys() if grid[p] != ' '][0]
    d = (1, 0)
    steps = 0
    while pos is not None:
        steps += 1
        pos, d = move(pos, d, grid)
    return steps


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
