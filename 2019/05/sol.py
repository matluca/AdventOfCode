#!/usr/bin/env python3
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from intcode import run


def get_input(filename):
    f = open(filename, 'r')
    memory = [int(x) for x in f.read().strip().split(',')]
    f.close()
    return memory


def sol1(filename):
    program = get_input(filename)
    _, outputs = run(program, input_value=1)
    print(f'Tests: {outputs[:-1]}')
    return outputs[-1]


def sol2(filename):
    program = get_input(filename)
    _, outputs = run(program, input_value=5)
    print(f'Tests: {outputs[:-1]}')
    return outputs[-1]


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
