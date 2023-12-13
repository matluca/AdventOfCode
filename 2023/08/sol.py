#!/usr/bin/env python3
import math


def get_input(filename):
    f = open(filename, 'r').read()
    lr, graph_raw = f.split('\n\n')
    graph = {}
    for line in graph_raw.split('\n'):
        graph[line.split(' = (')[0]] = (line.split('(')[1].split(',')[0], line.split(', ')[1].split(')')[0])
    return lr, graph


def sol1(filename):
    lr, graph = get_input(filename)
    found = False
    steps = 0
    point = 'AAA'
    while not found:
        if lr[steps % len(lr)] == 'L':
            point = graph[point][0]
        else:
            point = graph[point][1]
        if point == 'ZZZ':
            found = True
        steps += 1
    return steps


def sol2(filename):
    lr, graph = get_input(filename)
    points = [p for p in graph.keys() if p[2] == 'A']
    steps = []
    for p in points:
        x = p
        s = 0
        while True:
            direction = s % len(lr)
            if x[2] == 'Z':
                break
            if lr[direction] == 'L':
                x = graph[x][0]
            else:
                x = graph[x][1]
            s += 1
        steps.append(s)
    return math.lcm(*steps)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Test 2: {sol1("test2.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test3.txt")}')
    print(f'Solution: {sol2("input.txt")}')
