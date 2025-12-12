#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    all_raw = f.read().split('\n\n')
    regions = all_raw[-1]
    f.close()
    return regions


def sol1(filename):
    regions = get_input(filename)
    tot = 0
    for region in regions.split('\n'):
        if region.strip() == '':
            continue
        a, b = int(region.split(':')[0].split('x')[0]), int(region.split(':')[0].split('x')[1])
        n_tiles = sum([int(n) for n in region.split(':')[1].split()])
        if 9*n_tiles <= a*b:
            tot += 1
    return tot


def sol2(filename):
    _ = get_input(filename)
    return 0


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
