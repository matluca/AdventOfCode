#!/usr/bin/env python3
import time


def get_input(filename):
    f = open(filename, 'r')
    instructions = [l.strip() for l in f.readlines()]
    f.close()
    return instructions


def swap(pwd_list, idx_1, idx_2):
    tmp = pwd_list[idx_1]
    pwd_list[idx_1] = pwd_list[idx_2]
    pwd_list[idx_2] = tmp
    return pwd_list


def apply_instruction(instruction, password):
    pwd_list = list(password)
    if instruction.startswith('swap position'):
        idx_1, idx_2 = int(instruction.split()[2]), int(instruction.split()[5])
        return ''.join(swap(pwd_list, idx_1, idx_2))
    if instruction.startswith('swap letter'):
        a, b =  instruction.split()[2], instruction.split()[5]
        idx_1, idx_2 = pwd_list.index(a), pwd_list.index(b)
        return ''.join(swap(pwd_list, idx_1, idx_2))
    if instruction.startswith('reverse'):
        idx_1, idx_2 = int(instruction.split()[2]), int(instruction.split()[4])
        return ''.join(pwd_list[:idx_1] + pwd_list[idx_1:idx_2 + 1][::-1] + pwd_list[idx_2 + 1:])
    if instruction.startswith('rotate left'):
        steps = int(instruction.split()[2])
        for step in range(steps):
            pwd_list = pwd_list[1:] + pwd_list[:1]
        return ''.join(pwd_list)
    if instruction.startswith('rotate right'):
        steps = int(instruction.split()[2])
        for step in range(steps):
            pwd_list = pwd_list[-1:] + pwd_list[:-1]
        return ''.join(pwd_list)
    if instruction.startswith('move position'):
        idx_1, idx_2 = int(instruction.split()[2]), int(instruction.split()[5])
        pwd_list.insert(idx_2, pwd_list.pop(idx_1))
        return ''.join(pwd_list)
    if instruction.startswith('rotate based on position of letter'):
        a = instruction.split()[6]
        idx = pwd_list.index(a)
        steps = 1 + idx
        if idx >= 4:
            steps += 1
        for step in range(steps):
            pwd_list = pwd_list[-1:] +pwd_list[:-1]
        return ''.join(pwd_list)
    return password


def sol1(filename, password):
    instructions = get_input(filename)
    for instruction in instructions:
        password = apply_instruction(instruction, password)
    return password


def revert_instruction(instruction, password):
    pwd_list = list(password)
    if instruction.startswith('swap') or instruction.startswith('reverse'):
        return apply_instruction(instruction, password)
    if instruction.startswith('rotate left'):
        return apply_instruction(instruction.replace("left", "right"), password)
    if instruction.startswith('rotate right'):
        return apply_instruction(instruction.replace("right", "left"), password)
    if instruction.startswith('move position'):
        idx_1, idx_2 = int(instruction.split()[2]), int(instruction.split()[5])
        pwd_list.insert(idx_1, pwd_list.pop(idx_2))
        return ''.join(pwd_list)
    if instruction.startswith('rotate based on position of letter'):
        new_pwd_list = pwd_list.copy()
        while True:
            new_pwd_list = new_pwd_list[1:] + new_pwd_list[:1]
            new_pwd = ''.join(new_pwd_list)
            if apply_instruction(instruction, new_pwd) == password:
                return new_pwd
    return password


def sol2(filename, password):
    instructions = get_input(filename)
    for instruction in instructions[::-1]:
        password = revert_instruction(instruction, password)
    return password


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", "abcde")}')
    print(f'Solution: {sol1("input.txt", "abcdefgh")}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt", "decab")}')
    print(f'Solution: {sol2("input.txt", "fbgdceah")}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
