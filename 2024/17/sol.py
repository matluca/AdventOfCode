#!/usr/bin/env python3

import time


def get_input(filename):
    f = open(filename, 'r')
    registers_raw, program_raw = f.read().strip().split('\n\n')
    f.close()
    registers = [int(rr.split(': ')[1]) for rr in registers_raw.split('\n')]
    program = [int(x) for x in program_raw.split(': ')[1].split(',')]
    return registers, program


def combo(operand, registers):
    if operand <= 3:
        return operand
    if operand <= 6:
        return registers[operand - 4]


def process(registers, program, instruction_pointer, out):
    opcode = program[instruction_pointer]
    operand = program[instruction_pointer + 1]
    combo_operand = combo(operand, registers)
    if opcode == 0:
        registers[0] = int(registers[0] / 2 ** combo_operand)
    elif opcode == 1:
        registers[1] = registers[1] ^ operand
    elif opcode == 2:
        registers[1] = combo_operand % 8
    elif opcode == 3 and registers[0] != 0:
        instruction_pointer = operand
        return registers, instruction_pointer, out
    elif opcode == 4:
        registers[1] = registers[1] ^ registers[2]
    elif opcode == 5:
        out.append(combo_operand % 8)
    elif opcode == 6:
        registers[1] = int(registers[0] / 2 ** combo_operand)
    elif opcode == 7:
        registers[2] = int(registers[0] / 2 ** combo_operand)
    instruction_pointer += 2
    return registers, instruction_pointer, out


def output(registers, program):
    instruction_pointer = 0
    out = []
    while instruction_pointer < len(program):
        registers, instruction_pointer, out = process(registers, program, instruction_pointer, out)
    return out


def sol1(filename):
    registers, program = get_input(filename)
    return ','.join([str(x) for x in output(registers, program)])


def sol2(filename):
    registers, program = get_input(filename)
    possibilities = {0: [x for x in range(8)]}
    for exponent in range(1, len(program)):
        possibilities[exponent] = []
        for p in possibilities[exponent - 1]:
            for q in range(8):
                if p == 0:
                    continue
                ra = 8 * p + q
                registers[0] = ra
                out = output(registers, program)
                l = len(out)
                if out == program[len(program) - l:]:
                    possibilities[exponent].append(ra)
                if out == program:
                    return ra


if __name__ == '__main__':
    start_time = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test1.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    end1_time = time.time()
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    end2_time = time.time()
    print(
        f'Part 1: {end1_time - start_time:.3f}s, Part 2: {end2_time - end1_time:.3f}s, Tot: {end2_time - start_time:.3f}s')
