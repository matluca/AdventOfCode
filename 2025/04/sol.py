#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    grid = {}
    i = 0
    for line in f.readlines():
        for j in range(len(line.strip())):
            grid[(i, j)] = line[j]
        i += 1
    f.close()
    return grid


def neighbours(grid, p):
    tot = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            q = (p[0] + i, p[1] + j)
            if q in grid.keys() and q != p and grid[q] == '@':
                tot += 1
    return tot


def find_free(grid):
    free = set()
    for p in grid.keys():
        if grid[p] == '@' and neighbours(grid, p) < 4:
            free.add(p)
    return free


def sol1(filename):
    grid = get_input(filename)
    return len(find_free(grid))


def sol2(filename):
    grid = get_input(filename)
    tot = 0
    while True:
        free = find_free(grid)
        if len(free) == 0:
            break
        tot += len(free)
        for f in free:
            grid[f] = '.'
    return tot


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
