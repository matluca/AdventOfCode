#!/usr/bin/env python3

def get_input(filename):
    rules = {}
    f = open(filename, 'r')
    for line in f.readlines():
        rules[line.split(' => ')[0]] = line.strip().split(' => ')[1]
    f.close()
    return rules


def print_grid(grid):
    for line in grid:
        print(line)


def subgrid(grid, x, y, size):
    sub = []
    for j in range(size):
        sub.append(grid[x + j][y: y + size])
    return sub


def patterns(grid):
    p = ['/'.join(grid), '/'.join([line[::-1] for line in grid])]
    size = len(grid)
    rot_grid = [''.join([grid[j][i] for j in range(size)]) for i in range(size)]
    p.append('/'.join(rot_grid))
    p.append('/'.join([line[::-1] for line in rot_grid]))
    flip_grid = grid[::-1]
    p.append('/'.join(flip_grid))
    p.append('/'.join([line[::-1] for line in flip_grid]))
    last_grid = [line[::-1] for line in flip_grid]
    last_rot = [''.join([last_grid[j][i] for j in range(size)]) for i in range(size)]
    p.append('/'.join(last_rot))
    p.append('/'.join([line[::-1] for line in last_rot]))
    return p


def extend(grid, rules):
    new_grid = []
    if len(grid) % 2 == 0:
        for i in range(len(grid) // 2):
            for j in range(len(grid) // 2):
                subg = subgrid(grid, i * 2, j * 2, 2)
                for pattern in patterns(subg):
                    if pattern in rules.keys():
                        ext = rules[pattern]
                        new_grid += ext.split('/')
                        break
        collapsed_grid = []
        for b in range(len(grid) // 2):
            for i in range(3):
                line = ''
                for j in range(len(grid) // 2):
                    line += new_grid[i + 3 * len(grid) // 2 * b + 3 * j]
                collapsed_grid.append(line)
        return collapsed_grid
    elif len(grid) % 3 == 0:
        for i in range(len(grid) // 3):
            for j in range(len(grid) // 3):
                subg = subgrid(grid, i * 3, j * 3, 3)
                for pattern in patterns(subg):
                    if pattern in rules.keys():
                        ext = rules[pattern]
                        new_grid += ext.split('/')
                        break
        collapsed_grid = []
        for b in range(len(grid) // 3):
            for i in range(4):
                line = ''
                for j in range(len(grid) // 3):
                    line += new_grid[i + 4 * len(grid) // 3 * b + 4 * j]
                collapsed_grid.append(line)
        return collapsed_grid
    return new_grid


def sol1(filename, steps):
    rules = get_input(filename)
    grid = ['.#.', '..#', '###']
    for _ in range(steps):
        grid = extend(grid, rules)
    return sum([sum([c == '#' for c in line]) for line in grid])


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 2)}')
    print(f'Solution: {sol1("input.txt", 5)}')
    print('--- Part 2 ---')
    print(f'Solution: {sol1("input.txt", 18)}')
