#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    raw = f.read()
    f.close()
    part1_raw = raw.split('\n\n\n\n')[0]
    samples = []
    for sample_raw in part1_raw.split('\n\n'):
        before = [int(x) for x in sample_raw.split('\n')[0].split('[')[1].split(']')[0].split(',')]
        instruction = [int(x) for x in sample_raw.split('\n')[1].split()]
        after = [int(x) for x in sample_raw.split('\n')[2].split('[')[1].split(']')[0].split(',')]
        samples.append((before, instruction, after))
    program = []
    if len(raw.split('\n\n\n\n')) > 1:
        program_raw = raw.split('\n\n\n\n')[1]
        for line in program_raw.split('\n'):
            program.append([int(x) for x in line.split()])
    return samples, program


instrs = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr',
          'eqir', 'eqri', 'eqrr']


def apply(instr, input_registers, a, b, c):
    registers = input_registers.copy()
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
    return registers


def sol1(filename):
    samples, _ = get_input(filename)
    tot = 0
    for sample in samples:
        before, instruction, after = sample
        before_registers = {i: before[i] for i in range(4)}
        valid = 0
        for instr in instrs:
            after_registers = apply(instr, before_registers, instruction[1], instruction[2], instruction[3])
            if after == [after_registers[i] for i in range(4)]:
                valid += 1
        if valid >= 3:
            tot += 1
    return tot


def sol2(filename):
    samples, program = get_input(filename)
    valid = {i: set(instrs.copy()) for i in range(len(instrs))}
    for sample in samples:
        before, instruction, after = sample
        before_registers = {i: before[i] for i in range(4)}
        valid_instr = set()
        for instr in instrs:
            after_registers = apply(instr, before_registers, instruction[1], instruction[2], instruction[3])
            if after == [after_registers[i] for i in range(4)]:
                valid_instr.add(instr)
        valid[instruction[0]] &= valid_instr
    solution = {}
    while len(solution) < len(instrs):
        key, value = None, None
        for k, v in valid.items():
            if len(v) == 1:
                key = k
                value = list(v)[0]
                break
        solution[key] = value
        del valid[key]
        for k in valid.keys():
            if value in valid[k]:
                valid[k].remove(value)
    registers = {i: 0 for i in range(10)}
    for line in program:
        if len(line) == 0:
            continue
        instr = solution[line[0]]
        a, b, c = line[1], line[2], line[3]
        registers = apply(instr, registers, a, b, c)
    return registers[0]


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
