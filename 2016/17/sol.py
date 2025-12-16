#!/usr/bin/env python3
import time
import hashlib


def get_input(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return [s.strip() for s in lines]


def neighbours(pos, salt, current_path):
    h = hashlib.md5((salt + current_path).encode("utf-8")).hexdigest()
    neigh = []
    if pos == (3, 3):
        return neigh
    if h[0] in ['b', 'c', 'd', 'e', 'f'] and pos[0] > 0:
        neigh.append(('U', (pos[0] - 1, pos[1])))
    if h[1] in ['b', 'c', 'd', 'e', 'f'] and pos[0] < 3:
        neigh.append(('D', (pos[0] + 1, pos[1])))
    if h[2] in ['b', 'c', 'd', 'e', 'f'] and pos[1] > 0:
        neigh.append(('L', (pos[0], pos[1] - 1)))
    if h[3] in ['b', 'c', 'd', 'e', 'f'] and pos[1] < 3:
        neigh.append(('R', (pos[0], pos[1] + 1)))
    return neigh


def min_path(end, salt):
    queue = [('', (0,0))]
    while queue:
        q = sorted(queue, key=len)
        current_state = q.pop(0)
        queue = q
        current_path, current_pos = current_state
        if current_pos == end:
            return current_path
        for neigh in neighbours(current_pos, salt, current_path):
            direction, new_pos = neigh
            new_state = (current_path + direction, new_pos)
            if new_state not in queue:
                queue.append(new_state)
    return None


def sol1(filename):
    salts = get_input(filename)
    return [(salt, min_path((3, 3), salt)) for salt in salts]


def longest_path(end, salt):
    queue = [('', (0,0))]
    longest = 0
    while queue:
        q = sorted(queue, key=len)
        current_state = q.pop(0)
        queue = q
        current_path, current_pos = current_state
        if current_pos == end and len(current_path) > longest:
            longest = len(current_path)
        for neigh in neighbours(current_pos, salt, current_path):
            direction, new_pos = neigh
            new_state = (current_path + direction, new_pos)
            if new_state not in queue:
                queue.append(new_state)
    return longest


def sol2(filename):
    salts = get_input(filename)
    return [(salt, longest_path((3, 3), salt)) for salt in salts]


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
