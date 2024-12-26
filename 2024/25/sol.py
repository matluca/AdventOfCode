#!/usr/bin/env python3

import time


def get_input(filename):
    f = open(filename, 'r')
    schematics = f.read().split('\n\n')
    f.close()
    locks = []
    keys = []
    for schematic in schematics:
        grid = {}
        i = 0
        for line in schematic.strip().split('\n'):
            for j in range(len(line)):
                grid[(i, j)] = line[j]
            i += 1
        if grid[(0, 0)] == '#':
            lock = []
            for j in range(5):
                lock.append(max([i for i in range(7) if grid[(i, j)] == '#']))
            locks.append(lock)
        else:
            key = []
            for j in range(5):
                key.append(6 - min([i for i in range(7) if grid[(i, j)] == '#']))
            keys.append(key)
    return locks, keys


def sol1(filename):
    locks, keys = get_input(filename)
    tot = 0
    for lock in locks:
        for key in keys:
            fit = True
            for l, k in zip(lock, key):
                if l + k > 5:
                    fit = False
                    break
            if fit:
                tot += 1
    return tot


if __name__ == '__main__':
    start_time = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    end1_time = time.time()
    print(f'Part 1: {end1_time - start_time:.3f}s')
