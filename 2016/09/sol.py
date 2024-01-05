#!/usr/bin/env python3
import time


def get_input(filename):
    f = open(filename, 'r').read()
    return f.split('\n')


def decompress_length(line):
    res = len(line)
    i = 0
    while i < len(line):
        c = line[i]
        if c == '(':
            par = line[i + 1:].find(')') + i + 1
            length, amount = int(line[i + 1:par].split('x')[0]), int(line[i + 1:par].split('x')[1])
            res += length * (amount - 1) - par - 1 + i
            i = par + length + 1
        else:
            i += 1
    return res


def decompress_length_2(line):
    res = len(line)
    i = 0
    while i < len(line):
        c = line[i]
        if c == '(':
            par = line[i + 1:].find(')') + i + 1
            length, amount = int(line[i + 1:par].split('x')[0]), int(line[i + 1:par].split('x')[1])
            res += decompress_length_2(line[par + 1:par + length + 1]) * amount - length - par - 1 + i
            i = par + length + 1
        else:
            i += 1
    return res


def sol1(filename):
    lines = get_input(filename)
    res = 0
    for line in lines:
        res += decompress_length(line)
    return res


def sol2(filename):
    lines = get_input(filename)
    res = 0
    for line in lines:
        res += decompress_length_2(line)
    return res


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
