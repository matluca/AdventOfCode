#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    sequences = []
    for line in f.readlines():
        sequences.append([int(x) for x in line.strip()])
    f.close()
    return sequences


def res(sequence):
    tot = 0
    for i in range(len(sequence)):
        if sequence[i] == sequence[(i + 1) % len(sequence)]:
            tot += sequence[i]
    return tot


def sol1(filename):
    sequences = get_input(filename)
    return [res(sequence) for sequence in sequences]


def res2(sequence):
    tot = 0
    for i in range(len(sequence)):
        if sequence[i] == sequence[(i + len(sequence) // 2) % len(sequence)]:
            tot += sequence[i]
    return tot


def sol2(filename):
    sequences = get_input(filename)
    return [res2(sequence) for sequence in sequences]


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
