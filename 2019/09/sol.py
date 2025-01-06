#!/usr/bin/env python3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from intcode import Intcode

def get_input(filename):
    f = open(filename, 'r')
    memory = [int(x) for x in f.read().strip().split(',')]
    f.close()
    return memory


def sol1(filename, inputs):
    memory = get_input(filename)
    intcode = Intcode(memory, inputs)
    intcode.run()
    return intcode.output


def sol2(filename, inputs):
    memory = get_input(filename)
    intcode = Intcode(memory, inputs)
    intcode.run()
    return intcode.output


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", [])}')
    print(f'Solution: {sol1("input.txt", [1])}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt", [2])}')
