#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    instructions = []
    for line in f.readlines():
        instructions.append(line.strip())
    f.close()
    registers = {}
    for instruction in instructions:
        reg1, reg2 = instruction.split()[0], instruction.split()[4]
        registers[reg1] = 0
        registers[reg2] = 0
    return instructions, registers


def apply(instruction, registers):
    condition_raw = instruction.split("if ")[1]
    register = condition_raw.split()[0]
    check = condition_raw.split()[1]
    value = int(condition_raw.split()[2])
    condition = eval(f'{registers[register]} {check} {value}')
    if condition:
        verb = instruction.split()[1]
        if verb == "inc":
            registers[instruction.split()[0]] += int(instruction.split()[2])
        else:
            registers[instruction.split()[0]] -= int(instruction.split()[2])
    return registers


def sol1(filename):
    instructions, registers = get_input(filename)
    for instruction in instructions:
        registers = apply(instruction, registers)
    return max(registers.values())


def sol2(filename):
    instructions, registers = get_input(filename)
    max_value = 0
    for instruction in instructions:
        registers = apply(instruction, registers)
        max_value = max(max_value, max(registers.values()))
    return max_value


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
