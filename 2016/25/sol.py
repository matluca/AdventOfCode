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


def apply(registers, instructions, position, output):
    if instructions[position:position + 3] == ["inc d", "dec b", "jnz b -2"]:
        registers['d'] += registers['b']
        registers['b'] = 0
        return registers, position + 3, output
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
    elif verb == 'out':
        x = instruction.split()[1]
        try:
            v = int(x)
        except ValueError:
            v = registers[x]
        output.append(v)
        position += 1
    return registers, position, output


def sol1(filename):
    registers_original, instructions = get_input(filename)
    print(2534, bin(2534))
    x = int('101010101010', 2)
    print(x, bin(x))
    for i in range(x - 2 - 2534, x + 3 - 2534):
        registers = registers_original.copy()
        registers['a'] = i
        position = 0
        output = []
        while position < len(instructions) and len(output) < 15:
            registers, position, output = apply(registers, instructions, position, output)
        print(i, output)
    return x - 2534


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
