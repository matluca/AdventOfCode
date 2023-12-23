#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    grid = {}
    size = 0
    for i, line in enumerate(f):
        for j, c in enumerate(line.strip()):
            grid[(i, j)] = c
        size += 1
    f.close()
    return grid, size - 1


def node_neighbours(grid, node, previous):
    special = []
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        p = (node[0] + d[0], node[1] + d[1])
        if p == previous or p not in grid.keys():
            continue
        if grid[p] == 'v' and d == (-1, 0):
            continue
        if grid[p] == '>' and d == (0, -1):
            continue
        if grid[p] in ['>', 'v']:
            special.append(p)
    return special


def move_forward(grid, node, previous):
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        p = (node[0] + d[0], node[1] + d[1])
        if p == previous:
            continue
        if p in grid.keys() and grid[p] == '.':
            return p
    return None


def move_forward_2(grid, node, previous):
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        p = (node[0] + d[0], node[1] + d[1])
        if p == previous:
            continue
        if p in grid.keys() and grid[p] != '#':
            return p
    return None


def find_children(grid, node):
    previous = node
    current = node
    if grid[node] == '>':
        current = (node[0], node[1] + 1)
    elif grid[node] == '<':
        current = (node[0], node[1] - 1)
    elif grid[node] == 'v':
        current = (node[0] + 1, node[1])
    elif grid[node] == '^':
        current = (node[0] - 1, node[1])
    steps = 2
    while True:
        node_neigh = node_neighbours(grid, current, previous)
        if len(node_neigh) > 0:
            return [(n, steps) for n in node_neigh]
        next_step = move_forward(grid, current, previous)
        if next_step is None:
            return []
        previous = current
        current = next_step
        steps += 1


def find_paths(tree, a, b):
    if a == b:
        return [0]
    paths = []
    children = tree[a]
    for child in children:
        node, distance = child
        paths = paths + [(x + distance) for x in find_paths(tree, node, b)]
    return paths


def sol1(filename):
    grid, size = get_input(filename)
    start = (0, 1)
    end = (size, size - 1)
    grid[start] = 'v'
    grid[end] = 'v'
    nodes = []
    for p, c in grid.items():
        if c not in ['.', '#']:
            nodes.append(p)
    tree = {}
    for n in nodes:
        tree[n] = find_children(grid, n)
    paths = find_paths(tree, start, end)
    return max(paths)


def find_children_2(grid, nodes, node):
    next_nodes = []
    children = []
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        p = (node[0] + d[0], node[1] + d[1])
        if p in grid.keys() and grid[p] != '#':
            next_nodes.append(p)
    for next_node in next_nodes:
        previous = node
        current = next_node
        steps = 2
        found = False
        while not found:
            next_step = move_forward_2(grid, current, previous)
            if next_step is None:
                return []
            if next_step in nodes:
                children.append((next_step, steps))
                found = True
            previous = current
            current = next_step
            steps += 1
    return children


def find_paths_2(tree, a, b, path):
    if a == b:
        return [([a], 0)]
    paths = []
    children = tree[a]
    for child in children:
        node, distance = child
        if node in path:
            continue
        child_paths = find_paths_2(tree, node, b, path + [node])
        new_paths = []
        for child_path in child_paths:
            new_paths.append(([a] + child_path[0], distance + child_path[1]))
        paths = paths + new_paths
    return paths


def sol2(filename):
    grid, size = get_input(filename)
    start = (0, 1)
    end = (size, size - 1)
    grid[start] = 'v'
    grid[end] = 'v'
    nodes = [start]
    for node in grid.keys():
        free = 0
        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            p = (node[0] + d[0], node[1] + d[1])
            if p in grid.keys() and grid[p] != '#' and grid[node] != '#':
                free += 1
        if free > 2:
            nodes.append(node)
    nodes.append(end)
    tree = {}
    for node in nodes:
        tree[node] = find_children_2(grid, nodes, node)
    paths = find_paths_2(tree, start, end, [])
    return max([p[1] for p in paths])


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
