#!/usr/bin/env python3
import json


def get_input(filename):
    f = open(filename, 'r')
    return json.load(f)


def get_sum(d):
    if isinstance(d, int):
        return int(d)
    if isinstance(d, list):
        return sum([get_sum(v) for v in d])
    if isinstance(d, dict):
        return sum([get_sum(v) for v in d.values()])
    return 0


def get_sum_2(d):
    if isinstance(d, int):
        return int(d)
    if isinstance(d, list):
        return sum([get_sum_2(v) for v in d])
    if isinstance(d, dict):
        if "red" in d.values():
            return 0
        return sum([get_sum_2(v) for v in d.values()])
    return 0


def sol1(filename):
    inp = get_input(filename)
    return get_sum(inp)


def sol2(filename):
    inp = get_input(filename)
    return get_sum_2(inp)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
