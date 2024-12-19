#!/usr/bin/env python3
import math
from fractions import Fraction
from functools import cmp_to_key


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


def dist(p1, p2):
    return (p2[1] - p1[1]) * (p2[1] - p1[1]) + (p2[0] - p1[0]) * (p2[0] - p1[0])


def see(as1, asteroids):
    angles = set()
    for ast in asteroids:
        if ast == as1:
            continue
        angles.add(angle(as1, ast))
    return len(angles)


def compare_angle(a1, a2):
    f1, s1 = a1
    f2, s2 = a2
    if a1 == a2:
        return 0
    if s1 == 0 and f1 < 0:
        return -1
    if s2 == 0 and f2 < 0:
        return 1
    if s1 == 0 and s2 == 1:
        return 1
    if s1 == 0 and s2 == -1:
        return -1
    if s2 == 0 and s1 == 1:
        return -1
    if s2 == 0 and s1 == -1:
        return 1
    if s1 == s2 == 1:
        if f1 < f2:
            return -1
        else:
            return 1
    if s1 == s2 == -1:
        if f1 < f2:
            return -1
        else:
            return 1
    if s1 == 1:
        return -1
    if s2 == 1:
        return 1


def by_angle(as1, asteroids):
    by_ang = {}
    for ast in asteroids:
        if ast == as1:
            continue
        a = angle(as1, ast)
        if a not in by_ang.keys():
            by_ang[a] = []
        by_ang[a].append(dist(as1, ast))
    for k in by_ang.keys():
        by_ang[k].sort()
    return by_ang


def angle(p1, p2):
    if p2[0] == p1[0]:
        if p2[1] > p1[1]:
            return Fraction(10000, 1), 0
        return Fraction(-10000, 1), 0
    if p2[0] > p1[0]:
        sign = 1
    else:
        sign = -1
    return Fraction(p2[1] - p1[1], p2[0] - p1[0]), sign


def find_optimal(asteroids):
    max_see = 0
    best_ast = None
    for a in asteroids:
        see_ast = see(a, asteroids)
        if see_ast > max_see:
            max_see = see_ast
            best_ast = a
    return max_see, best_ast


def sol1(filename):
    data = get_input(filename)
    asteroids = get_asteroids(data)
    return find_optimal(asteroids)


def sol2(filename):
    data = get_input(filename)
    asteroids = get_asteroids(data)
    max_see, best_ast = find_optimal(asteroids)
    by_ang = by_angle(best_ast, asteroids)
    angles = list(by_ang.keys())
    angles.sort(key=cmp_to_key(compare_angle))
    n_asteroids = 0
    for a in angles:
        if len(by_ang[a]) > 0:
            distance = by_ang[a].pop(0)
            n_asteroids += 1
            if n_asteroids == 200:
                f, s = a
                if s == 0:
                    if f < 0:
                        return best_ast[0], best_ast[1] - distance
                    if f > 0:
                        return best_ast[0], best_ast[1] + distance
                rapp = distance / (f.numerator * f.numerator + f.denominator * f.denominator)
                if s > 0:
                    return int(100 * (best_ast[0] + math.sqrt(rapp) * f.denominator) + best_ast[1] + math.sqrt(
                        rapp) * f.numerator)
                else:
                    return int(100 * (best_ast[0] - math.sqrt(rapp) * f.denominator) + best_ast[1] - math.sqrt(
                        rapp) * f.numerator)
    return 0


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Test: {sol1("test2.txt")}')
    print(f'Test: {sol1("test3.txt")}')
    print(f'Test: {sol1("test4.txt")}')
    print(f'Test: {sol1("test5.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test5.txt")}')
    print(f'Solution: {sol2("input.txt")}')
