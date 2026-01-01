#!/usr/bin/env python3

def get_input(filename):
    grid = set()
    f = open(filename, 'r')
    size = 0
    for i, line in enumerate(f.readlines()):
        size += 1
        for j, c in enumerate(line.strip()):
            if c == '#':
                grid.add((i, j))
    f.close()
    return grid, size


def turn_right(d):
    if d == (-1, 0):
        return 0, 1
    if d == (0, 1):
        return 1, 0
    if d == (1, 0):
        return 0, -1
    return -1, 0


def turn_left(d):
    dd = turn_right(d)
    return -dd[0], -dd[1]


def sol1(filename, steps):
    grid, size = get_input(filename)
    pos = (size // 2, size // 2)
    d = (-1, 0)
    bursts = 0
    for i in range(steps):
        if pos in grid:
            d = turn_right(d)
            grid.remove(pos)
        else:
            d = turn_left(d)
            grid.add(pos)
            bursts += 1
        pos = (pos[0] + d[0], pos[1] + d[1])
    return bursts


def sol2(filename, steps):
    grid_old, size = get_input(filename)
    pos = (size // 2, size // 2)
    grid = {}
    for node in grid_old:
        grid[node] = 'I'
    d = (-1, 0)
    bursts = 0
    for i in range(steps):
        if pos not in grid.keys():
            d = turn_left(d)
            grid[pos] = 'W'
        elif grid[pos] == 'W':
            bursts += 1
            grid[pos] = 'I'
        elif grid[pos] == 'I':
            d = turn_right(d)
            grid[pos] = 'F'
        else:
            d = (-d[0], -d[1])
            del grid[pos]
        pos = (pos[0] + d[0], pos[1] + d[1])
    return bursts


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 10000)}')
    print(f'Solution: {sol1("input.txt", 10000)}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt", 10000000)}')
    print(f'Solution: {sol2("input.txt", 10000000)}')
