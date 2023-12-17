#!/usr/bin/env python3
import heapq


def get_input(filename):
    f = open(filename, 'r').read()
    lines = f.split('\n')
    grid = {}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            grid[(i, j)] = int(lines[i][j])
    return grid, (len(lines), len(lines[0]))


def get_neighbours(p, grid):
    all_poss = [(p[0] + 1, p[1]), (p[0] - 1, p[1]), (p[0], p[1] + 1), (p[0], p[1] - 1)]
    return [p for p in all_poss if p in grid]


def dijkstra(grid, start, end, min_cons, max_cons):
    visited = set()
    queue = [(0, start, (1, 0), 1), (0, start, (0, 1), 1)]
    while queue:
        cost, node, current_dir, dir_count = heapq.heappop(queue)
        if (node, current_dir, dir_count) in visited:
            continue
        visited.add((node, current_dir, dir_count))
        new_node = (node[0] + current_dir[0], node[1] + current_dir[1])
        if new_node not in get_neighbours(node, grid):
            continue
        new_cost = cost + grid[new_node]
        if min_cons <= dir_count <= max_cons and new_node == end:
            return new_cost
        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (d[0] + current_dir[0], d[1] + current_dir[1]) == (0, 0):
                continue
            new_dir_count = dir_count + 1 if d == current_dir else 1
            if new_dir_count > max_cons:
                continue
            if d != current_dir and dir_count < min_cons:
                continue
            heapq.heappush(queue, (new_cost, new_node, d, new_dir_count))


def sol1(filename):
    grid, size = get_input(filename)
    start = (0, 0)
    end = (size[0]-1, size[1]-1)
    return dijkstra(grid, start, end, 0, 3)


def sol2(filename):
    grid, size = get_input(filename)
    start = (0, 0)
    end = (size[0]-1, size[1]-1)
    return dijkstra(grid, start, end, 4, 10)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
