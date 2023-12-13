#!/usr/bin/env python3
import math


def get_input(filename):
    f = open(filename, 'r')
    data = []
    for line in f.readlines():
        data.append(list(line.strip()))
    f.close()
    return data


def get_asteroids(data):
    asteroids = set()
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                asteroids.add((j, i))
    return asteroids


def ang(p1, p2):
    tan = math.atan2(p2[0]-p1[0], p2[1]-p1[1])
    if tan < 0:
        return tan + 2*math.pi


def dist(p1, p2):
    return (p2[1]-p1[1])*(p2[1]-p1[1]) + (p2[0]-p1[0])*(p2[0]-p1[0])


def see(as1, asteroids):
    angles = set()
    for ast in asteroids:
        if ast == as1:
            continue
        angles.add(ang(as1, ast))
    return len(angles)


def order(as1, asteroids):
    by_angle = {}
    for ast in asteroids:
        if ast == as1:
            continue
        a = ang(as1, ast)
        if a not in by_angle.keys():
            by_angle[a] = []
        by_angle[a].append(dist(as1, ast))
    for k in by_angle.keys():
        by_angle[k].sort()


def sol1(filename):
    data = get_input(filename)
    asteroids = get_asteroids(data)
    max_see = 0
    for a in asteroids:
        see_ast = see(a, asteroids)
        if see_ast > max_see:
            max_see = see_ast
    return max_see


def sol2(filename):
    _ = get_input(filename)
    return 0


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Test: {sol1("test2.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    # print(f'Test: {sol2("test.txt")}')
    # print(f'Solution: {sol2("input.txt")}')
