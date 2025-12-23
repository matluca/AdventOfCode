#!/usr/bin/env python3

def get_input(filename):
    jump_offsets = []
    f = open(filename, 'r')
    for line in f.readlines():
        jump_offsets.append(int(line.strip()))
    f.close()
    return jump_offsets


def next_jump(jump_offsets, position):
    new_position = position + jump_offsets[position]
    jump_offsets[position] += 1
    return jump_offsets, new_position


def find_steps(jump_offsets, next_jump_func):
    position = 0
    i = 0
    while 0 <= position < len(jump_offsets):
        i += 1
        jump_offsets, position = next_jump_func(jump_offsets, position)
    return i


def sol1(filename):
    jump_offsets = get_input(filename)
    return find_steps(jump_offsets, next_jump)


def next_jump_2(jump_offsets, position):
    new_position = position + jump_offsets[position]
    if jump_offsets[position] < 3:
        jump_offsets[position] += 1
    else:
        jump_offsets[position] -= 1
    return jump_offsets, new_position


def sol2(filename):
    jump_offsets = get_input(filename)
    return find_steps(jump_offsets, next_jump_2)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
