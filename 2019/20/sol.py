#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    grid = {}
    for i, line in enumerate(f.readlines()):
        for j, c in enumerate(line):
            if c != ' ':
                grid[(i, j)] = c
    f.close()
    return grid


def simplify_grid(grid):
    for p in [p for p, v in grid.items() if v == '.']:
        if grid[(p[0], p[1] + 1)].isupper():
            grid[(p[0], p[1] + 1)] += grid[(p[0], p[1] + 2)]
        if grid[(p[0], p[1] - 1)].isupper():
            grid[(p[0], p[1] - 1)] = grid[(p[0], p[1] - 2)] + grid[(p[0], p[1] - 1)]
        if grid[(p[0] + 1, p[1])].isupper():
            grid[(p[0] + 1, p[1])] += grid[(p[0] + 2, p[1])]
        if grid[(p[0] - 1, p[1])].isupper():
            grid[(p[0] - 1, p[1])] = grid[(p[0] - 2, p[1])] + grid[(p[0] - 1, p[1])]
    return grid


def valid_neighbours(grid, p):
    neigh = set()
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        q = (p[0] + d[0], p[1] + d[1])
        if q in grid.keys():
            if grid[q] == '.':
                neigh.add(q)
            elif len(grid[q]) == 2:
                label = grid[q]
                teleport = [x for x in find(grid, label) if x != p]
                if len(teleport) > 0:
                    neigh.add(teleport[0])
    return neigh


def find(grid, value):
    labels = [p for p, v in grid.items() if v == value]
    neigh = []
    for label in labels:
        neigh += valid_neighbours(grid, label)
    return neigh


def find_shortest_path(grid):
    start = find(grid, 'AA')[0]
    end = find(grid, 'ZZ')[0]
    visited = set()
    queue = [(0, start)]
    while queue:
        queue.sort()
        current_distance, current_pos = queue.pop(0)
        if current_pos == end:
            return current_distance
        visited.add(current_pos)
        for n in valid_neighbours(grid, current_pos):
            if n not in visited:
                queue.append((current_distance + 1, n))


def is_external(grid, p):
    max_x, max_y = max([p[0] for p in grid.keys()]), max([p[1] for p in grid.keys()])
    return (p[0] in [2, max_x - 2]) or (p[1] in [2, max_y - 3])


def find_external(grid, value):
    vs = find(grid, value)
    if value in ['AA', 'ZZ']:
        return vs[0]
    if is_external(grid, vs[0]):
        return vs[0]
    if is_external(grid, vs[1]):
        return vs[1]
    return None


def find_internal(grid, value):
    vs = find(grid, value)
    if value in ['AA', 'ZZ']:
        return None
    ext = find_external(grid, value)
    return [v for v in vs if v != ext][0]


def neighbours(grid, p):
    neigh = set()
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        q = (p[0] + d[0], p[1] + d[1])
        if q in grid.keys() and grid[q] == '.':
                neigh.add(q)
    return neigh


def find_distance_same_level(grid, start, end):
    visited = set()
    queue = [(0, start)]
    while queue:
        queue.sort()
        current_distance, current_pos = queue.pop(0)
        if current_pos == end:
            return current_distance
        visited.add(current_pos)
        for n in neighbours(grid, current_pos):
            if n not in visited:
                queue.append((current_distance + 1, n))


def build_graph(grid):
    labels = [v for v in grid.values() if len(v) == 2]
    label_locations = {}
    for label in labels:
        if label in ['AA', 'ZZ']:
            label_locations[label] = find_external(grid, label)
        else:
            label_locations[label + 'e'] = find_external(grid, label)
            label_locations[label + 'i'] = find_internal(grid, label)
    graph = {}
    labels = list(label_locations.keys())
    for label in labels:
        graph[label] = {}
    for i, label1 in enumerate(labels):
        for label2 in labels[i + 1:]:
            distance = find_distance_same_level(grid, label_locations[label1], label_locations[label2])
            if distance is not None:
                graph[label1][label2] = distance
                graph[label2][label1] = distance
    return graph


def valid_neighbours_2(graph, p, level):
    neigh = []
    for q, d in graph[p].items():
        if q == 'AA':
            continue
        if q == 'ZZ' and level != 0:
            continue
        if level == 0 and len(q) == 3 and q[2] == 'e':
            continue
        neigh.append((q, d))
    return neigh


def find_shortest_path_2(graph):
    start = 'AA'
    end = 'ZZ'
    end_level = 0
    visited = set()
    queue = [(0, 0, start)]
    while queue:
        queue.sort()
        current_distance, current_level, current_pos = queue.pop(0)
        if current_pos == end and current_level == end_level:
            return current_distance
        visited.add((current_pos, current_level))
        for n in valid_neighbours_2(graph, current_pos, current_level):
            next_label, dist = n
            if len(next_label) == 3 and next_label[2] == 'e':
                if (next_label[:2] + 'i', current_level - 1) not in visited and (current_distance + dist + 1, current_level - 1, next_label[:2] + 'i') not in queue:
                    queue.append((current_distance + dist + 1, current_level - 1, next_label[:2] + 'i'))
            if len(next_label) == 3 and next_label[2] == 'i':
                if (next_label[:2] + 'e', current_level + 1) not in visited and (current_distance + dist + 1, current_level + 1, next_label[:2] + 'e') not in queue:
                    queue.append((current_distance + dist + 1, current_level + 1, next_label[:2] + 'e'))
            if next_label == 'ZZ' and current_level == 0:
                queue.append((current_distance + dist, current_level, next_label))

def sol1(filename):
    grid = get_input(filename)
    grid = simplify_grid(grid)
    return find_shortest_path(grid)


def sol2(filename):
    grid = get_input(filename)
    grid = simplify_grid(grid)
    graph = build_graph(grid)
    return find_shortest_path_2(graph)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
