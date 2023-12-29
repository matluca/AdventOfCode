#!/usr/bin/env python3
import time
from collections import Counter


def get_input(filename):
    f = open(filename, 'r')
    inputs = []
    for line in f:
        rooms_raw, checksum_raw = line.strip().split('[')
        sector_id = int(rooms_raw.split('-')[-1])
        checksum = checksum_raw[:-1]
        rooms = rooms_raw.split('-')[:-1]
        inputs.append((rooms, sector_id, checksum))
    f.close()
    return inputs


def sol1(filename):
    inputs = get_input(filename)
    res = 0
    for inp in inputs:
        c = Counter(''.join(inp[0]))
        sorted_c = sorted(c.items(), key=lambda x: (x[1], -ord(x[0])), reverse=True)
        if inp[2] == ''.join([x[0] for x in sorted_c[:5]]):
            res += inp[1]
    return res


def sol2(filename):
    inputs = get_input(filename)
    for inp in inputs:
        decrypted_rooms = []
        rooms = inp[0]
        sector_id = inp[1]
        for room in rooms:
            decrypted_room = ''
            for c in room:
                decrypted_room += chr(ord('a') + (ord(c) + sector_id - ord('a')) % 26)
            decrypted_rooms.append(decrypted_room.replace('{', 'a'))
        if 'north' in ' '.join(decrypted_rooms):
            return sector_id


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
