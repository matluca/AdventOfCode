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


def apply(instruction, pos, registers, output, rcv, part, counter):
    verb = instruction.split()[0]
    if verb == 'snd':
        output.append(get(instruction.split()[1], registers))
        if counter is not None:
            counter += 1
    elif verb == 'set':
        registers[instruction.split()[1]] = get(instruction.split()[2], registers)
    elif verb == 'add':
        registers[instruction.split()[1]] += get(instruction.split()[2], registers)
    elif verb == 'mul':
        registers[instruction.split()[1]] *= get(instruction.split()[2], registers)
    elif verb == 'mod':
        registers[instruction.split()[1]] %= get(instruction.split()[2], registers)
    elif verb == 'rcv':
        if (len(output) == 0 and part == 1) or (len(rcv) == 0 and part == 2):
            return registers, output, pos, rcv, counter
        if registers[instruction.split()[1]] != 0 and part == 1:
            rcv.append(output.pop())
        if part == 2:
            registers[instruction.split()[1]] = rcv.pop(0)
    elif verb == 'jgz':
        if get(instruction.split()[1], registers) > 0:
            pos += get(instruction.split()[2], registers) - 1
    pos += 1
    return registers, output, pos, rcv, counter


def sol1(filename):
    registers, instructions = get_input(filename)
    output = []
    rcv = []
    pos = 0
    while True:
        registers, output, pos, rcv, _ = apply(instructions[pos], pos, registers, output, rcv, 1, None)
        if len(rcv) > 0:
            return rcv[0]


def sol2(filename):
    registers, instructions = get_input(filename)
    prog = [registers.copy(), registers.copy()]
    prog[0]['p'] = 0
    prog[1]['p'] = 1
    inp = [[], []]
    pos = [0, 0]
    tot = 0
    while not (len(inp[0]) == 0 and len(inp[1]) == 0 and instructions[pos[0]].startswith('rcv') and instructions[pos[1]].startswith('rcv')):
        prog[0], inp[1], pos[0], inp[0], _ = apply(instructions[pos[0]], pos[0], prog[0], inp[1], inp[0], 2, None)
        prog[1], inp[0], pos[1], inp[1], tot = apply(instructions[pos[1]], pos[1], prog[1], inp[0], inp[1], 2, tot)
    return tot


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
