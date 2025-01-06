#!/usr/bin/env python3
import itertools
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


def amplify(program, phases, second_input):
    second_inp = second_input
    for i in range(5):
        intcode = Intcode(program.copy(), [phases[i], second_inp])
        intcode.run()
        second_inp = intcode.output[0]
    return second_inp


def sol1(filename):
    program = get_input(filename)
    phase_settings = [0, 1, 2, 3, 4]
    max_signal = 0
    for perm in itertools.permutations(phase_settings):
        amp = amplify(program.copy(), perm, 0)
        if amp > max_signal:
            max_signal = amp
    return max_signal


def sol2(filename):
    program = get_input(filename)
    phase_settings = [9, 8, 7, 6, 5]
    max_signal = 0
    for perm in itertools.permutations(phase_settings):
        ampl = []
        for i in range(5):
            ampl.append(Intcode(program.copy(), [perm[i]]))
        ampl[0].input.append(0)
        i = 0
        last_output = 0
        while True:
            ampl[i].execute()
            if ampl[i].halted:
                break
            if len(ampl[i].output) > 0:
                if i == 4:
                    last_output = ampl[i].output[0]
                ampl[(i + 1) % 5].input.append(ampl[i].output.pop(0))
                i = (i + 1) % 5
        if last_output > max_signal:
            max_signal = last_output
    return max_signal


if __name__ == '__main__':
    start_time = time.time()
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
    end1_time = time.time()
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    end2_time = time.time()
    print(
        f'Part 1: {end1_time - start_time:.3f}s, Part 2: {end2_time - end1_time:.3f}s, Tot: {end2_time - start_time:.3f}s')
