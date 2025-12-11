#!/usr/bin/env python3
from cachetools import cached
from cachetools.keys import hashkey


def get_input(filename):
    graph = {}
    f = open(filename, 'r')
    for lr in f.readlines():
        key = lr.split(':')[0]
        values = lr.split(':')[1].split()
        graph[key] = values
    f.close()
    return graph


@cached(cache={}, key=lambda graph, start, end: hashkey(start, end))
def count_paths(graph, start, end):
    if start == end:
        return 1
    if start not in graph.keys():
        return 0
    return sum(count_paths(graph, child, end) for child in graph[start])


def sol1(filename):
    graph = get_input(filename)
    count_paths.cache.clear()
    return count_paths(graph, 'you', 'out')


def sol2(filename):
    graph = get_input(filename)
    count_paths.cache.clear()
    a = count_paths(graph, 'svr', 'fft')
    b = count_paths(graph, 'fft', 'dac')
    c = count_paths(graph, 'dac', 'out')
    p1 = a * b * c
    d = count_paths(graph, 'svr', 'dac')
    e = count_paths(graph, 'dac', 'fft')
    f = count_paths(graph, 'fft', 'out')
    p2 = d * e * f
    return p1 + p2

if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
