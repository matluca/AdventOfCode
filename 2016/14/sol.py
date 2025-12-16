#!/usr/bin/env python3
import time
import hashlib


def get_input(filename):
    f = open(filename, 'r')
    salt = f.read().strip()
    f.close()
    return salt


def hash1(salt, n):
    return hashlib.md5((salt + str(n)).encode("utf-8")).hexdigest()


def hash2(salt, n):
    h = hash1(salt, n)
    for i in range(2016):
        h = hashlib.md5(h.encode("utf-8")).hexdigest()
    return h


def find_keys(filename, hash_func):
    salt = get_input(filename)
    hashes = [hash_func(salt, n) for n in range(1001)]
    n = 0
    keys = set()
    while len(keys) < 64:
        h = hashes[0]
        triple = ''
        for j in range(len(h) - 2):
            if h[j] == h[j + 1] and h[j] == h[j + 2]:
                triple = h[j]
                break
        if triple != '':
            for i, h2 in enumerate(hashes[1:]):
                if triple * 5 in h2:
                    keys.add(h)
                    break
        new_h = hash_func(salt, n + 1001)
        hashes = hashes[1:]
        hashes.append(new_h)
        n += 1
    return n - 1


def sol1(filename):
    return find_keys(filename, hash1)


def sol2(filename):
    return find_keys(filename, hash2)


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt",)}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
