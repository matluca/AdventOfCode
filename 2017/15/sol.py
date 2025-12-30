#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    starting_values = []
    for line in f.readlines():
        starting_values.append(int(line.strip().split()[-1]))
    f.close()
    return starting_values


def sol1(filename):
    starting_values = get_input(filename)
    a, b = starting_values[0], starting_values[1]
    tot = 0
    for i in range(40000000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        if a % (2 ** 16) == b % (2 ** 16):
            tot += 1
    return tot


def sol2(filename):
    starting_values = get_input(filename)
    a, b = starting_values[0], starting_values[1]
    tot = 0
    for i in range(5000000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        while a % 4 != 0:
            a = (a * 16807) % 2147483647
        while b % 8 != 0:
            b = (b * 48271) % 2147483647
        if a % (2 ** 16) == b % (2 ** 16):
            tot += 1
    return tot


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
