#!/usr/bin/env python3

import math
import time


def get_input(filename):
    f = open(filename, 'r')
    equations = []
    for line in f.readlines():
        result = int(line.split(':')[0])
        numbers = [int(x) for x in line.strip().split(':')[1][1:].split(' ')]
        equations.append((result, numbers))
    f.close()
    return equations


def add_inv(a, b):
    return a - b


def mul_inv(a, b):
    if a % b == 0:
        return a / b
    return None


def concat_inv(a, b):
    if (a - b) % math.pow(10, len(str(b))) == 0:
        return (a - b) / math.pow(10, len(str(b)))
    return None


def is_valid(result, numbers, operators):
    if len(numbers) == 1:
        return result == numbers[0]
    for op in operators:
        if op(result, numbers[-1]) and is_valid(op(result, numbers[-1]), numbers[:-1], operators):
            return True
    return False


def valid_results(filename, operators):
    equations = get_input(filename)
    tot = 0
    for equation in equations:
        result, numbers = equation
        if is_valid(result, numbers, operators):
            tot += result
    return tot


def sol1(filename):
    return valid_results(filename, [add_inv, mul_inv])


def sol2(filename):
    return valid_results(filename, [add_inv, mul_inv, concat_inv])


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    end1 = time.time()
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    end2 = time.time()
    print(f'Part 1: {end1 - start:.3f}s, Part 2: {end2 - end1:.3f}s, Tot: {end2 - start:.3f}s')
