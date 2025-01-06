#!/usr/bin/env python3
import re
import math


def get_input(filename):
    f = open(filename, 'r')
    regex = '<x=(-?\d+), y=(-?\d+), z=(-?\d+)>'
    moons = re.findall(regex, f.read().strip())
    f.close()
    return moons


def apply_gravity(p, v):
    for i in range(len(p)):
        for j in range(i, len(p)):
            for d in range(3):
                if p[i][d] < p[j][d]:
                    v[i][d] += 1
                    v[j][d] -= 1
                if p[i][d] > p[j][d]:
                    v[i][d] -= 1
                    v[j][d] += 1
    return v


def move(p, v):
    v = apply_gravity(p, v)
    for i in range(len(p)):
        for d in range(3):
            p[i][d] += v[i][d]
    return p, v


def energy(p, v):
    e = 0
    for i in range(len(p)):
        pot = abs(p[i][0]) + abs(p[i][1]) + abs(p[i][2])
        kin = abs(v[i][0]) + abs(v[i][1]) + abs(v[i][2])
        e += pot * kin
    return e


def sol1(filename, steps):
    positions_tuples = get_input(filename)
    positions = []
    for i, p in enumerate(positions_tuples):
        positions.append([int(x) for x in list(p)])
    velocities = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(steps):
        positions, velocities = move(positions, velocities)
    return energy(positions, velocities)


def sol2(filename):
    positions_tuples = get_input(filename)
    positions = []
    for i, p in enumerate(positions_tuples):
        positions.append([int(x) for x in list(p)])
    velocities = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    visited = [dict(), dict(), dict()]
    steps = 0
    cycles = [0, 0, 0]
    while 0 in cycles:
        positions, velocities = move(positions, velocities)
        status = [(), (), ()]
        for i in range(len(positions)):
            for d in range(3):
                status[d] += (positions[i][d], velocities[i][d])
        for d in range(3):
            if (status[d] in visited[d].keys()) and cycles[d] == 0:
                cycles[d] = visited[d][status[d]] - steps
            else:
                visited[d][status[d]] = steps
        steps += 1
    return math.lcm(*cycles)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 10)}')
    print(f'Solution: {sol1("input.txt", 1000)}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
