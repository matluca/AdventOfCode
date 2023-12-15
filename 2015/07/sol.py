#!/usr/bin/env python3


def get_input(filename):
    f = open(filename, 'r').read()
    return f.split('\n')


def get_value(inst_dict, label, values):
    if label in values:
        return values[label]
    if label.isnumeric():
        return int(label)
    operation = inst_dict[label]
    if operation.isnumeric():
        values[label] = int(operation)
    elif operation.islower():
        values[label] = get_value(inst_dict, operation, values)
    elif operation.startswith('NOT'):
        values[label] = 2**16 - get_value(inst_dict, operation.split(' ')[1], values) - 1
    else:
        a, op, b = operation.split(' ')
        if op == 'AND':
            values[label] = get_value(inst_dict, a, values) & get_value(inst_dict, b, values)
        elif op == 'OR':
            values[label] = get_value(inst_dict, a, values) | get_value(inst_dict, b, values)
        elif op == 'LSHIFT':
            values[label] = get_value(inst_dict, a, values) << get_value(inst_dict, b, values)
        elif op == 'RSHIFT':
            values[label] = get_value(inst_dict, a, values) >> get_value(inst_dict, b, values)
    return values[label]


def sol1(filename, label):
    instructions = get_input(filename)
    inst_dict = {}
    for inst in instructions:
        target = inst.split(' -> ')[1]
        operation = inst.split(' -> ')[0]
        inst_dict[target] = operation
    values = {}
    return get_value(inst_dict, label, values)


def sol2(filename):
    instructions = get_input(filename)
    inst_dict = {}
    for inst in instructions:
        target = inst.split(' -> ')[1]
        operation = inst.split(' -> ')[0]
        inst_dict[target] = operation
    values = {}
    v = get_value(inst_dict, 'a', values)
    values = {'b': v}
    return get_value(inst_dict, 'a', values)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", "i")}')
    print(f'Solution: {sol1("input.txt", "a")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
