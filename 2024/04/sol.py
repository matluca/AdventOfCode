#!/usr/bin/env python3

import time

def get_input(filename):
    matrix = []
    f = open(filename, 'r')
    for line in f.readlines():
        if len(line.strip()) > 0:
            matrix.append(line.strip())
    f.close()
    return matrix


def can_continue(x, y, matrix, level, direction):
    if not (0 <= x < len(matrix)):
        return False
    if not (0 <= y < len(matrix[x])):
        return False
    letter = matrix[x][y]
    if level == 0 and letter != 'X':
        return False
    if level == 1 and letter != 'M':
        return False
    if level == 2 and letter != 'A':
        return False
    if level == 3:
        return letter == 'S'
    return can_continue(x + direction[0], y + direction[1], matrix, level + 1, direction)


def sol1(filename):
    matrix = get_input(filename)
    size_x = len(matrix)
    size_y = len(matrix[0])
    tot = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for x in range(size_x):
        for y in range(size_y):
            if matrix[x][y] == 'X':
                for direction in directions:
                    if can_continue(x, y, matrix, 0, direction):
                        tot += 1
    return tot


def is_xmas(x, y, matrix):
    if matrix[x][y] != 'A':
        return False
    if (x == 0) or (x == len(matrix)-1) or (y == 0) or (y == len(matrix[x])-1):
        return False
    d1 = [matrix[x - 1][y - 1], matrix[x + 1][y + 1]]
    if ('M' not in d1) or ('S' not in d1):
        return False
    d2 = [matrix[x - 1][y + 1], matrix[x + 1][y - 1]]
    if ('M' not in d2) or ('S' not in d2):
        return False
    return True


def sol2(filename):
    matrix = get_input(filename)
    size_x = len(matrix)
    size_y = len(matrix[0])
    tot = 0
    for x in range(size_x):
        for y in range(size_y):
            if is_xmas(x, y, matrix):
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
