#!/usr/bin/env python3

import time
import regex


def get_input(filename):
    f = open(filename, 'r')
    systems = []
    systems_raw = f.read().strip().split('\n\n')
    f.close()
    for system_raw in systems_raw:
        reg = 'Button A: X\+(?P<a>\d+), Y\+(?P<b>\d+)\nButton B: X\+(?P<c>\d+), Y\+(?P<d>\d+)\nPrize: X=(?P<e>\d+), Y=(?P<f>\d+)'
        m = regex.search(reg, system_raw)
        systems.append(
            [int(m.group('a')), int(m.group('b')), int(m.group('c')), int(m.group('d')), int(m.group('e')),
             int(m.group('f'))])
    return systems


def solve(system):
    a, b, c, d, e, f = system
    if (f * a - b * e) % (d * a - c * b) == 0 and (e * d - c * f) % (d * a - c * b) == 0:
        y = int((f * a - b * e) / (d * a - c * b))
        x = int((e * d - c * f) / (d * a - c * b))
        return x, y
    return 0, 0


def sol1(filename):
    systems = get_input(filename)
    tot = 0
    for system in systems:
        x, y = solve(system)
        tot += 3 * x + y
    return tot


def sol2(filename):
    systems = get_input(filename)
    tot = 0
    for system in systems:
        system[4] += 10000000000000
        system[5] += 10000000000000
        x, y = solve(system)
        tot += 3 * x + y
    return tot


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    end1 = time.time()
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    end2 = time.time()
    print(f'Part 1: {end1 - start:.3f}s, Part 2: {end2 - end1:.3f}s, Tot: {end2 - start:.3f}s')
