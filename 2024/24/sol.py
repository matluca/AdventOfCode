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


def build_sum_gates(n):
    gates = [('x00', 'y00', 'XOR', 'z00'), ('x00', 'y00', 'AND', 'c01')]
    for i in range(1, n):
        x = f'x{i}'
        y = f'y{i}'
        s = f's{i}'
        z = f'z{i}'
        a = f'a{i}'
        c = f'c{i}'
        p = f'p{i}'
        nc = f'c{i + 1}'
        if i < 10:
            s = f's0{i}'
            z = f'z0{i}'
            a = f'a0{i}'
            x = f'x0{i}'
            y = f'y0{i}'
            c = f'c0{i}'
            p = f'p0{i}'
        if i < 9:
            nc = f'c0{i + 1}'
        gates.append((x, y, 'XOR', s))
        gates.append((c, s, 'XOR', z))
        gates.append((c, s, 'AND', p))
        gates.append((x, y, 'AND', a))
        gates.append((p, a, 'OR', nc))
    return gates


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
        z = label('z', i)
        mapping[and_gate[3]] = a
        mapping[xor_gate[3]] = s
        inv_mapping = {v: k for k, v in mapping.items()}
        z_gate = find_partial(gates, xor_gate[3], 'XOR')
        # TODO, find full with and + xor instead of finding partial
        if z_gate is None:
            print('not found', i, xor_gate[3])
            zz_gate = find_z(gates, z)
            print(zz_gate)
            aa, bb, oop, tt = zz_gate
            try:
                print(mapping[aa])
            except KeyError:
                exchange.append((xor_gate[3], aa))
                print(aa, "not mapped")
            try:
                print(mapping[bb])
            except KeyError:
                print(bb, "not mapped")
                exchange.append((xor_gate[3], bb))
            continue
        if z_gate[3] != z:
            print('error', i, z_gate)
            exchange.append((z_gate[3], z))
            continue
    list_exchange = []
    for ex in exchange:
        a, b = ex
        list_exchange.append(a)
        list_exchange.append(b)
    return ','.join(sorted(list_exchange))


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
