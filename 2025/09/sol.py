#!/usr/bin/env python3
import itertools


def get_input(filename):
    f = open(filename, 'r')
    tiles = []
    for lr in f.readlines():
        tiles.append(tuple([int(x) for x in lr.split(',')]))
    f.close()
    return tiles


def area(p, q):
    return (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) + 1)


def sol1(filename):
    tiles = get_input(filename)
    max_area = 0
    for pair in itertools.combinations(tiles, 2):
        rect_area = area(pair[0], pair[1])
        if rect_area > max_area:
            max_area = rect_area
    return max_area


def line(p, q):
    l = set()
    a1, a2 = min(p[0], q[0]), max(p[0], q[0])
    b1, b2 = min(p[1], q[1]), max(p[1], q[1])
    for a in range(a1, a2 + 1):
        for b in range(b1, b2 + 1):
            l.add((a, b))
    return l


def find_perimeter(tiles):
    perimeter = set()
    for i in range(1, len(tiles)):
        l = line(tiles[i - 1], tiles[i])
        perimeter |= l
    perimeter |= line(tiles[-1], tiles[0])
    return perimeter


def strictly_contains_perimeter(p, q, perimeter):
    a1, a2 = min(p[0], q[0]), max(p[0], q[0])
    b1, b2 = min(p[1], q[1]), max(p[1], q[1])
    for s in perimeter:
        if (a1 < s[0] < a2) and (b1 < s[1] < b2):
            return False
    return True


def sol2(filename):
    tiles = get_input(filename)
    perimeter = find_perimeter(tiles)
    areas = []
    for pair in itertools.combinations(tiles, 2):
        areas.append((pair, area(pair[0], pair[1])))
    areas.sort(key=lambda x: x[1], reverse=True)
    for rect_area in areas:
        p, a = rect_area
        if strictly_contains_perimeter(p[0], p[1], perimeter):
            return a
    return 0


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
