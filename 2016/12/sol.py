#!/usr/bin/env python3
import time
import string


def get_input(filename):
    f = open(filename, 'r')
    instructions = []
    for line in f.readlines():
        instructions.append(line.strip())
    f.close()
    registers = {}
    for l in list(string.ascii_lowercase):
        for instruction in instructions:
            if " " + l + " " in instruction and l not in registers.keys():
                registers[l] = 0
    return registers, instructions


def apply(registers, instructions, position):
    if instructions[position] == "inc a" and instructions[position + 1] == "dec b" and instructions[position + 2] == "jnz b -2":
        registers['a'] += registers['b']
        registers['b'] = 0
        return registers, position + 3
    instruction = instructions[position]
    verb = instruction.split()[0]
    if verb == 'cpy':
        x, y = instruction.split()[1:3]
        try:
            registers[y] = int(x)
        except ValueError:
            registers[y] = registers[x]
        position += 1
    elif verb == 'inc':
        registers[instruction.split()[1]] += 1
        position += 1
    elif verb == 'dec':
        registers[instruction.split()[1]] -= 1
        position += 1
    elif verb == 'jnz':
        x, y = instruction.split()[1:3]
        try:
            if int(x) != 0:
                position += int(y)
            else:
                position += 1
        except ValueError:
            if registers[x] != 0:
                position += int(y)
            else:
                position += 1
    return registers, position


def sol1(filename):
    registers, instructions = get_input(filename)
    position = 0
    while position < len(instructions):
        registers, position = apply(registers, instructions, position)
    return registers['a']


def sol2(filename):
    registers, instructions = get_input(filename)
    registers['c'] = 1
    position = 0
    while position < len(instructions):
        registers, position = apply(registers, instructions, position)
    return registers['a']


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
