#!/usr/bin/env python3
import copy
import itertools
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from intcode import Intcode


def get_input(filename):
    f = open(filename, 'r')
    memory = [int(x) for x in f.read().strip().split(',')]
    f.close()
    return memory


def get_output(intcode):
    out = ''
    while len(intcode.output) > 0:
        c = intcode.output.pop(0)
        out += chr(c)
    return out


def add_input(intcode, instruction):
    for c in instruction:
        intcode.input.append(ord(c))
    intcode.input.append(ord('\n'))
    return intcode


# initial input found by exploring manually the game and collecting all items
initial_input = '''west
take whirled peas
east
south
west
take bowl of rice
north
south
east
east
take mutex
east
take astronaut ice cream
east
take ornament
east
west
west
south
take tambourine
north
west
south
east
take mug
east
west
west
south
east
west
west
south
take easter egg
west
'''

# objects found by exploring manually the game
objects = ['bowl of rice', 'easter egg', 'tambourine', 'astronaut ice cream', 'mug', 'mutex', 'whirled peas',
           'ornament']


def sol1(filename, mode):
    memory = get_input(filename)
    if mode == 'manual':
        intcode = Intcode(memory.copy(), [])
        while not intcode.halted:
            try:
                intcode.execute()
            except IndexError:
                print(get_output(intcode))
                user_input = input()
                intcode = add_input(intcode, user_input)
                continue
        print(get_output(intcode))
        return 0
    intcode = Intcode(memory.copy(), [])
    intcode = add_input(intcode, initial_input)
    while True:
        try:
            intcode.execute()
        except IndexError:
            break
    for r in range(len(objects) + 1):
        for comb in itertools.combinations(objects, r):
            checkpoint = copy.deepcopy(intcode)
            command = ''
            for obj in comb:
                command += f'drop {obj}\n'
            command += 'west\n'
            checkpoint = add_input(checkpoint, command)
            while True:
                if checkpoint.halted:
                    print(get_output(checkpoint))
                    return
                try:
                    checkpoint.execute()
                except IndexError:
                    if 'ejected' in get_output(checkpoint):
                        break


if __name__ == '__main__':
    print('--- Part 1 ---')
    sol1("input.txt", mode='auto')
