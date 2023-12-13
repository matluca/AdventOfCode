#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r').read()
    patterns = f.split('\n\n')
    return patterns


def transpose_pattern(pattern):
    lines = pattern.split('\n')
    new_lines = []
    for i in range(len(lines[0])):
        new_lines.append(''.join([line[i] for line in lines]))
    return '\n'.join(new_lines)


def compare_lists(l1, l2, smudges):
    if smudges == 0:
        return l1 == l2
    if len(l1) != len(l2):
        return False
    off = 0
    for i in range(len(l1)):
        for j in range(len(l1[i])):
            if l1[i][j] != l2[i][j]:
                off += 1
                if off > smudges:
                    return False
    return off == smudges


def find_reflection_row(pattern, smudges):
    lines = pattern.split('\n')
    for i in range(1, int(len(lines) / 2) + 1):
        if compare_lists(lines[:i], list(reversed(lines[i:2 * i])), smudges):
            return i
        if compare_lists(lines[-i:], list(reversed(lines[-2 * i:-i])), smudges):
            return len(lines) - i
    return 0


def find_reflection_column(pattern, smudges):
    return find_reflection_row(transpose_pattern(pattern), smudges)


def sol1(filename):
    patterns = get_input(filename)
    res = 0
    for p in patterns:
        res += 100 * find_reflection_row(p, 0) + find_reflection_column(p, 0)
    return res


def sol2(filename):
    patterns = get_input(filename)
    res = 0
    for p in patterns:
        res += 100 * find_reflection_row(p, 1) + find_reflection_column(p, 1)
    return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
