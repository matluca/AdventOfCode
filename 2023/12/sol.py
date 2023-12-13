#!/usr/bin/env python3
import functools


def get_input(filename):
    f = open(filename, 'r')
    inputs, blocks = [], []
    for line in f:
        inputs.append(line.split(' ')[0])
        blocks.append([int(n) for n in line.strip().split(' ')[1].split(',')])
    f.close()
    return inputs, blocks


@functools.cache
def possibilities(inp, block):
    if len(block) == 0:
        if '#' not in inp:
            return 1
        return 0

    if len(inp) < sum(block) + len(block) - 1:
        return 0

    if len(block) == 1:
        if len(inp) == block[0]:
            if '.' not in inp:
                return 1
            else:
                return 0

    if inp[0] == '.':
        return possibilities(inp[1:], block)

    if inp[0] == '#':
        if '.' in inp[:block[0]]:
            return 0
        if len(inp) == block[0]:
            return 1
        if inp[block[0]] == '#':
            return 0
        else:
            return possibilities(inp[block[0] + 1:], block[1:])

    if inp[0] == '?':
        return possibilities('.' + inp[1:], block) + possibilities('#' + inp[1:], block)


def sol(inputs, blocks):
    res = 0
    for i in range(len(inputs)):
        res += possibilities(inputs[i], tuple(blocks[i]))
    return res


def sol1(filename):
    inputs, blocks = get_input(filename)
    return sol(inputs, blocks)


def sol2(filename):
    inputs, blocks = get_input(filename)
    for i in range(len(inputs)):
        inp = inputs[i]
        b = blocks[i].copy()
        for j in range(4):
            inputs[i] += '?' + inp
            blocks[i] += b
    return sol(inputs, blocks)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
