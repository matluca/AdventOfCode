#!/usr/bin/env python3
import math


def get_input(filename):
    f = open(filename, 'r').read()
    n = int(f)
    return n


def presents(n):
    s = 0
    for d in range(1, int(math.sqrt(n)) + 1):
        if n % d == 0:
            s += (d + n / d) * 10
    return s


def presents_2(n):
    s = 0
    for d in range(1, int(math.sqrt(n)) + 1):
        if n % d == 0:
            if n / d <= 50:
                s += d * 11
            if d < 50:
                s += n / d * 11
    return s


def sol1(filename):
    target = get_input(filename)
    found = False
    n = 0
    while not found:
        n += 1
        s = presents(n)
        if s >= target:
            found = True
    return n


def sol1_input(filename):
    target = get_input(filename)
    found = False
    step = 1000
    n = 0
    while not found:
        n += step
        s = presents(n)
        if s > target / 2:
            step = 1
        if s >= target:
            found = True
    return n


def sol2_input(filename):
    target = get_input(filename)
    found = False
    step = 1000
    n = 0
    while not found:
        n += step
        s = presents_2(n)
        if s > target / 2:
            step = 1
        if s >= target:
            found = True
    return n


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1_input("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2_input("input.txt")}')
