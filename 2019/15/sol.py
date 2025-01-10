#!/usr/bin/env python3
import sys
import os
import copy
from functools import cmp_to_key

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from intcode import Intcode


def get_input(filename):
    f = open(filename, 'r')
    memory = [int(x) for x in f.read().strip().split(',')]
    f.close()
    return memory


def cmp(a, b):
    if a[0] < b[0]:
        return -1
    if a[0] > b[0]:
        return 1
    return 0


def get_next_pos(current_pos, direction):
    if direction == 1:
        return current_pos[0] - 1, current_pos[1]
    if direction == 2:
        return current_pos[0] + 1, current_pos[1]
    if direction == 3:
        return current_pos[0], current_pos[1] - 1
    if direction == 4:
        return current_pos[0], current_pos[1] + 1
    return current_pos


def explore(intcode, mode):
    current_pos = (0, 0)
    visited = set(current_pos)
    walls = set()
    queue = [(0, current_pos, copy.deepcopy(intcode))]
    oxygen = None
    while True:
        if len(queue) == 0:
            return oxygen, walls
        queue.sort(key=cmp_to_key(cmp))
        current_distance, current_pos, current_intcode = queue.pop(0)
        for i in range(1, 5):
            next_pos = get_next_pos(current_pos, i)
            if next_pos in walls:
                continue
            pr = copy.deepcopy(current_intcode)
            pr.input = [i]
            while len(pr.output) == 0:
                pr.execute()
            out = pr.output.pop()
            if out == 2:
                oxygen = next_pos
                if mode == 'find_oxygen':
                    return current_distance + 1
            if out == 0:
                walls.add(next_pos)
                continue
            if next_pos not in visited:
                queue.append((current_distance + 1, next_pos, pr))
                visited.add(next_pos)


def sol1(filename):
    memory = get_input(filename)
    intcode = Intcode(memory)
    return explore(intcode, 'find_oxygen')


def sol2(filename):
    memory = get_input(filename)
    intcode = Intcode(memory)
    oxygen_pos, walls = explore(intcode, 'all')
    oxygen = {oxygen_pos}
    steps = 0
    while True:
        extra = set()
        for o in oxygen:
            for n in [get_next_pos(o, d) for d in range(1, 5)]:
                if n not in walls and n not in oxygen:
                    extra.add(n)
        if len(extra) == 0:
            return steps
        steps += 1
        oxygen |= extra


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
