#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    winning = []
    have = []
    for line in f:
        w = line.strip().split(': ')[1].split(' | ')[0].split(' ')
        h = line.strip().split(': ')[1].split(' | ')[1].split(' ')
        winning.append([int(n) for n in w if n != ''])
        have.append([int(n) for n in h if n != ''])
    f.close()
    return winning, have


def sol1(filename):
    winning, have = get_input(filename)
    res = 0
    for i in range(len(winning)):
        matches = len(set(winning[i]) & set(have[i]))
        if matches > 0:
            res += pow(2, matches - 1)
    return res


def sol2(filename):
    winning, have = get_input(filename)
    matches = []
    for i in range(len(winning)):
        matches.append(len(set(winning[i]) & set(have[i])))
    instances = [1] * len(matches)
    for i in range(len(matches)):
        for j in range(matches[i]):
            instances[i + j + 1] += instances[i]
    return sum(instances)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
