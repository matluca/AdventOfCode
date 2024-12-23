#!/usr/bin/env python3
import re
import time


def get_input(filename):
    f = open(filename, 'r')
    regex = '(\w+)-(\w+)'
    graph = {}
    for match in re.finditer(regex, f.read()):
        a, b = match.group(1), match.group(2)
        if a not in graph.keys():
            graph[a] = []
        if b not in graph.keys():
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    f.close()
    return graph


def find_groups(graph, n):
    groups = set()
    if n > 2:
        previous_groups = find_groups(graph, n - 1)
        for previous_group in previous_groups:
            for k in [kk for kk in graph.keys() if kk not in previous_groups]:
                connected = True
                for n in previous_group:
                    if k not in graph[n]:
                        connected = False
                        break
                if connected:
                    new_group = list(previous_group + (k,))
                    groups.add(tuple(sorted(new_group)))
        return groups
    for n1 in graph.keys():
        if n1[0] != 't':
            continue
        for n2 in graph[n1]:
            groups.add(tuple(sorted([n1, n2])))
    return groups


def sol1(filename):
    graph = get_input(filename)
    return len(find_groups(graph, 3))


def sol2(filename):
    graph = get_input(filename)
    for n in range(3, len(graph.keys())):
        groups = find_groups(graph, n)
        if len(groups) == 1:
            return ','.join(groups.pop())
    return None


if __name__ == '__main__':
    start_time = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    end1_time = time.time()
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    end2_time = time.time()
    print(
        f'Part 1: {end1_time - start_time:.3f}s, Part 2: {end2_time - end1_time:.3f}s, Tot: {end2_time - start_time:.3f}s')
