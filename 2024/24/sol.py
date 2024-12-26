#!/usr/bin/env python3

import time


def get_input(filename):
    f = open(filename, 'r')
    inputs_raw, gates_raw = f.read().strip().split('\n\n')
    f.close()
    inputs = {}
    for line in inputs_raw.split('\n'):
        inputs[line.split(':')[0]] = int(line.split(': ')[1])
    gates = []
    for line in gates_raw.split('\n'):
        a, op, b = line.split(' ')[0], line.split(' ')[1], line.split(' ')[2]
        target = line.split('-> ')[1]
        gates.append((a, b, op, target))
    return inputs, gates


def is_over(inputs, outputs):
    for output in outputs:
        if output not in inputs.keys():
            return False
    return True


def compute(inputs, gates):
    for gate in gates:
        a, b, op, target = gate
        if a not in inputs.keys() or b not in inputs.keys():
            continue
        if op == 'AND':
            inputs[target] = inputs[a] and inputs[b]
        elif op == 'OR':
            inputs[target] = inputs[a] or inputs[b]
        elif op == 'XOR':
            inputs[target] = inputs[a] ^ inputs[b]
    return inputs


def sol1(filename):
    inputs, gates = get_input(filename)
    outputs = [g[3] for g in gates if g[3].startswith('z')]
    while not is_over(inputs, outputs):
        inputs = compute(inputs, gates)
    result = [str(inputs[out]) for out in sorted(outputs)]
    result.reverse()
    return int(''.join(result), 2)


def label(letter, i):
    if i < 10:
        return f'{letter}0{i}'
    return f'{letter}{i}'


def find(gates, x, y, op):
    for gate in gates:
        a, b, o, t = gate
        if (((a == x) and (b == y)) or ((a == y) and (b == x))) and o == op:
            return gate
    return None


def find_partial(gates, x, op):
    for gate in gates:
        a, b, o, t = gate
        if ((a == x) or (b == x)) and o == op:
            return gate
    return None


def find_z(gates, z):
    for gate in gates:
        a, b, o, t = gate
        if t == z and o == 'XOR':
            return gate
    return None


def find_c(gates, c):
    for gate in gates:
        a, b, o, t = gate
        if t == c and o == 'OR':
            return gate
    return None


def sol2(filename):
    inputs, gates = get_input(filename)
    size_n = int(len(inputs) / 2)
    mapping = {find(gates, 'x00', 'y00', 'AND')[3]: 'c01'}
    exchange = []
    for i in range(1, size_n):
        x, y, c = label('x', i), label('y', i), label('c', i)
        and_gate = find(gates, x, y, 'AND')
        xor_gate = find(gates, x, y, 'XOR')
        a, s = label('a', i), label('s', i)
        z, p = label('z', i), label('p', i)
        z_gate = find_partial(gates, xor_gate[3], 'XOR')
        p_gate = find_partial(gates, xor_gate[3], 'AND')
        if z_gate is not None and p_gate is not None:
            zc = [a for a in (z_gate[0], z_gate[1]) if a != xor_gate[3]][0]
            pc = [a for a in (p_gate[0], p_gate[1]) if a != xor_gate[3]][0]
            if zc == pc and z_gate[3] != z:
                exchange.append(z_gate[3])
                exchange.append(z)
                continue
        if z_gate is None and p_gate is None:
            exchange.append(xor_gate[3])
            real_z_gate = find_z(gates, z)
            a, b = real_z_gate[0], real_z_gate[1]
            if find_c(gates, a) is not None:
                exchange.append(b)
            if find_c(gates, b) is not None:
                exchange.append(a)
            continue
        nc_gate = find(gates, p_gate[3], and_gate[3], 'OR')
        if nc_gate is None:
            print('error', i)
    return ','.join(sorted(exchange))


if __name__ == '__main__':
    start_time = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    end1_time = time.time()
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
    end2_time = time.time()
    print(
        f'Part 1: {end1_time - start_time:.3f}s, Part 2: {end2_time - end1_time:.3f}s, Tot: {end2_time - start_time:.3f}s')
