#!/usr/bin/env python3
import math

def get_input(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    instr_pointer = int(lines[0].strip().split()[1])
    instructions = []
    for line in lines[1:]:
        instr = line.split()[0]
        values = [int(x) for x in line.strip().split()[1:]]
        a, b, c = values
        instructions.append((instr, a, b, c))
    return instr_pointer, instructions


def apply(instr, registers, a, b, c):
    if instr == 'addr':
        registers[c] = registers[a] + registers[b]
    elif instr == 'addi':
        registers[c] = registers[a] + b
    elif instr == 'mulr':
        registers[c] = registers[a] * registers[b]
    elif instr == 'muli':
        registers[c] = registers[a] * b
    elif instr == 'banr':
        registers[c] = registers[a] & registers[b]
    elif instr == 'bani':
        registers[c] = registers[a] & b
    elif instr == 'borr':
        registers[c] = registers[a] | registers[b]
    elif instr == 'bori':
        registers[c] = registers[a] | b
    elif instr == 'setr':
        registers[c] = registers[a]
    elif instr == 'seti':
        registers[c] = a
    elif instr == 'gtir':
        registers[c] = 1 if a > registers[b] else 0
    elif instr == 'gtri':
        registers[c] = 1 if registers[a] > b else 0
    elif instr == 'gtrr':
        registers[c] = 1 if registers[a] > registers[b] else 0
    elif instr == 'eqir':
        registers[c] = 1 if a == registers[b] else 0
    elif instr == 'eqri':
        registers[c] = 1 if registers[a] == b else 0
    elif instr == 'eqrr':
        registers[c] = 1 if registers[a] == registers[b] else 0


def sol1(filename):
    instr_pointer, instructions = get_input(filename)
    registers = [0] * 6
    while 0 <= registers[instr_pointer] < len(instructions):
        instr, a, b, c = instructions[registers[instr_pointer]]
        apply(instr, registers, a, b, c)
        registers[instr_pointer] += 1
    return registers[0]


def sum_of_divisors(n):
    tot = 0
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            tot += i + n // i
    return tot


def sol2(filename):
    instr_pointer, instructions = get_input(filename)
    registers = [0] * 6
    registers[0] = 1
    while 0 <= registers[instr_pointer] < len(instructions):
        instr, a, b, c = instructions[registers[instr_pointer]]
        # instructions 2 - 15 are a double loop extracting the sum of divisors of registers[2] - input specific
        if registers[instr_pointer] == 2:
            registers[0] += sum_of_divisors(registers[2])
            registers[instr_pointer] = 15
        apply(instr, registers, a, b, c)
        registers[instr_pointer] += 1
    return registers[0]


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')

# 10551433 too low