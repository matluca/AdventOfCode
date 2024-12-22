#!/usr/bin/env python3
import time


def get_input(filename):
    f = open(filename, 'r')
    secrets = [int(x) for x in f.readlines()]
    f.close()
    return secrets


def mix(value, secret):
    return value ^ secret


def prune(secret):
    return secret % 16777216


def next_secret(secret):
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret


def sol1(filename):
    secrets = get_input(filename)
    tot = 0
    for secret in secrets:
        for i in range(2000):
            secret = next_secret(secret)
        tot += secret
    return tot


def find_sub_list(sl, l):
    for i in range(len(l) - 4):
        if l[i:i + 4] == sl:
            return i + 4


def find_tot_bananas(sublist, diffs, bananas):
    tot = 0
    for i, diff in enumerate(diffs):
        x = find_sub_list(sublist, diff)
        if x is not None:
            tot += bananas[i][x]
    return tot


def sol2(filename):
    secrets = get_input(filename)
    bananas = []
    diffs = []
    for i, secret in enumerate(secrets):
        bananas.append([])
        diffs.append([])
        for j in range(2000):
            secret = next_secret(secret)
            bananas[i].append((secret % 10))
            if j > 0:
                diffs[i].append(bananas[i][-1] - bananas[i][-2])
    max_bananas = 0
    subs = []
    seen = set()
    for i, diff in enumerate(diffs):
        for j in range(len(diff) - 4):
            subl = diff[j: j + 4]
            if tuple(subl) in seen:
                continue
            seen.add(tuple(subl))
            print(i, j, subl, max_bananas)
            bananas_sold = find_tot_bananas(subl, diffs, bananas)
            if bananas_sold > max_bananas:
                max_bananas = bananas_sold
                subs = subl
    return max_bananas, subs


if __name__ == '__main__':
    start_time = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    end1_time = time.time()
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    end2_time = time.time()
    print(
        f'Part 1: {end1_time - start_time:.3f}s, Part 2: {end2_time - end1_time:.3f}s, Tot: {end2_time - start_time:.3f}s')
