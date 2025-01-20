#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    grid = {}
    for i, line in enumerate(lines):
        for j, c in enumerate(line.strip()):
            grid[(i, j)] = c
    return grid


def adjacent_bugs(grid, p):
    tot = 0
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        q = (p[0] + d[0], p[1] + d[1])
        if q in grid.keys() and grid[q] == '#':
            tot += 1
    return tot


def advance(grid):
    new_grid = {}
    for p in grid.keys():
        if grid[p] == '#' and adjacent_bugs(grid, p) != 1:
            new_grid[p] = '.'
        elif grid[p] == '.' and adjacent_bugs(grid, p) in [1, 2]:
            new_grid[p] = '#'
        else:
            new_grid[p] = grid[p]
    return new_grid


def print_grid(grid):
    for i in range(5):
        for j in range(5):
            print(grid[(i, j)], end='')
        print()


def to_hash(grid):
    h = ()
    for i in range(5):
        for j in range(5):
            h += (grid[(i, j)],)
    return h


def biodiversity(grid_hash):
    b = 0
    for i in range(len(grid_hash)):
        if grid_hash[i] == '#':
            b += pow(2, i)
    return b


def sol1(filename):
    grid = get_input(filename)
    seen = set(to_hash(grid))
    while True:
        grid = advance(grid)
        h = to_hash(grid)
        if h in seen:
            break
        seen.add(h)
    return biodiversity(to_hash(grid))


def adjacent_bugs_2(grids, level, p):
    tot = 0
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        q = (p[0] + d[0], p[1] + d[1])
        if q in grids[level].keys() and q != (2, 2) and grids[level][q] == '#':
            tot += 1
    if p == (2, 1) and (level + 1) in grids.keys():
        for q in [(i, 0) for i in range(5)]:
            if grids[level + 1][q] == '#':
                tot += 1
    if p == (2, 3) and (level + 1) in grids.keys():
        for q in [(i, 4) for i in range(5)]:
            if grids[level + 1][q] == '#':
                tot += 1
    if p == (1, 2) and (level + 1) in grids.keys():
        for q in [(0, i) for i in range(5)]:
            if grids[level + 1][q] == '#':
                tot += 1
    if p == (3, 2) and (level + 1) in grids.keys():
        for q in [(4, i) for i in range(5)]:
            if grids[level + 1][q] == '#':
                tot += 1
    if p[1] == 0 and (level - 1) in grids.keys():
        if grids[level - 1][(2, 1)] == '#':
            tot += 1
    if p[1] == 4 and (level - 1) in grids.keys():
        if grids[level - 1][(2, 3)] == '#':
            tot += 1
    if p[0] == 0 and (level - 1) in grids.keys():
        if grids[level - 1][(1, 2)] == '#':
            tot += 1
    if p[0] == 4 and (level - 1) in grids.keys():
        if grids[level - 1][(3, 2)] == '#':
            tot += 1
    return tot


def build_new_grid():
    grid = {}
    for i in range(5):
        for j in range(5):
            grid[(i, j)] = '.'
    return grid


def advance_2(grids):
    sorted_levels = list(sorted(grids.keys()))
    if list(grids[sorted_levels[0]].values()).count('#') != 0:
        grids[sorted_levels[0] - 1] = build_new_grid()
    if list(grids[sorted_levels[-1]].values()).count('#') != 0:
        grids[sorted_levels[-1] + 1] = build_new_grid()
    new_grids = {}
    for level, grid in grids.items():
        new_grid = {}
        for p in [p for p in grid.keys() if p != (2, 2)]:
            if grid[p] == '#' and adjacent_bugs_2(grids, level, p) != 1:
                new_grid[p] = '.'
            elif grid[p] == '.' and adjacent_bugs_2(grids, level, p) in [1, 2]:
                new_grid[p] = '#'
            else:
                new_grid[p] = grid[p]
        new_grids[level] = new_grid
        new_grids[level][(2, 2)] = '.'
    return new_grids


def print_grids(grids):
    sorted_levels = list(sorted(grids.keys()))
    for level in sorted_levels:
        if list(grids[level].values()).count('#') != 0:
            print('Level', level)
            print_grid(grids[level])
            print()


def sol2(filename, steps):
    grid = get_input(filename)
    grids = {0: grid}
    for i in range(steps):
        grids = advance_2(grids)
    return sum(list(grid.values()).count('#') for grid in grids.values())


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt", 10)}')
    print(f'Solution: {sol2("input.txt", 200)}')
