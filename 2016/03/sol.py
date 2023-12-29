#!/usr/bin/env python3
import time


def get_input(filename):
    f = open(filename, 'r')
    triangles = []
    for line in f:
        triangle_raw = line.strip().split()
        triangles.append([int(t) for t in triangle_raw])
    f.close()
    return triangles


def sol1(filename):
    triangles = get_input(filename)
    possible = 0
    for triangle in triangles:
        triangle.sort()
        if triangle[0] + triangle[1] > triangle[2]:
            possible += 1
    return possible


def sol2(filename):
    triangles = get_input(filename)
    possible = 0
    for i in range(len(triangles) // 3):
        for j in range(3):
            triangle = [triangles[3 * i][j], triangles[3 * i + 1][j], triangles[3 * i + 2][j]]
            triangle.sort()
            if triangle[0] + triangle[1] > triangle[2]:
                possible += 1
    return possible


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
