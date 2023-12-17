#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    grid = {}
    for i, line in enumerate(f):
        for j, c in enumerate(line.strip()):
            grid[(i, j)] = c
    f.close()
    return grid


def apply_step(grid):
    new_grid = {}
    for p, v in grid.items():
        neighbours_on = 0
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                q = (p[0] + x, p[1] + y)
                if q not in grid or q == p:
                    continue
                if grid[q] == '#':
                    neighbours_on += 1
        if v == '#':
            new_grid[p] = '#' if neighbours_on in [2, 3] else '.'
        if v == '.':
            new_grid[p] = '#' if neighbours_on == 3 else '.'
    return new_grid


def sol1(filename, steps):
    grid = get_input(filename)
    for _ in range(steps):
        grid = apply_step(grid)
    return sum(v == '#' for v in grid.values())


def add_corners(grid):
    size_x, size_y = max([p[0] for p in grid.keys()]), max([p[1] for p in grid.keys()])
    corners = [(0, 0), (size_x, 0), (0, size_y), (size_x, size_y)]
    for p in corners:
        grid[p] = '#'
    return grid


def sol2(filename, steps):
    grid = get_input(filename)
    grid = add_corners(grid)
    for _ in range(steps):
        grid = apply_step(grid)
        grid = add_corners(grid)
    return sum(v == '#' for v in grid.values())


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 4)}')
    print(f'Solution: {sol1("input.txt", 100)}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt", 5)}')
    print(f'Solution: {sol2("input.txt", 100)}')
