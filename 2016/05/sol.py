#!/usr/bin/env python3
import time
import hashlib


def get_input(filename):
    f = open(filename, 'r').read()
    return f.strip()


def sol1(filename):
    door_id = get_input(filename)
    n = 0
    password = ''
    while len(password) < 8:
        n += 1
        h = hashlib.md5((door_id + str(n)).encode('utf-8')).hexdigest()
        if h[:5] == '00000':
            password += h[5]
    return password


def sol2(filename):
    door_id = get_input(filename)
    n = 0
    password = ['?'] * 8
    while '?' in password:
        n += 1
        h = hashlib.md5((door_id + str(n)).encode('utf-8')).hexdigest()
        if h[:5] == '00000' and h[5] in ['0', '1', '2', '3', '4', '5', '6', '7'] and password[int(h[5])] == '?':
            password[int(h[5])] = h[6]
    return ''.join(password)


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
