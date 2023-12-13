#!/usr/bin/env python3
import math


def get_input(filename):
    t, d = open(filename, 'r').readlines()
    times = [int(n) for n in t.split(': ')[1].strip().split(' ') if n != '']
    distances = [int(n) for n in d.split(': ')[1].strip().split(' ') if n != '']
    return times, distances


def sol1(filename):
    times, distances = get_input(filename)
    res = 1
    for race in range(len(times)):
        z1 = math.floor((times[race] - math.sqrt(times[race] * times[race] - 4 * distances[race])) / 2)
        z2 = math.ceil((times[race] + math.sqrt(times[race] * times[race] - 4 * distances[race])) / 2) - 1
        res *= (z2 - z1)
    return res


def sol2(filename):
    times, distances = get_input(filename)
    time = int(''.join([str(t) for t in times]))
    distance = int(''.join([str(d) for d in distances]))
    z1 = math.floor((time - math.sqrt(time * time - 4 * distance)) / 2)
    z2 = math.ceil((time + math.sqrt(time * time - 4 * distance)) / 2) - 1
    return z2 - z1


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
