#!/usr/bin/env python3

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


def find_key(grid, key):
    return [k for k in grid.keys() if grid[k] == key][0]


def allowed_neighbours(grid, p):
    possible = [(p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)]
    allowed = []
    for n in possible:
        if n not in grid.keys() or grid[n] == '#':
            continue
        allowed.append(n)
    return allowed


def shortest_path_from_to(key1, key2, grid):
    if key1 == key2:
        return 0
    k1, k2 = find_key(grid, key1), find_key(grid, key2)
    queue = [(0, k1, [])]
    visited = set()
    while queue:
        queue.sort()
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


def allowed_next_keys(graph, current_path, last_key):
    next_keys = []
    for k, v in graph[last_key].items():
        allowed = True
        for needed in v[1]:
            if needed not in current_path and needed != last_key:
                allowed = False
                break
        if allowed and k not in current_path:
            next_keys.append((k, v[0]))
    return next_keys


def build_graph(grid, part):
    keys = [k for k in grid.values() if k.islower()]
    keys.append('@')
    if part == 2:
        keys.append('^')
        keys.append('$')
        keys.append('%')
    graph = {key: {} for key in keys}
    for i, key1 in enumerate(keys):
        for j in range(i + 1, len(keys)):
            key2 = keys[j]
            if shortest_path_from_to(key1, key2, grid) is None:
                continue
            distance, doors = shortest_path_from_to(key1, key2, grid)
            graph[key1][key2] = distance, doors
            graph[key2][key1] = distance, doors
    return graph


def shortest_path(grid):
    graph = build_graph(grid, 1)
    queue = [(0, set('@'), '@')]
    visited = set()
    while True:
        queue.sort()
        current_distance, current_opened, last_key = queue.pop(0)
        current_path = list(current_opened)
        current_path.append(last_key)
        visited.add(tuple(sorted(current_path)))
        if len(current_path) == len(graph):
            return current_distance
        next_keys = allowed_next_keys(graph, current_path, current_path[-1])
        for next_key in next_keys:
            key, distance = next_key
            next_path = current_path.copy()
            next_path.append(key)
            if tuple(sorted(next_path)) not in visited and (current_distance + distance, set(current_path), key) not in queue:
                queue.append((current_distance + distance, set(current_path), key))


def sol1(filename):
    grid = get_input(filename)
    return shortest_path(grid)


def print_grid(grid):
    max_x = max([p[0] for p in grid.keys()])
    max_y = max([p[1] for p in grid.keys()])
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            print(grid[(x, y)], end='')
        print()


def allowed_next_keys_2(graph, current_opened, last_keys):
    next_keys = []
    for last_key in last_keys:
        next_keys.append(allowed_next_keys(graph, current_opened, last_key))
    return next_keys


def shortest_path_2(grid):
    graph = build_graph(grid, 2)
    queue = [(0, {'@', '^', '$', '%'}, ['@', '^', '$', '%'])]
    visited = set()
    while True:
        queue.sort()
        current_distance, current_opened, last_keys = queue.pop(0)
        current_path = list(current_opened)
        visited.add(tuple(sorted(current_path)))
        if len(current_path) == len(graph):
            return current_distance
        next_keys_all = allowed_next_keys_2(graph, current_opened, last_keys)
        for i in range(4):
            next_keys = next_keys_all[i]
            for next_key in next_keys:
                key, distance = next_key
                next_opened = current_opened.copy()
                next_opened.add(key)
                next_last_keys = last_keys.copy()
                next_last_keys[i] = key
                if tuple(sorted(list(next_opened))) not in visited and (current_distance + distance, next_opened, next_last_keys) not in queue:
                    queue.append((current_distance + distance, next_opened, next_last_keys))


def sol2(filename):
    grid = get_input(filename)
    c = find_key(grid, '@')
    grid[(c[0] - 1, c[1] - 1)] = '@'
    grid[(c[0] - 1, c[1] + 1)] = '^'
    grid[(c[0] + 1, c[1] - 1)] = '$'
    grid[(c[0] + 1, c[1] + 1)] = '%'
    grid[(c[0] - 1, c[1])] = '#'
    grid[(c[0] + 1, c[1])] = '#'
    grid[(c[0], c[1] - 1)] = '#'
    grid[(c[0], c[1] + 1)] = '#'
    grid[c] = '#'
    return shortest_path_2(grid)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test 1: {sol1("test1.txt")}')
    print(f'Test 2: {sol1("test2.txt")}')
    print(f'Test 4: {sol1("test4.txt")}')
    print(f'Test 3: {sol1("test3.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test5.txt")}')
    print(f'Test: {sol2("test6.txt")}')
    print(f'Test: {sol2("test7.txt")}')
    print(f'Solution: {sol2("input.txt")}')
