#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r').read()
    row, column = f.strip().split(', ')
    return int(row), int(column)


def next_spot(r, c):
    if r > 1:
        return r - 1, c + 1
    else:
        return c + 1, 1


def sol1(filename):
    row, column = get_input(filename)
    code = 20151125
    r, c = 1, 1
    while (r, c) != (row, column):
        r, c = next_spot(r, c)
        code = (code * 252533) % 33554393
    return code


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
