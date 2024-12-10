#!/usr/bin/env python3

import time


def get_input(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    grid = {}
    for i in range(len(lines)):
        for j in range(len(lines[i].strip())):
            grid[(i, j)] = int(lines[i][j])
    return grid


def neighbours(grid, p):
    v = grid[p]
    n = []
    dirs = (0, 1), (1, 0), (0, -1), (-1, 0)
    for d in dirs:
        q = (p[0] + d[0], p[1] + d[1])
        if q in grid.keys() and grid[q] - v == 1:
            n.append(q)
    return n


def dijkstra(grid, p):
    queue = [p]
    ends = set()
    n_trails = 0
    while queue:
        node = queue.pop(0)
        if grid[node] == 9:
            ends.add(node)
            n_trails += 1
        for n in neighbours(grid, node):
            queue.append(n)
    return len(ends), n_trails


def sol1(filename):
    grid = get_input(filename)
    tot = 0
    for p, value in grid.items():
        if value == 0:
            score, _ = dijkstra(grid, p)
            tot += score
    return tot


def sol2(filename):
    grid = get_input(filename)
    tot = 0
    for p, value in grid.items():
        if value == 0:
            _, n_trails = dijkstra(grid, p)
            tot += n_trails
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
