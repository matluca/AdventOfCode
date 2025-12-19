#!/usr/bin/env python3
import itertools
import time


def get_input(filename):
    grid = {}
    f = open(filename, 'r')
    max_n = 0
    for i, line in enumerate(f.readlines()):
        for j, c in enumerate(list(line.strip())):
            grid[(i, j)] = c
            try:
                v = int(c)
                if v > max_n:
                    max_n = v
            except ValueError:
                pass
    f.close()
    return grid, max_n


def neighbours(node, grid):
    neigh = []
    for n in [(node[0] - 1, node[1]), (node[0] + 1, node[1]), (node[0], node[1] - 1), (node[0], node[1] + 1)]:
        if n in grid.keys() and grid[n] != '#':
            neigh.append(n)
    return neigh


def distance(n1, n2, grid):
    node1 = [key for key, value in grid.items() if value == str(n1)][0]
    node2 = [key for key, value in grid.items() if value == str(n2)][0]
    visited = set(node1)
    queue = [(0, node1)]
    while queue:
        queue.sort()
        current_state = queue.pop(0)
        current_steps, current_node = current_state
        visited.add(current_node)
        if current_node == node2:
            return current_steps
        for n in neighbours(current_node, grid):
            if n not in visited and (current_steps + 1, n) not in queue:
                queue.append((current_steps + 1, n))
    return None


def sol1(filename):
    grid, max_n = get_input(filename)
    distances = {}
    for i in range(max_n + 1):
        for j in range(i + 1, max_n + 1):
            distances[(i, j)] = distance(i, j, grid)
            distances[(j, i)] = distances[(i, j)]
    min_distance = float('infinity')
    for p in itertools.permutations(range(1, max_n + 1)):
        dist = distances[(0, p[0])]
        for j in range(1, max_n):
            dist += distances[(p[j - 1], p[j])]
        if dist < min_distance:
            min_distance = dist
    return min_distance


def sol2(filename):
    grid, max_n = get_input(filename)
    distances = {}
    for i in range(max_n + 1):
        for j in range(i + 1, max_n + 1):
            distances[(i, j)] = distance(i, j, grid)
            distances[(j, i)] = distances[(i, j)]
    min_distance = float('infinity')
    for p in itertools.permutations(range(1, max_n + 1)):
        dist = distances[(0, p[0])] + distances[(p[-1], 0)]
        for j in range(1, max_n):
            dist += distances[(p[j - 1], p[j])]
        if dist < min_distance:
            min_distance = dist
    return min_distance


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
