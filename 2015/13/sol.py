#!/usr/bin/env python3
import itertools


def get_input(filename):
    f = open(filename, 'r')
    gains = {}
    people = set()
    for line in f:
        p1 = line.split(' ')[0]
        p2 = line.strip().split(' ')[-1][:-1]
        gain = line.split(' ')[2]
        amount = line.split(' ')[3]
        gains[(p1, p2)] = int(amount) if gain == 'gain' else -int(amount)
        people.add(p1)
    f.close()
    return gains, people


def get_max_gain(gains, people):
    max_gain = 0
    for perm in itertools.permutations(people):
        tot_gain = gains[(perm[0], perm[-1])] + gains[(perm[-1], perm[0])]
        for i in range(len(perm)-1):
            tot_gain += gains[(perm[i], perm[i + 1])] + gains[(perm[i + 1], perm[i])]
        if tot_gain > max_gain:
            max_gain = tot_gain
    return max_gain


def sol1(filename):
    gains, people = get_input(filename)
    return get_max_gain(gains, people)


def sol2(filename):
    gains, people = get_input(filename)
    for p in people:
        gains[('Me', p)] = 0
        gains[(p, 'Me')] = 0
    people.add('Me')
    return get_max_gain(gains, people)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
