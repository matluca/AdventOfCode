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


def sol1(filename):
    memory = get_input(filename)
    intcode = []
    for i in range(50):
        intcode.append(Intcode(memory.copy(), [i]))
    while True:
        for i in range(50):
            try:
                intcode[i].execute()
            except IndexError:
                intcode[i].input = [-1]
            if len(intcode[i].output) == 3:
                a, x, y = intcode[i].output.pop(0), intcode[i].output.pop(0), intcode[i].output.pop(0)
                if a == 255:
                    return y
                intcode[a].input.append(x)
                intcode[a].input.append(y)
                break


def are_all_idle(is_idle):
    for i in range(50):
        if not is_idle[i]:
            return False
    return True


def sol2(filename):
    memory = get_input(filename)
    intcode = []
    is_idle = []
    for i in range(50):
        intcode.append(Intcode(memory.copy(), [i]))
        is_idle.append(False)
    nat_packet = []
    last_nat_packet = [-1, -1]
    while True:
        for i in range(50):
            try:
                intcode[i].execute()
            except IndexError:
                if i == 0 and are_all_idle(is_idle):
                    intcode[0].input = nat_packet.copy()
                    if nat_packet == last_nat_packet:
                        return nat_packet[1]
                    last_nat_packet = nat_packet.copy()
                    is_idle[0] = False
                else:
                    intcode[i].input = [-1]
                    is_idle[i] = True
            if len(intcode[i].output) == 3:
                a, x, y = intcode[i].output.pop(0), intcode[i].output.pop(0), intcode[i].output.pop(0)
                if a == 255:
                    nat_packet = [x, y]
                else:
                    intcode[a].input.append(x)
                    intcode[a].input.append(y)
                    is_idle[a] = False
                    break


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
