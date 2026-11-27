#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    regexes = [line.strip()[1:-1] for line in f.readlines()]
    f.close()
    return regexes


def build_graph(regex):
    graph = {(0, 0): set()}
    current_positions = {(0, 0)}
    stack = []
    for c in regex:
        new_positions = set()
        if c == '(':
            stack.append((current_positions, set()))
        elif c == '|':
            starts, ends = stack[-1]
            ends |= current_positions
            current_positions = starts
        elif c == ')':
            starts, ends = stack.pop()
            current_positions = ends | current_positions
        if c in ['E', 'W', 'N', 'S']:
            for a in current_positions:
                x, y = a
                if c == 'E':
                    b = (x + 1, y)
                elif c == 'W':
                    b = (x - 1, y)
                elif c == 'N':
                    b = (x, y + 1)
                elif c == 'S':
                    b = (x, y - 1)
                if b not in graph.keys():
                    graph[b] = set()
                graph[b].add(a)
                graph[a].add(b)
                new_positions.add(b)
            current_positions = new_positions
    return graph


def distances(graph):
    dist = {(0, 0): 0}
    queue = [((0, 0), 0)]
    while queue:
        current_pos, current_dist = queue.pop(0)
        for next_pos in graph[current_pos]:
            if next_pos in dist.keys():
                continue
            queue.append((next_pos, current_dist + 1))
            dist[next_pos] = current_dist + 1
    return dist


def sol1(filename):
    regexes = get_input(filename)
    solutions = []
    for regex in regexes:
        graph = build_graph(regex)
        dist = distances(graph)
        solutions.append(max(dist.values()))
    return solutions


def sol2(filename):
    regexes = get_input(filename)
    solutions = []
    for regex in regexes:
        graph = build_graph(regex)
        dist = distances(graph)
        solutions.append(sum([1 for d in dist.values() if d >= 1000]))
    return solutions


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
