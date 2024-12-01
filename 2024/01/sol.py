#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    a, b = [], []
    lines = (line.rstrip() for line in f.readlines())
    for line in lines:
        if not line:
            continue
        x, y = line.split('   ')
        a.append(int(x))
        b.append(int(y))
    f.close()
    a.sort()
    b.sort()
    return a, b


def sol1(filename):
    a, b = get_input(filename)
    tot = 0
    for i in range(len(a)):
        tot += abs(a[i] - b[i])
    return tot


def sol2(filename):
    a, b = get_input(filename)
    tot = 0
    for x in a:
        tot += x * b.count(x)
    return tot


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
