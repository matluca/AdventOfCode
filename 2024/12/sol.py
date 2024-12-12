#!/usr/bin/env python3

import time


def get_input(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    grid = {}
    for i in range(len(lines)):
        for j in range(len(lines[i].strip())):
            grid[(i, j)] = lines[i][j]
    return grid


def neighbours(p, grid):
    directions = (-1, 0), (0, -1), (1, 0), (0, 1)
    np = []
    for d in directions:
        n = (p[0] + d[0], p[1] + d[1])
        if n in grid.keys():
            np.append(n)
    return np


def fill_zone(zone_id, grid, zones, is_in_zone, p):
    queue = [p]
    zones[zone_id] = [p]
    is_in_zone[p] = zone_id
    while queue:
        q = queue.pop()
        for n in neighbours(q, grid):
            if n not in is_in_zone.keys() and grid[n] == grid[q]:
                is_in_zone[n] = zone_id
                zones[zone_id].append(n)
                queue.append(n)
    return grid, zones, is_in_zone


def price(z, zones, is_in_zone):
    area = len(zones[z])
    perimeter = 0
    for p in zones[z]:
        for n in [(p[0] + d[0], p[1] + d[1]) for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]]:
            if n not in is_in_zone.keys() or is_in_zone[n] != z:
                perimeter += 1
    return area * perimeter


def sol1(filename):
    grid = get_input(filename)
    zone_id = 0
    zones = {}
    is_in_zone = {}
    while len(is_in_zone) < len(grid):
        for p in [x for x in grid.keys() if x not in is_in_zone.keys()]:
            grid, zones, is_in_zone = fill_zone(zone_id, grid, zones, is_in_zone, p)
            zone_id += 1
            break
    tot = 0
    for z in zones.keys():
        tot += price(z, zones, is_in_zone)
    return tot


def price2(z, zones, is_in_zone):
    area = len(zones[z])
    weighted_angles = {}
    for p in zones[z]:
        up_left = []
        for n in [(p[0] + d[0], p[1] + d[1]) for d in [(-1, 0), (-1, -1), (0, -1)]]:
            try:
                up_left.append(is_in_zone[n])
            except KeyError:
                up_left.append(None)
        if up_left.count(z) in [0, 2]:
            weighted_angles[p] = 1
        if up_left.count(z) == 1 and up_left[1] == z:
            weighted_angles[p] = 2
        up_right = []
        for n in [(p[0] + d[0], p[1] + d[1]) for d in [(-1, 0), (-1, 1), (0, 1)]]:
            try:
                up_right.append(is_in_zone[n])
            except KeyError:
                up_right.append(None)
        if up_right.count(z) in [0, 2]:
            weighted_angles[(p[0], p[1] + 1)] = 1
        if up_right.count(z) == 1 and up_right[1] == z:
            weighted_angles[(p[0], p[1] + 1)] = 2
        bottom_left = []
        for n in [(p[0] + d[0], p[1] + d[1]) for d in [(1, 0), (1, -1), (0, -1)]]:
            try:
                bottom_left.append(is_in_zone[n])
            except KeyError:
                bottom_left.append(None)
        if bottom_left.count(z) in [0, 2]:
            weighted_angles[(p[0] + 1, p[1])] = 1
        if bottom_left.count(z) == 1 and bottom_left[1] == z:
            weighted_angles[(p[0] + 1, p[1])] = 2
        bottom_right = []
        for n in [(p[0] + d[0], p[1] + d[1]) for d in [(1, 0), (1, 1), (0, 1)]]:
            try:
                bottom_right.append(is_in_zone[n])
            except KeyError:
                bottom_right.append(None)
        if bottom_right.count(z) in [0, 2]:
            weighted_angles[(p[0] + 1, p[1] + 1)] = 1
        if bottom_right.count(z) == 1 and bottom_right[1] == z:
            weighted_angles[(p[0] + 1, p[1] + 1)] = 2
    return area * sum(weighted_angles.values())


def sol2(filename):
    grid = get_input(filename)
    zone_id = 0
    zones = {}
    is_in_zone = {}
    while len(is_in_zone) < len(grid):
        for p in [x for x in grid.keys() if x not in is_in_zone.keys()]:
            grid, zones, is_in_zone = fill_zone(zone_id, grid, zones, is_in_zone, p)
            zone_id += 1
            break
    tot = 0
    for z in zones.keys():
        tot += price2(z, zones, is_in_zone)
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
