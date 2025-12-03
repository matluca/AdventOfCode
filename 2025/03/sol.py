#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    banks = [[int(s) for s in line.strip()] for line in f.readlines()]
    f.close()
    return banks


def max_joltage(bank, n):
    joltage = []
    idx = 0
    for i in range(n):
        a = max(bank[idx:len(bank) + i - n + 1])
        joltage.append(a)
        idx = bank.index(a, idx) + 1
    return int(''.join(str(j) for j in joltage))


def sol1(filename):
    banks = get_input(filename)
    return sum(max_joltage(bank, 2) for bank in banks)


def sol2(filename):
    banks = get_input(filename)
    return sum(max_joltage(bank, 12) for bank in banks)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
