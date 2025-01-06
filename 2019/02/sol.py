#!/usr/bin/env python3
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from intcode import Intcode



def get_input(filename):
    f = open(filename, 'r')
    memory = [int(x) for x in f.read().strip().split(',')]
    f.close()
    return memory


def sol1(filename):
    memory = get_input(filename)
    memory[1] = 12
    memory[2] = 2
    program = Intcode(memory)
    program.run()
    return program.program[0]


def sol2(filename):
    memory = get_input(filename)
    for noun in range(100):
        for verb in range(100):
            inp = memory.copy()
            inp[1] = noun
            inp[2] = verb
            program = Intcode(inp)
            program.run()
            if program.program[0] == 19690720:
                return 100 * noun + verb
    return 0


if __name__ == '__main__':
    start_time = time.time()
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
    end1_time = time.time()
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
    end2_time = time.time()
    print(
        f'Part 1: {end1_time - start_time:.3f}s, Part 2: {end2_time - end1_time:.3f}s, Tot: {end2_time - start_time:.3f}s')
