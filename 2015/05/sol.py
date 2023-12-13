#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r').read()
    return f.split('\n')


def is_nice_1(s):
    if s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') < 3:
        return False

    no_doubles = True
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            no_doubles = False
            break
    if no_doubles:
        return False

    for x in ['ab', 'cd', 'pq', 'xy']:
        if x in s:
            return False
    return True


def is_nice_2(s):
    repeated_pair = False
    for i in range(len(s) - 1):
        p = s[i:i + 2]
        if p in s[i + 2:]:
            repeated_pair = True
            break
    if not repeated_pair:
        return False

    letter_in_between = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            letter_in_between = True
            break
    return letter_in_between


def sol1(filename):
    strings = get_input(filename)
    res = 0
    for s in strings:
        if is_nice_1(s):
            res += 1
    return res


def sol2(filename):
    strings = get_input(filename)
    res = 0
    for s in strings:
        if is_nice_2(s):
            res += 1
    return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
