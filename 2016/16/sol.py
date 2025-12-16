#!/usr/bin/env python3
import time


def get_input(filename):
    f = open(filename, 'r')
    a = f.read().strip()
    f.close()
    return a


def dragon(a):
    b = a[::-1]
    b = ''.join([str((int(x) + 1) % 2) for x in b])
    return a + "0" + b


def checksum(value):
    cs = ''.join(str((int(value[i]) + int(value[i + 1]) + 1) % 2) for i in range(0, len(value), 2))
    if len(cs) % 2 == 1:
        return cs
    return checksum(cs)


def sol1(filename, size):
    a = get_input(filename)
    while len(a) < size:
        a = dragon(a)
    return checksum(a[:size])


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 20)}')
    print(f'Solution: {sol1("input.txt", 272)}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Solution: {sol1("input.txt", 35651584)}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
