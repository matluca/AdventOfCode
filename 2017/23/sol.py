#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    registers = {}
    instructions = []
    for line in f.readlines():
        instr = line.strip()
        instructions.append(instr)
        if 'a' <= instr.split()[1] <= 'z':
            registers[instr.split()[1]] = 0
        if len(instr.split()) == 3 and 'a' <= instr.split()[2] <= 'z':
            registers[instr.split()[2]] = 0
    f.close()
    return registers, instructions


def get(x, registers):
    try:
        return int(x)
    except ValueError:
        return registers[x]


def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def apply(instructions, pos, registers, counter):
    if pos == 10 and registers['a'] == 1:
        if not prime(registers['b']):
            registers['f'] = 0
        registers['g'] = 0
        registers['d'] = registers['b']
        registers['e'] = registers['b']
        return registers, 23, counter
    instruction = instructions[pos]
    print(pos, instruction, registers)
    verb = instruction.split()[0]
    if verb == 'set':
        registers[instruction.split()[1]] = get(instruction.split()[2], registers)
    elif verb == 'sub':
        registers[instruction.split()[1]] -= get(instruction.split()[2], registers)
    elif verb == 'mul':
        if counter is not None:
            counter += 1
        registers[instruction.split()[1]] *= get(instruction.split()[2], registers)
    elif verb == 'jnz':
        if get(instruction.split()[1], registers) != 0:
            pos += get(instruction.split()[2], registers) - 1
    pos += 1
    return registers, pos, counter


def sol1(filename):
    registers, instructions = get_input(filename)
    pos = 0
    counter = 0
    while 0 <= pos < len(instructions):
        registers, pos, counter = apply(instructions, pos, registers, counter)
    return counter


def sol2(filename):
    registers, instructions = get_input(filename)
    registers['a'] = 1
    pos = 0
    counter = None
    while 0 <= pos < len(instructions):
        registers, pos, counter = apply(instructions, pos, registers, counter)
    return registers['h']


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
