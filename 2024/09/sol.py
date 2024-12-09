#!/usr/bin/env python3

import time


def get_input(filename):
    f = open(filename, 'r')
    disk_map = [int(x) for x in f.read().strip()]
    f.close()
    return disk_map


def build_blocks(checksum):
    blocks = []
    for i in range(len(checksum)):
        if i % 2 == 0:
            n = checksum[i]
            for j in range(n):
                blocks.append(int(i / 2))
        else:
            n = checksum[i]
            for j in range(n):
                blocks.append(None)
    return blocks


def sol1(filename):
    disk_map = get_input(filename)
    blocks = build_blocks(disk_map)
    idx = 0
    checksum = 0
    while idx < len(blocks):
        if blocks[idx] is not None:
            checksum += idx * blocks[idx]
        else:
            if blocks[-1] is None:
                blocks = blocks[:-1]
                continue
            checksum += idx * blocks[-1]
            blocks = blocks[:-1]
        idx += 1
    return checksum


def compact_blocks(disk_map, blocks):
    str_blocks = "".join([str(x) + ',' if x is not None else '.,' for x in blocks])
    right_idx = len(disk_map) - 1
    while right_idx > 0:
        length = disk_map[right_idx]
        value = int(right_idx / 2)
        until = str_blocks.find(str(value))
        if "".join(['.,'] * length) in str_blocks[:until]:
            str_blocks = str_blocks.replace("".join([str(value) + ','] * length), "".join(['.,'] * length), 1)
            str_blocks = str_blocks.replace("".join(['.,'] * length), "".join([str(value) + ','] * length), 1)
        right_idx -= 2
    blocks_new = []
    i = 0
    checksum = 0
    real_i = 0
    l = len(str_blocks)
    while i < len(str_blocks):
        if str_blocks[i] == '.':
            blocks_new.append(None)
            i += 1
            real_i += 1
        if str_blocks[i] == ',':
            i += 1
            continue
        else:
            checksum += real_i * int(str_blocks[i:].split(',')[0])
            real_i += 1
            i += len(str_blocks[i:].split(',')[0])
    return checksum


def sol2(filename):
    disk_map = get_input(filename)
    blocks = build_blocks(disk_map)
    return compact_blocks(disk_map, blocks)


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    end1 = time.time()
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    end2 = time.time()
    print(f'Part 1: {end1 - start:.3f}s, Part 2: {end2 - end1:.3f}s, Tot: {end2 - start:.3f}s')
