#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    instructions = []
    for line in f:
        instructions.append(line.strip())
    f.close()
    return instructions


def apply_instruction(instructions, idx, a, b):
    instruction = instructions[idx]
    typ = instruction.split(' ')[0]
    var = instruction.split(' ')[1][0]
    next_idx = idx + 1
    if typ == 'hlf':
        if var == 'a':
            a = int(a / 2)
        else:
            b = int(b / 2)
    if typ == 'tpl':
        if var == 'a':
            a = a * 3
        else:
            b = b * 3
    if typ == 'inc':
        if var == 'a':
            a += 1
        else:
            b += 1
    if typ == 'jmp':
        next_idx = idx + int(instruction.split(' ')[1])
    if typ == 'jie':
        if var == 'a' and a % 2 == 0:
            next_idx = idx + int(instruction.split(', ')[1])
        if var == 'b' and b % 2 == 0:
            next_idx = idx + int(instruction.split(', ')[1])
    if typ == 'jio':
        if var == 'a' and a == 1:
            next_idx = idx + int(instruction.split(', ')[1])
        if var == 'b' and b == 1:
            next_idx = idx + int(instruction.split(', ')[1])
    return next_idx, a, b


def sol1(filename):
    instructions = get_input(filename)
    a, b = 0, 0
    idx = 0
    while 0 <= idx < len(instructions):
        idx, a, b = apply_instruction(instructions, idx, a, b)
    return a, b


def sol2(filename):
    instructions = get_input(filename)
    a, b = 1, 0
    idx = 0
    while 0 <= idx < len(instructions):
        idx, a, b = apply_instruction(instructions, idx, a, b)
    return a, b


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
