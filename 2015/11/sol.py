#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r').read()
    return f.strip()


def next_pwd(pwd, i):
    idx = len(pwd) - 1 - i
    c = pwd[idx]
    if c == 'z':
        pwd = pwd[:idx] + 'a' + pwd[idx + 1:]
        return next_pwd(pwd, i + 1)
    return pwd[:idx] + chr(ord(c) + 1) + pwd[idx + 1:]


def is_valid(pwd):
    three_straight = False
    for i in range(len(pwd) - 2):
        if ord(pwd[i]) + 1 == ord(pwd[i + 1]) and ord(pwd[i]) + 2 == ord(pwd[i + 2]):
            three_straight = True
            break
    if not three_straight:
        return False

    if 'i' in pwd or 'l' in pwd or 'o' in pwd:
        return False

    n_pairs = 0
    for i in range(len(pwd) - 1):
        if pwd[i] == pwd[i + 1] and pwd[i] != pwd[i - 1]:
            n_pairs += 1
    return n_pairs >= 2


def sol1(filename):
    pwd = get_input(filename)
    valid = False
    while not valid:
        pwd = next_pwd(pwd, 0)
        valid = is_valid(pwd)
    return pwd


def sol2(filename):
    pwd = get_input(filename)
    n_valid = 0
    while n_valid < 2:
        pwd = next_pwd(pwd, 0)
        valid = is_valid(pwd)
        if valid:
            n_valid += 1
    return pwd


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
