#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    rotations_raw = f.readlines()
    f.close()
    rotations = []
    for rr in rotations_raw:
        rotations.append((rr[0], int(rr[1:])))
    return rotations


def apply_rotation(position, rotation):
    if rotation[0] == 'L':
        new_position = (position - rotation[1]) % 100
        rounds = abs((position - rotation[1]) // 100)
    else:
        new_position = (position + rotation[1]) % 100
        rounds = (position + rotation[1]) // 100
    if position == 0 and rotation[0] == 'L':
        rounds -= 1
    if new_position == 0 and rotation[0] == 'L':
        rounds += 1
    return new_position, rounds


def sol1(filename):
    rotations = get_input(filename)
    pos = 50
    tot = 0
    for rotation in rotations:
        pos, _ = apply_rotation(pos, rotation)
        if pos == 0:
            tot += 1
    return tot


def sol2(filename):
    rotations = get_input(filename)
    pos = 50
    tot = 0
    for rotation in rotations:
        pos, rounds = apply_rotation(pos, rotation)
        tot += rounds
    return tot


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')