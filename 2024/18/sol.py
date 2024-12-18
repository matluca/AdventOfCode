#!/usr/bin/env python3

import time


def get_input(filename):
    f = open(filename, 'r')
    byte_pos = []
    for line in f.readlines():
        byte_pos.append((int(line.split(',')[0]), int(line.strip().split(',')[1])))
    f.close()
    return byte_pos


def dijkstra(obstacles, size):
    start = (0, 0)
    end = (size, size)
    queue = [(0, start)]
    visited = {start}
    while queue:
        queue.sort()
        current_length, current_pos = queue.pop(0)
        if current_pos == end:
            return current_length
        for n in [(current_pos[0] + d[0], current_pos[1] + d[1]) for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]]:
            if (0 <= n[0] <= size) and (0 <= n[1] <= size) and (n not in obstacles) and (n not in visited):
                visited.add(n)
                queue.append((current_length + 1, n))


def sol1(filename, size, max_bytes):
    byte_pos = get_input(filename)
    return dijkstra(byte_pos[:max_bytes], size)


def bisection(min_bytes, max_bytes, size, byte_pos):
    while max_bytes - min_bytes >= 2:
        new_bytes = int((max_bytes + min_bytes) / 2)
        d = dijkstra(byte_pos[:new_bytes], size)
        if d is None:
            max_bytes = new_bytes
        else:
            min_bytes = new_bytes
    return byte_pos[min_bytes]


def sol2(filename, size):
    byte_pos = get_input(filename)
    return bisection(0, len(byte_pos), size, byte_pos)


if __name__ == '__main__':
    start_time = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 6, 12)}')
    print(f'Solution: {sol1("input.txt", 70, 1024)}')
    end1_time = time.time()
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt", 6)}')
    print(f'Solution: {sol2("input.txt", 70)}')
    end2_time = time.time()
    print(
        f'Part 1: {end1_time - start_time:.3f}s, Part 2: {end2_time - end1_time:.3f}s, Tot: {end2_time - start_time:.3f}s')
