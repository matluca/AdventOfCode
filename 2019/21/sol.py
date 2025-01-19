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


def display_output(intcode):
    for c in intcode.output:
        if c < 0x110000:
            print(chr(c), end='')


def build_input(raw):
    return [ord(c) for c in raw]


def sol1(filename):
    memory = get_input(filename)
    intcode = Intcode(memory)
    intcode.input = build_input('NOT B T\nNOT C J\nOR T J\nNOT A T\nOR T J\nAND D J\nWALK\n')
    intcode.run()
    display_output(intcode)
    return intcode.output[-1]


def sol2(filename):
    memory = get_input(filename)
    intcode = Intcode(memory)
    intcode.input = build_input('NOT B T\nNOT C J\nOR T J\nNOT A T\nOR T J\nAND D J\nNOT H T\nAND A T\nAND B T\nAND F T\nNOT T T\nAND T J\nRUN\n')
    intcode.run()
    display_output(intcode)
    return intcode.output[-1]


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')