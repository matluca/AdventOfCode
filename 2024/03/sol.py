#!/usr/bin/env python3

import re


def get_input(filename):
    f = open(filename, 'r')
    in_string = f.read()
    f.close()
    return in_string


def multiply(string):
    regex = "mul\((\d+),(\d+)\)"
    groups = re.search(regex, string, flags=re.DOTALL).groups()
    return int(groups[0]) * int(groups[1])


def compute(string):
    tot = 0
    regex = "mul\(\d+,\d+\)"
    matches = re.findall(regex, string, flags=re.DOTALL)
    for match in matches:
        tot += multiply(match)
    return tot


def sol1(filename):
    in_string = get_input(filename)
    return compute(in_string)


def sol2(filename):
    in_string = get_input(filename)
    regex = "don't\(\).*?do\(\)"
    new_string = re.sub(regex, 'XXX', in_string, flags=re.DOTALL)
    return compute(new_string)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
