#!/usr/bin/env python3

import time

U, R, D, L = (-1, 0), (0, 1), (1, 0), (0, -1)

def get_input(filename):
    f = open(filename, 'r')
    lines = []
    guard = (0, 0, U)
    for line in f.readlines():
        lines.append(line.strip())
    f.close()
    obstacles = set()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                obstacles.add((i, j))
            elif lines[i][j] == '^':
                pos = (i, j)
                guard = (pos, U)
    return obstacles, guard, len(lines), len(lines[0])


def turn_right(direction):
    if direction == U:
        return R
    elif direction == R:
        return D
    elif direction == D:
        return L
    else:
        return U


def next_position(obstacles, guard, visited, size_x, size_y):
    pos = guard[0]
    direction = guard[1]
    next_pos = (pos[0] + direction[0], pos[1] + direction[1])
    a, b = next_pos
    if (a < 0) or (b < 0) or (a >= size_x) or (b >= size_y):
        return next_pos, visited, True
    if next_pos in obstacles:
        direction = turn_right(direction)
        next_pos = pos
    new_guard = (next_pos, direction)
    visited.add(next_pos)
    return new_guard, visited, False


def travel1(obstacles, guard, size_x, size_y):
    pos = guard[0]
    visited = {pos}
    end = False
    while not end:
        guard, visited, end = next_position(obstacles, guard, visited, size_x, size_y)
    return visited

def sol1(filename):
    obstacles, guard, size_x, size_y = get_input(filename)
    visited = travel1(obstacles, guard, size_x, size_y)
    return len(visited)


def next_position_2(obstacles, guard, visited, size_x, size_y):
    pos = guard[0]
    direction = guard[1]
    next_pos = (pos[0] + direction[0], pos[1] + direction[1])
    a, b = next_pos
    if (a < 0) or (b < 0) or (a >= size_x) or (b >= size_y):
        return next_pos, visited, True, False
    if next_pos in obstacles:
        direction = turn_right(direction)
        next_pos = pos
    new_guard = (next_pos, direction)
    if new_guard in visited:
        return new_guard, visited, False, True
    visited.add(new_guard)
    return new_guard, visited, False, False


def travel2(obstacles, guard, size_x, size_y):
    visited = {guard}
    while True:
        guard, visited, end, loop = next_position_2(obstacles, guard, visited, size_x, size_y)
        if end:
            return False
        if loop:
            return True


def sol2(filename):
    obstacles, guard, size_x, size_y = get_input(filename)
    tot = 0
    t1 = travel1(obstacles, guard, size_x, size_y)
    for p in t1:
        pos = guard[0]
        if p != pos:
            new_obstacles = obstacles.copy()
            new_obstacles.add(p)
            is_loop = travel2(new_obstacles, guard, size_x, size_y)
            if is_loop:
                tot += 1
    return tot


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    end1 = time.time()
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    end2 = time.time()
    print(f'Part 1: {end1 - start:.3f}s, Part 2: {end2 - end1:.3f}s, Tot: {end2 - start:.3f}s')
