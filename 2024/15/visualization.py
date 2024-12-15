#!/usr/bin/env python3

import time
from sol import get_input, next_grid, next_grid_2, enlarge_grid
import os, re, sys, termios, tty

part = int(sys.argv[1])
filename = sys.argv[2]


def move_cursor(y, x):
    print("\033[%d;%dH" % (y, x))


def print_grid_nice(grid):
    print('\033[?25l', end="")  # hide cursor
    size_x = max(p[0] for p in grid.keys())
    size_y = max(p[1] for p in grid.keys())
    for i in range(size_x + 1):
        print(' ', end='')
        for j in range(size_y + 1):
            c = grid[(i, j)]
            if c == '.':
                print('  ', end='')
            elif c == '@':
                print(chr(0x1F916), end='')
            elif c == '#':
                print(chr(0x1F9F1), end='')
            else:
                print(chr(0x1F4E6), end='')
        print()


def visualize(next_function):
    print('\033[?25l', end="")  # hide cursor
    grid, moves = get_input(filename)
    if part == 2:
        grid = enlarge_grid(grid)
    os.system('clear')
    start = time.time()
    for step in range(len(moves)):
        move = moves[step]
        grid = next_function(grid, move)
        if step % 2 == 0:
            move_cursor(0, 0)
            print_grid_nice(grid)
            print()
            print(f'Step {step}/{len(moves)}: {step / len(moves) * 100:.1f}%')
    end = time.time()
    print('\033[?25h', end="")  # show cursor again


if __name__ == '__main__':
    if part == 1:
        visualize(next_grid)
    else:
        visualize(next_grid_2)
