#!/usr/bin/env python3
import time


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


def print_grid(grid):
    a, b = max([p[0] for p in grid.keys()]), max([p[1] for p in grid.keys()])
    for i in range(a + 1):
        for j in range(b + 1):
            if grid[(i, j)] == '.':
                print('  ', end='')
            else:
                print('🧻', end='')
        print()


def print_grid_simple(grid):
    a, b = max([p[0] for p in grid.keys()]), max([p[1] for p in grid.keys()])
    for i in range(a + 1):
        for j in range(b + 1):
            if grid[(i, j)] == '.':
                print(' ', end='')
            else:
                print('@', end='')
        print()


def move_cursor(y, x):
    print("\033[%d;%dH" % (y, x))


def visualization(filename):
    grid = get_input(filename)
    print('\033[?25l', end="") # hide cursor
    step = 0
    should_exit = False
    tot = 0
    while True:
        move_cursor(0, 0)
        print(chr(27) + "[2J") # clear terminal
        print_grid_simple(grid)
        free = find_free(grid)
        if len(free) == 0:
            should_exit = True
        tot += len(free)
        for f in free:
            grid[f] = '.'
        step += 1
        print()
        print('--- Step ', step, '---')
        print('--- Removed rolls: ', len(free), '---')
        print('--- Total removed rolls: ', tot)
        if should_exit:
            break
        time.sleep(0.2)
    print('\033[?25h', end="")  # show cursor again


if __name__ == '__main__':
    visualization("input.txt")