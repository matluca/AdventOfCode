#!/usr/bin/env python3


import time


direction = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}


def get_input(filename):
    f = open(filename, 'r')
    grid_raw, moves_raw = f.read().strip().split('\n\n')
    f.close()
    grid = {}
    grid_lines = grid_raw.split('\n')
    for i in range(len(grid_lines)):
        for j in range(len(grid_lines[i])):
            grid[(i, j)] = grid_lines[i][j]
    moves = []
    for c in moves_raw:
        if c != '\n':
            moves.append(c)
    return grid, moves


def print_grid(grid):
    size_x = max(p[0] for p in grid.keys())
    size_y = max(p[1] for p in grid.keys())
    for i in range(size_x + 1):
        for j in range(size_y + 1):
            print(grid[(i, j)], end='')
        print()


def next_position(p, d):
    return p[0] + d[0], p[1] + d[1]


def previous_position(p, d):
    return p[0] - d[0], p[1] - d[1]


def can_move(p, d, repl, grid):
    n = next_position(p, d)
    if grid[n] == '#':
        return False, grid
    if grid[n] == '.':
        grid[n] = grid[p]
        grid[p] = repl
        return True, grid
    if grid[n] == 'O':
        did_move, grid = can_move(n, d, grid[previous_position(p, d)], grid)
        if did_move:
            grid[n] = grid[p]
            grid[p] = repl
            return True, grid
        return False, grid


def next_grid(grid, move):
    d = direction[move]
    robot = [p for p in grid.keys() if grid[p] == '@'][0]
    _, grid = can_move(robot, d, '.', grid)
    return grid


def sol1(filename):
    grid, moves = get_input(filename)
    for move in moves:
        grid = next_grid(grid, move)
    tot = 0
    for box in [p for p in grid.keys() if grid[p] == 'O']:
        tot += 100 * box[0] + box[1]
    return tot


def can_move_2(p, d, grid):
    n = next_position(p, d)
    if grid[n] == '#':
        return False
    if grid[n] == '.':
        return True
    if d in [(0, -1), (0, 1)]:
        return can_move_2(n, d, grid)
    if grid[n] == '[':
        return can_move_2(n, d, grid) and can_move_2((n[0], n[1] + 1), d, grid)
    if grid[n] == ']':
        return can_move_2(n, d, grid) and can_move_2((n[0], n[1] - 1), d, grid)


def move_2(p, d, repl, grid):
    n = next_position(p, d)
    if grid[n] == '.':
        grid[n] = grid[p]
        grid[p] = repl
        return grid
    if d in [(0, -1), (0, 1)]:
        grid = move_2(n, d, grid[previous_position(p, d)], grid)
        grid[n] = grid[p]
        grid[p] = repl
        return grid
    if grid[n] == '[':
        grid = move_2(n, d, grid[previous_position(p, d)], grid)
        grid = move_2((n[0], n[1] + 1), d, '.', grid)
        grid[n] = grid[p]
        grid[p] = repl
        return grid
    if grid[n] == ']':
        grid = move_2(n, d, grid[previous_position(p, d)], grid)
        grid = move_2((n[0], n[1] - 1), d, '.', grid)
        grid[n] = grid[p]
        grid[p] = repl
        return grid


def next_grid_2(grid, move):
    d = direction[move]
    robot = [p for p in grid.keys() if grid[p] == '@'][0]
    if can_move_2(robot, d, grid):
        grid = move_2(robot, d, '.', grid)
    return grid


def sol2(filename):
    old_grid, moves = get_input(filename)
    grid = {}
    for p in old_grid.keys():
        x, y = p
        if old_grid[p] == '#':
            grid[(x, 2 * y)] = '#'
            grid[(x, 2 * y + 1)] = '#'
        elif old_grid[p] == 'O':
            grid[(x, 2 * y)] = '['
            grid[(x, 2 * y + 1)] = ']'
        elif old_grid[p] == '.':
            grid[(x, 2 * y)] = '.'
            grid[(x, 2 * y + 1)] = '.'
        elif old_grid[p] == '@':
            grid[(x, 2 * y)] = '@'
            grid[(x, 2 * y + 1)] = '.'
    for move in moves:
        grid = next_grid_2(grid, move)
    tot = 0
    for box in [p for p in grid.keys() if grid[p] == '[']:
        tot += 100 * box[0] + box[1]
    return tot


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test 1: {sol1("test1.txt")}')
    print(f'Test 2: {sol1("test2.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    end1 = time.time()
    print('--- Part 2 ---')
    print(f'Test 1: {sol2("test1.txt")}')
    print(f'Test 2: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    end2 = time.time()
    print(f'Part 1: {end1 - start:.3f}s, Part 2: {end2 - end1:.3f}s, Tot: {end2 - start:.3f}s')
