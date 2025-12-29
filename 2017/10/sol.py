#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    lengths = [int(x) for x in f.read().split(',')]
    f.close()
    return lengths


def get_input_2(filename):
    inputs = []
    f = open(filename, 'r')
    for line in f.readlines():
        inputs.append([ord(x) for x in line.strip()] + [17, 31, 73, 47, 23])
    f.close()
    return inputs


def get_hash(elements, current_position, skip_size, lengths):
    for length in lengths:
        tmp = []
        for j in range(length):
            tmp.append(elements[(current_position + j) % len(elements)])
        for j in range(length):
            elements[(current_position + length - j - 1) % len(elements)] = tmp[j]
        current_position = (current_position + length + skip_size) % len(elements)
        skip_size += 1
    return elements, current_position, skip_size


def sol1(filename, max_element):
    lengths = get_input(filename)
    elements = list(range(max_element))
    current_position = 0
    skip_size = 0
    elements, _, _ = get_hash(elements, current_position, skip_size, lengths)
    return elements[0] * elements[1]


def dense(elements):
    res = []
    for i in range(16):
        x = elements[16 * i] ^ elements[16 * i + 1]
        for j in range(2, 16):
            x = x ^ elements[16 * i + j]
        res.append(hex(x))
    return ''.join([str(x)[2:] for x in res])


def sol2(filename):
    inputs = get_input_2(filename)
    results = []
    for inp in inputs:
        elements = list(range(256))
        current_position = 0
        skip_size = 0
        for i in range(64):
            elements, current_position, skip_size = get_hash(elements, current_position, skip_size, inp)
        results.append(dense(elements))
    return results


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 5)}')
    print(f'Solution: {sol1("input.txt", 256)}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
