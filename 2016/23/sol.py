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
            if " " + l in instruction and l not in registers.keys():
                registers[l] = 0
    return registers, instructions


def toggle(instruction):
    verb = instruction.split()[0]
    if len(instruction.split()) == 2:
        if verb == 'inc':
            return instruction.replace('inc', 'dec')
        else:
            return instruction.replace(verb, 'inc')
    else:
        if verb == 'jnz':
            return instruction.replace('jnz', 'cpy')
        else:
            return instruction.replace(verb, 'jnz')


def apply(registers, instructions, position):
    if instructions[position:position + 3] == ["inc a", "dec c", "jnz c -2"]:
        registers['a'] += registers['c']
        registers['c'] = 0
        return registers, position + 3
    if instructions[position:position + 6] == ["cpy b c", "inc a", "dec c", "jnz c -2", "dec d", "jnz d -5"]:
        registers['a'] += registers['d'] * registers['b']
        registers['d'] = 0
        return registers, position + 6
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
            y_value = int(y)
        except ValueError:
            y_value = registers[y]
        try:
            if int(x) != 0:
                position += y_value
            else:
                position += 1
        except ValueError:
            if registers[x] != 0:
                position += y_value
            else:
                position += 1
    elif verb == 'tgl':
        idx_to_toggle = position + registers[instruction.split()[1]]
        if idx_to_toggle < len(instructions):
            instructions[idx_to_toggle] = toggle(instructions[idx_to_toggle])
        position += 1
    return registers, position


def sol1(filename):
    registers, instructions = get_input(filename)
    position = 0
    registers['a'] = 7
    while position < len(instructions):
        registers, position = apply(registers, instructions, position)
    return registers['a']


def sol2(filename):
    registers, instructions = get_input(filename)
    position = 0
    registers['a'] = 12
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
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
