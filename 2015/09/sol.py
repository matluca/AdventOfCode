#!/usr/bin/env python3
import itertools


def get_input(filename):
    f = open(filename, 'r')
    dist = {}
    for line in f:
        points, d = line.strip().split(' = ')
        a, b = points.split(' to ')
        dist[(a, b)] = int(d)
        dist[(b, a)] = int(d)
    f.close()
    return dist


def sol1(filename):
    dist = get_input(filename)
    cities = []
    for d in dist.keys():
        for c in d:
            if c not in cities:
                cities.append(c)
    res = max(dist.values()) * len(cities)
    for perm in itertools.permutations(cities):
        tot = 0
        for i in range(len(perm) - 1):
            tot += dist[(perm[i], perm[i+1])]
        if tot < res:
            res = tot
    return res


def sol2(filename):
    dist = get_input(filename)
    cities = []
    for d in dist.keys():
        for c in d:
            if c not in cities:
                cities.append(c)
    res = 0
    for perm in itertools.permutations(cities):
        tot = 0
        for i in range(len(perm) - 1):
            tot += dist[(perm[i], perm[i+1])]
        if tot > res:
            res = tot
    return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
