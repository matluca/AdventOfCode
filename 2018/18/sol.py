#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    grid = {}
    i = 0
    for line in f.readlines():
        for j, c in enumerate(line.strip()):
            grid[(i, j)] = c
        i = i + 1
    f.close()
    return grid


def print_grid(grid):
    for i in range(0, max([p[0] for p in grid.keys()]) + 1):
        for j in range(0, max([p[1] for p in grid.keys()]) + 1):
            print(grid[(i, j)], end = '')
        print()


def n_neigh(grid, p, v):
    x, y = p
    tot = 0
    for q in [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]:
        if q in grid.keys() and grid[q] == v:
            tot = tot + 1
    return tot


def next_grid(grid):
    new_grid = {}
    for p, v in grid.items():
        new_grid[p] = grid[p]
        if v == '.':
            if n_neigh(grid, p, '|') >= 3:
                new_grid[p] = '|'
        elif v == '|':
            if n_neigh(grid, p, '#') >= 3:
                new_grid[p] = '#'
        elif v == '#':
            if not (n_neigh(grid, p, '#') >= 1 and n_neigh(grid, p, '|') >= 1):
                new_grid[p] = '.'
    return new_grid


def sol1(filename):
    grid = get_input(filename)
    for m in range(10):
        grid = next_grid(grid)
    n_w = sum([v == '|' for v in grid.values()])
    n_l = sum([v == '#' for v in grid.values()])
    return n_w * n_l


def to_key(grid):
    k = ''
    for i in range(0, max([p[0] for p in grid.keys()]) + 1):
        for j in range(0, max([p[1] for p in grid.keys()]) + 1):
            k = k + grid[(i, j)]
    return k


def sol2(filename):
    grid = get_input(filename)
    seen = {}
    values = {}
    m = 1
    while True:
        grid = next_grid(grid)
        n_w = sum([v == '|' for v in grid.values()])
        n_l = sum([v == '#' for v in grid.values()])
        key = to_key(grid)
        values[m] = n_w * n_l
        if key in seen.values():
            a = [m for m in seen.keys() if seen[m] == key][0]
            break
        seen[m] = key
        m = m + 1
    modulus = (1000000000 - a) % (m - a)
    return values[a + modulus]


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
