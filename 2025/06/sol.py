#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    lines_raw = f.readlines()
    f.close()
    lines = [l.strip().split() for l in lines_raw]
    return [[lines[j][i] for j in range(len(lines))] for i in range(len(lines[0]))]


def get_input_2(filename):
    f = open(filename, 'r')
    lines_raw = f.readlines()
    f.close()
    numbers = [l[:-1] for l in lines_raw[:-1]]
    operations = lines_raw[-1]
    return numbers, operations


def solve(problem):
    if problem[-1] == '+':
        return sum([int(i) for i in problem[:-1]])
    res = 1
    for i in problem[:-1]:
        res *= int(i)
    return res


def sol1(filename):
    problems = get_input(filename)
    tot = 0
    for problem in problems:
        tot += solve(problem)
    return tot


def op_size(operations):
    ops = []
    i = 0
    while i < len(operations):
        if operations[i] in ['+', '*']:
            j = 1
            while i + j < len(operations) and operations[i + j] not in ['+', '*']:
                j += 1
            ops.append((operations[i], i + j))
            i = i + j
    return ops


def compute_last_op(numbers, ops):
    op = ops.pop()
    if len(ops) > 0:
        prev_op = ops[-1]
    else:
        prev_op = ('+', 0)
    nums = []
    for i in range(op[1], prev_op[1] - 1, -1):
        num = ''
        for j in range(len(numbers)):
            try:
                num += numbers[j][i]
            except (IndexError, ValueError):
                num += ''
        try:
            nums.append(int(num))
        except ValueError:
            nums = []
    if op[0] == '+':
        return sum(nums), ops
    res = 1
    for num in nums:
        res *= num
    return res, ops


def sol2(filename):
    numbers, operations = get_input_2(filename)
    ops = op_size(operations)
    tot = 0
    while len(ops) > 0:
        res, ops = compute_last_op(numbers, ops)
        tot += res
    return tot


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
