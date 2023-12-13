#!/usr/bin/env python3
import hashlib


def get_input(filename):
    f = open(filename, 'r').read()
    return f


def sol(filename, zeroes):
    inp = get_input(filename)
    n = 1
    while True:
        s = inp + str(n)
        h = hashlib.md5(s.encode("utf-8")).hexdigest()
        if h[:zeroes] == '0' * zeroes:
            break
        n += 1
    return n


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol("test.txt", 5)}')
    print(f'Solution: {sol("input.txt", 5)}')
    print('--- Part 2 ---')
    print(f'Solution: {sol("input.txt", 6)}')
