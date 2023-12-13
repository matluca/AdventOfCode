#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r').read()
    return f.strip()


def sol1(filename):
    input_string = get_input(filename)
    return input_string.count('(') - input_string.count(')')


def sol2(filename):
    input_string = get_input(filename)
    floor = 0
    for i, c in enumerate(input_string):
        if c == '(':
            floor += 1
        else:
            floor += -1
        if floor < 0:
            return i + 1
    return 0


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
