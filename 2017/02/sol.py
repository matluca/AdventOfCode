#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    spreadsheet = []
    for line in f.readlines():
        spreadsheet.append([int(x) for x in line.split()])
    f.close()
    return spreadsheet


def sol1(filename):
    spreadsheet = get_input(filename)
    return sum([max(line) - min(line) for line in spreadsheet])


def sol2(filename):
    spreadsheet = get_input(filename)
    tot = 0
    for line in spreadsheet:
        for i, a in enumerate(line):
            for b in line[i + 1:]:
                if max(a, b) % min(a, b) == 0:
                    tot += max(a, b) // min (a, b)
    return tot


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
