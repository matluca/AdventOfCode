#!/usr/bin/env python3

def get_input(filename):
    grid = {}
    f = open(filename, 'r')
    for line in f.readlines():
        if line[0] == 'x':
            r = [int(x) for x in line.split('=')[2].split('..')]
            for i in range(r[0], r[1] + 1):
                grid[(i, int(line.split('=')[1].split(',')[0]))] = '#'
        else:
            r = [int(x) for x in line.split('=')[2].split('..')]
            for j in range(r[0], r[1] + 1):
                grid[(int(line.split('=')[1].split(',')[0]), j)] = '#'
    f.close()
    return grid


def print_grid(grid):
    for i in range(0, max(p[0] for p in grid.keys()) + 2):
        for j in range(min(p[1] for p in grid.keys()) - 1, max(p[1] for p in grid.keys()) + 2):
            c = '.'
            if (i, j) in grid.keys():
                c = grid[(i, j)]
            print(c, end='')
        print()


def flow(grid, p, limit):
    while p[0] + 1 <= limit and (p[0] + 1, p[1]) not in grid.keys():
        grid[p] = '|'
        p = p[0] + 1, p[1]
    if p[0] + 1 > limit:
        return grid
    if grid[(p[0] + 1, p[1])] in ["#", "~"]:
        return spread(grid, p, limit)
    grid[p] = '|'
    return grid


def spread(grid, p, limit):
    while True:
        row = {p}
        q = p
        n_walls = 0
        while True:
            q = q[0], q[1] - 1
            if q in grid.keys() and grid[q] == '#':
                n_walls = n_walls + 1
                break
            row.add(q)
            b = q[0] + 1, q[1]
            if b not in grid or grid[b] == '|':
                grid = flow(grid, q, limit)
                break
        q = p
        while True:
            q = q[0], q[1] + 1
            if q in grid.keys() and grid[q] == '#':
                n_walls = n_walls + 1
                break
            row.add(q)
            b = q[0] + 1, q[1]
            if b not in grid or grid[b] == '|':
                grid = flow(grid, q, limit)
                break
        fill = '~'
        if n_walls < 2:
            fill = '|'
        for q in row:
            if q not in grid.keys() or grid[q] != '~':
                grid[q] = fill
        if n_walls < 2:
            return grid
        if n_walls == 2:
            p = (p[0] - 1, p[1])


def sol1(filename):
    grid = get_input(filename)
    min_y = min(p[0] for p in grid)
    max_y = max(p[0] for p in grid)
    limit = max_y + 1
    grid = flow(grid, (0, 500), limit)
    return sum(1 for p, v in grid.items() if v in ['|', '~'] and min_y <= p[0] <= max_y)


def sol2(filename):
    grid = get_input(filename)
    min_y = min(p[0] for p in grid)
    max_y = max(p[0] for p in grid)
    limit = max_y + 1
    grid = flow(grid, (0, 500), limit)
    return sum(1 for p, v in grid.items() if v == '~' and min_y <= p[0] <= max_y)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
