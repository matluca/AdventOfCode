#!/usr/bin/env python3
import itertools
import time


class Node:
    def __init__(self, df_raw):
        name = df_raw.split()[0]
        self.position = (int(name.split('-')[1][1:]), int(name.split('-')[2][1:]))
        self.size = int(df_raw.split()[1][:-1])
        self.used = int(df_raw.split()[2][:-1])
        self.avail = int(df_raw.split()[3][:-1])


def get_input(filename):
    f = open(filename, 'r')
    nodes = []
    for line in f.readlines()[2:]:
        nodes.append(Node(line))
    f.close()
    return nodes


def sol1(filename):
    nodes = get_input(filename)
    tot = 0
    for node1, node2 in itertools.combinations(nodes, 2):
        if node1.used != 0 and node1.used <= node2.avail:
            tot += 1
        if node2.used != 0 and node2.used <= node1.avail:
            tot += 1
    return tot


def print_grid(grid):
    size_x, size_y = max([node[1] for node in grid.keys()]), max([node[0] for node in grid.keys()])
    for i in range(size_x + 1):
        for j in range(size_y + 1):
            print(grid[(j, i)], end='')
        print()


def neighbours(grid, node):
    neighs = []
    for neigh in [(node[0] - 1, node[1]), (node[0] + 1, node[1]), (node[0], node[1] - 1), (node[0], node[1] + 1)]:
        if neigh in grid.keys():
            neighs.append(neigh)
    return neighs


def min_path(grid):
    empty = [key for key, value in grid.items() if value == '_'][0]
    goal = [key for key, value in grid.items() if value == 'X'][0]
    queue = [(0, empty)]
    visited = set(empty)
    while queue:
        queue.sort()
        current_state = queue.pop(0)
        current_steps, current_node = current_state
        visited.add(current_node)
        if current_node == goal:
            return current_steps
        for neigh in neighbours(grid, current_node):
            if grid[neigh] != '#' and neigh not in visited and (current_steps + 1, neigh) not in queue:
                queue.append((current_steps + 1, neigh))
    return empty, goal


def distance(grid):
    goal = [key for key, value in grid.items() if value == 'X'][0]
    return goal[0] + goal[1]


def sol2(filename):
    nodes = get_input(filename)
    grid = {}
    limit = [node.avail for node in nodes if node.used == 0][0]
    for node in nodes:
        if node.used == 0:
            grid[node.position] = '_'
        elif node.used > limit:
            grid[node.position] = '#'
        else:
            grid[node.position] = '.'
    grid[(0, 0)] = 0
    grid[(max([node.position[0] for node in nodes]), 0)] = 'X'
    # print_grid(grid)
    return min_path(grid) + 5 * (distance(grid) - 1)


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
