#!/usr/bin/env python3
import itertools
import numpy


def get_input(filename):
    f = open(filename, 'r')
    packages = []
    for line in f:
        packages.append(int(line.strip()))
    f.close()
    return packages


def sol(filename, groups):
    packages = get_input(filename)
    tot_weight = sum(packages)
    min_len = 0
    qe = float('infinity')
    for i in range(len(packages)):
        for first in itertools.combinations(packages, i):
            if sum(first) != tot_weight / groups:
                continue
            min_len = len(first)
            quantum_ent = numpy.prod(first)
            if quantum_ent < qe:
                qe = quantum_ent
        if min_len > 0:
            break
    return qe


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol("test.txt", 3)}')
    print(f'Solution: {sol("input.txt", 3)}')
    print('--- Part 2 ---')
    print(f'Test: {sol("test.txt", 4)}')
    print(f'Solution: {sol("input.txt", 4)}')
