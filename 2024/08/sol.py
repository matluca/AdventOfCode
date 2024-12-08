#!/usr/bin/env python3

import itertools
import time


def get_input(filename):
    f = open(filename, 'r')
    antennas = {}
    lines = f.readlines()
    for i in range(len(lines)):
        for j in range(len(lines[i].strip())):
            c = lines[i][j]
            if c == '.':
                continue
            if c not in antennas.keys():
                antennas[c] = [(i, j)]
            else:
                antennas[c].append((i, j))
    f.close()
    return antennas, len(lines), len(lines[0].strip())


def is_inside(n, size_x, size_y):
    x, y = n
    if (x < 0) or (x >= size_x) or (y < 0) or (y >= size_y):
        return False
    return True


def add_antinodes(antinodes, pair, size_x, size_y):
    a, b = pair
    an1 = (2 * b[0] - a[0], 2 * b[1] - a[1])
    an2 = (2 * a[0] - b[0], 2 * a[1] - b[1])
    for an in [an1, an2]:
        if is_inside(an, size_x, size_y):
            antinodes.add(an)
    return antinodes


def sol1(filename):
    antennas, size_x, size_y = get_input(filename)
    antinodes = set()
    for frequency in antennas.keys():
        for pair in list(itertools.combinations(antennas[frequency], 2)):
            antinodes = add_antinodes(antinodes, pair, size_x, size_y)
    return len(antinodes)


def add_antinodes_2(antinodes, pair, size_x, size_y):
    a, b = pair
    for i in range(size_x):
        an = (b[0] + i * (b[0] - a[0]), b[1] + i * (b[1] - a[1]))
        if is_inside(an, size_x, size_y):
            antinodes.add(an)
        else:
            break
    for i in range(size_x):
        an = (a[0] + i * (a[0] - b[0]), a[1] + i * (a[1] - b[1]))
        if is_inside(an, size_x, size_y):
            antinodes.add(an)
        else:
            break
    return antinodes


def sol2(filename):
    antennas, size_x, size_y = get_input(filename)
    antinodes = set()
    for frequency in antennas.keys():
        for pair in list(itertools.combinations(antennas[frequency], 2)):
            antinodes = add_antinodes_2(antinodes, pair, size_x, size_y)
    return len(antinodes)


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
