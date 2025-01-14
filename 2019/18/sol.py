#!/usr/bin/env python3
import functools
from cachetools import cached
from cachetools.keys import hashkey

def get_input(filename):
    f = open(filename, 'r')
    i = 0
    grid = {}
    for line in f.readlines():
        for j, c in enumerate(line.strip()):
            grid[(i, j)] = c
        i += 1
    f.close()
    return grid


def allowed_neighbours(grid, p):
    possible = [(p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)]
    allowed = []
    for n in possible:
        if n not in grid.keys() or grid[n] == '#':
            continue
        allowed.append(n)
    return allowed


def cmp(a, b):
    if len(a[2]) > len(b[2]):
        return -1
    if len(a[2]) < len(b[2]):
        return 1
    if a[0] < b[0]:
        return -1
    if a[0] > b[0]:
        return 1
    return 0


def find_key(grid, key):
    return [k for k in grid.keys() if grid[k] == key][0]


# def shortest_path(grid, n_keys):
#     entrance = [p for p, v in grid.items() if v == '@'][0]
#     visited = set()
#     queue = [(0, entrance, tuple())]
#     while queue:
#         queue.sort(key=functools.cmp_to_key(cmp))
#         current_distance, current_pos, current_keys = queue.pop(0)
#         visited.add((current_pos, current_keys))
#         value = grid[current_pos]
#         next_keys = current_keys
#         if value.islower() and value not in next_keys:
#             next_keys = tuple(sorted(next_keys + (value,)))
#             if len(next_keys) == n_keys:
#                 return current_distance
#         for n in allowed_neighbours(grid, current_pos, next_keys):
#             if (n, next_keys) not in visited and (current_distance + 1, n, next_keys) not in queue:
#                 queue.append((current_distance + 1, n, next_keys))


@cached(cache={}, key=lambda key1, key2, grid: hashkey((key1, key2)))
def shortest_path_from_to(key1, key2, grid):
    if key1 == key2:
        return 0
    k1, k2 = find_key(grid, key1), find_key(grid, key2)
    queue = [(0, k1, [])]
    visited = set()
    while queue:
        queue.sort(key=functools.cmp_to_key(cmp))
        current_distance, current_pos, current_needed_keys = queue.pop(0)
        if current_pos == k2:
            current_needed_keys.remove(key1)
            return current_distance, set(current_needed_keys)
        next_needed_keys = current_needed_keys.copy()
        visited.add(current_pos)
        value = grid[current_pos]
        if value.isupper():
            next_needed_keys.append(value.lower())
        if (value.islower() or value == '@') and value != k2:
            next_needed_keys.append(value)
        for n in allowed_neighbours(grid, current_pos):
            if n not in visited:
                queue.append((current_distance + 1, n, next_needed_keys))


def included(a, b):
    for aa in a:
        if aa not in b:
            return False
    return True


def shortest_path_new(grid):
    keys = [v for v in grid.values() if v.islower()]
    visited = set()
    queue = [(0, '@', ['@'])]
    current_best = 1000000
    while queue:
        queue.sort(key=functools.cmp_to_key(cmp))
        current_distance, current_position, current_path = queue.pop(0)
        if current_distance >= current_best:
            continue
        visited.add(tuple(current_path))
        if len(current_path) == len(keys) + 1:
            print(current_distance)
            current_best = current_distance
            # return current_distance
        for next_key in [k for k in keys if k not in current_path]:
            sp, needed = shortest_path_from_to(current_position, next_key, grid)
            if sp is None:
                continue
            if not needed.issubset(set(current_path)):
                continue
            next_path = current_path.copy()
            next_path.append(next_key)
            if tuple(next_path) not in visited: # and (current_distance + sp, next_key, next_path) not in queue:
                queue.append((current_distance + sp, next_key, next_path))
    return current_best


def sol1(filename):
    grid = get_input(filename)
    return shortest_path_new(grid)


def sol2(filename):
    _ = get_input(filename)
    return 0


if __name__ == '__main__':
    print('--- Part 1 ---')
    # print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    # print('--- Part 2 ---')
    # print(f'Test: {sol2("test.txt")}')
    # print(f'Solution: {sol2("input.txt")}')
