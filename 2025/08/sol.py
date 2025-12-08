#!/usr/bin/env python3
import itertools


def get_input(filename):
    f = open(filename, 'r')
    boxes = []
    for lr in f.readlines():
        boxes.append(tuple([int(x) for x in lr.strip().split(',')]))
    f.close()
    return boxes


def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2


def get_sorted_distances(boxes):
    distances = []
    for pair in itertools.combinations(boxes, 2):
        distances.append((pair, dist(pair[0], pair[1])))
    return sorted(distances, key=lambda x: x[1])


def next_connection(pair, circuits):
    c1, c2 = set(), set()
    for circuit in circuits:
        if pair[0] in circuit:
            c1 = circuit
        if pair[1] in circuit:
            c2 = circuit
    if c1 != c2:
        circuits.remove(c1)
        circuits.remove(c2)
        circuits.append(c1.union(c2))
    return circuits


def sol1(filename, steps):
    boxes = get_input(filename)
    sorted_distances = get_sorted_distances(boxes)
    circuits = [{box} for box in boxes]
    for i in range(steps):
        pair, _ = sorted_distances[i]
        circuits = next_connection(pair, circuits)
    sizes = sorted([len(c) for c in circuits], reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


def sol2(filename):
    boxes = get_input(filename)
    sorted_distances = get_sorted_distances(boxes)
    circuits = [{box} for box in boxes]
    res = 0
    for i in range(len(sorted_distances)):
        pair, _ = sorted_distances[i]
        circuits = next_connection(pair, circuits)
        if len(circuits) == 1:
            res = pair[0][0] * pair[1][0]
            break
    return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 10)}')
    print(f'Solution: {sol1("input.txt", 1000)}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
