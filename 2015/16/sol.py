#!/usr/bin/env python3


desired = {'children': 3,
           'cats': 7,
           'samoyeds': 2,
           'pomeranians': 3,
           'akitas': 0,
           'vizslas': 0,
           'goldfish': 5,
           'trees': 3,
           'cars': 2,
           'perfumes': 1}


def get_input(filename):
    f = open(filename, 'r')
    sues = []
    for line in f:
        sue = {}
        for v in line.strip().split(': ', 1)[1].split(', '):
            sue[v.split(': ')[0]] = int(v.split(': ')[1])
        sues.append(sue)
    f.close()
    return sues


def sol1(filename):
    sues = get_input(filename)
    for i, sue in enumerate(sues):
        if all([v == desired[k] for k, v in sue.items()]):
            return i + 1


def sol2(filename):
    sues = get_input(filename)
    for i, sue in enumerate(sues):
        matches = [sue[k] == desired[k] for k in ['children', 'samoyeds', 'akitas', 'vizslas', 'cars', 'perfumes'] if
                   k in sue.keys()]
        for k in ['cats', 'trees']:
            if k in sue.keys():
                matches.append(sue[k] > desired[k])
        for k in ['pomeranians', 'goldfish']:
            if k in sue.keys():
                matches.append(sue[k] < desired[k])
        if all(matches):
            return i + 1


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
    print(f'Solution: {sol2("input.txt")}')
