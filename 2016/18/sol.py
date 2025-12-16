#!/usr/bin/env python3
import time


def get_input(filename):
    f = open(filename, 'r')
    raw = f.read()
    f.close()
    return raw.strip()


def next_line(line, size):
    line_dict = {-1: '.', size: '.'}
    for i, c in enumerate(line):
        line_dict[i] = c
    nl = ''
    for i in range(size):
        abc = ''.join([line_dict[j] for j in range(i - 1, i + 2)])
        if abc in ['^^.', '.^^', '^..', '..^']:
            nl += '^'
        else:
            nl += '.'
    return nl


def n_safe(line):
    return sum([c == '.' for c in line])


def sol(filename, n_rows):
    line = get_input(filename)
    size = len(line)
    tot = n_safe(line)
    for i in range(n_rows - 1):
        line = next_line(line, size)
        tot += n_safe(line)
    return tot


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol("test.txt", 10)}')
    print(f'Solution: {sol("input.txt", 40)}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Solution: {sol("input.txt", 400000)}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
