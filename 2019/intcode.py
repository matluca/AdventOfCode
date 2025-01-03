def get_n_parameters(opcode):
    if opcode in [1, 2, 7, 8]:
        return 3
    if opcode in [5, 6]:
        return 2
    if opcode in [3, 4]:
        return 1
    if opcode in [99]:
        return 0


def decode_opcode(program, pointer):
    opcode = program[pointer] % 100
    n_parameters = get_n_parameters(opcode)
    modes = [0] * n_parameters
    r = program[pointer] // 100
    i = 0
    while r > 0:
        modes[i] = r % 10
        r = r // 10
        i += 1
    return opcode, modes


def value(program, pointer, mode):
    if mode == 0:
        return program[program[pointer]]
    return program[pointer]


def add(program, pointer, modes):
    program[program[pointer + 3]] = value(program, pointer + 1, modes[0]) + value(program, pointer + 2, modes[1])
    return program, pointer + 4


def mul(program, pointer, modes):
    program[program[pointer + 3]] = value(program, pointer + 1, modes[0]) * value(program, pointer + 2, modes[1])
    return program, pointer + 4


def inp(program, pointer, input_value):
    program[program[pointer + 1]] = input_value
    return program, pointer + 2


def out(program, pointer, modes, outputs):
    outputs.append(value(program, pointer + 1, modes[0]))
    return program, pointer + 2, outputs


def jump_if_true(program, pointer, modes):
    if value(program, pointer + 1, modes[0]) != 0:
        return program, value(program, pointer + 2, modes[1])
    return program, pointer + 3


def jump_if_false(program, pointer, modes):
    if value(program, pointer + 1, modes[0]) == 0:
        return program, value(program, pointer + 2, modes[1])
    return program, pointer + 3


def less_then(program, pointer, modes):
    if value(program, pointer + 1, modes[0]) < value(program, pointer + 2, modes[1]):
        program[program[pointer + 3]] = 1
    else:
        program[program[pointer + 3]] = 0
    return program, pointer + 4


def equals(program, pointer, modes):
    if value(program, pointer + 1, modes[0]) == value(program, pointer + 2, modes[1]):
        program[program[pointer + 3]] = 1
    else:
        program[program[pointer + 3]] = 0
    return program, pointer + 4


def run(program, input_value=None):
    pointer = 0
    outputs = []
    while True:
        opcode, modes = decode_opcode(program, pointer)
        if opcode == 99:
            return program, outputs
        elif opcode == 1:
            program, pointer = add(program, pointer, modes)
        elif opcode == 2:
            program, pointer = mul(program, pointer, modes)
        elif opcode == 3:
            program, pointer = inp(program, pointer, input_value)
        elif opcode == 4:
            program, pointer, outputs = out(program, pointer, modes, outputs)
        elif opcode == 5:
            program, pointer = jump_if_true(program, pointer, modes)
        elif opcode == 6:
            program, pointer = jump_if_false(program, pointer, modes)
        elif opcode == 7:
            program, pointer = less_then(program, pointer, modes)
        elif opcode == 8:
            program, pointer = equals(program, pointer, modes)