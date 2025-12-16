#!/usr/bin/env python3
import time


def get_input(filename):
    f = open(filename, 'r')
    r = f.read()
    f.close()
    return int(r)


def value(x, y, n):
    p = x*x + 3*x + 2*x*y + y + y*y + n
    if p.bit_count() % 2 == 0:
        return  '.'
    return '#'


def valid_neighbours(grid, node):
    neigh = []
    for p in [(node[0] - 1, node[1]), (node[0] + 1, node[1]), (node[0], node[1] - 1), (node[0], node[1] + 1)]:
        if p in grid.keys() and grid[p] == '.':
            neigh.append(p)
    return neigh


def find_path_length(node, end, grid):
    visited = set()
    queue = [(0, node)]
    while queue:
        queue.sort()
        current_state = queue.pop(0)
        current_steps, current_node = current_state
        visited.add(current_node)
        if current_node == end:
            return current_steps
        for neigh in valid_neighbours(grid, current_node):
            if neigh not in visited:
                queue.append((current_steps + 1, neigh))
    return None


def sol1(filename, end, size):
    n = get_input(filename)
    grid = {}
    for x in range(size):
        for y in range(size):
            grid[(x, y)] = value(x, y, n)
    return find_path_length((1, 1), end, grid)


def find_locations(node, grid):
    visited = set()
    queue = [(0, node)]
    while queue:
        queue.sort()
        current_state = queue.pop(0)
        current_steps, current_node = current_state
        # print(current_node, current_steps)
        if current_steps > 50:
            return visited
        if current_node in visited:
            continue
        visited.add(current_node)
        for neigh in valid_neighbours(grid, current_node):
            if neigh not in visited:
                queue.append((current_steps + 1, neigh))
    return None


def sol2(filename, size):
    n = get_input(filename)
    grid = {}
    for x in range(size):
        for y in range(size):
            grid[(x, y)] = value(x, y, n)
    locations = find_locations((1, 1), grid)
    return len(locations)


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", (7, 4), 10)}')
    print(f'Solution: {sol1("input.txt", (31, 39), 50)}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt", 50)}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
