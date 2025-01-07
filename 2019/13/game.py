#!/usr/bin/env python3
import sys
import os
import time
import readchar

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from intcode import Intcode

from sol import get_input, print_grid, find_ball, find_paddle, move_paddle


def next_character(mode, grid):
    if mode == 'manual':
        print("Waiting for input")
        c = readchar.readkey()
        if c == 'a':
            return -1
        elif c == 's':
            return 0
        elif c == 'd':
            return 1
    if mode == 'auto':
        return move_paddle(grid)


def game(filename, mode):
    print("\033[%d;%dH" % (0, 0))
    score = -1
    memory = get_input(filename)
    memory[0] = 2
    grid = {}
    intcode = Intcode(memory)
    finished_setup = False
    while True:
        while len(intcode.output) < 3:
            if intcode.program[intcode.pointer] % 100 == 3:
                finished_setup = True
                intcode.input = [next_character(mode, grid)]
            intcode.execute()
            if intcode.halted:
                break
        if intcode.halted:
            break
        x, y, tile = intcode.output[0], intcode.output[1], intcode.output[2]
        if (x, y) == (-1, 0):
            score = tile
        intcode.output = []
        grid[(x, y)] = tile
        if finished_setup and mode == 'auto':
            time.sleep(0.01)
        print("\033[%d;%dH" % (0, 0))
        print_grid(grid)
        if score > -1:
            print(f'Score: {score}')


if __name__ == '__main__':
    game("input.txt", 'auto')
