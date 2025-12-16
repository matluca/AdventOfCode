#!/usr/bin/env python3
import time


def get_input(filename):
    f = open(filename, 'r')
    disks = []
    for line in f.readlines():
        positions, offset = int(line.split()[3]), int(line.split()[-1][:-1])
        disks.append((positions, offset))
    f.close()
    return disks


def sol(disks):
    crts = []
    for i, disk in enumerate(disks):
        crts.append(((-disk[1] - i - 1) % disk[0], disk[0]))
    mcm = 1
    for crt in crts:
        mcm *= crt[1]
    for i in range(mcm // crts[0][1]):
        x = crts[0][0] + i * crts[0][1]
        solution = True
        for crt in crts[1:]:
            if x % crt[1] != crt[0]:
                solution = False
                break
        if solution:
            return x
    return 0

def sol1(filename):
    disks = get_input(filename)
    return sol(disks)


def sol2(filename):
    disks = get_input(filename)
    disks.append((11, 0))
    return sol(disks)


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
