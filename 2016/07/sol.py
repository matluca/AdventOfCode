#!/usr/bin/env python3
import time


def get_input(filename):
    f = open(filename, 'r').read()
    return f.split('\n')


def sol1(filename):
    ips = get_input(filename)
    valid = 0
    for ip in ips:
        inside = False
        is_valid = False
        for i in range(len(ip) - 3):
            if ip[i] == '[':
                inside = True
                continue
            if ip[i] == ']':
                inside = False
                continue
            abba = ip[i] == ip[i + 3] and ip[i + 1] == ip[i + 2] and ip[i] != ip[i + 1]
            if inside and abba:
                is_valid = False
                break
            if abba and not inside:
                is_valid = True
        if is_valid:
            valid += 1
    return valid


def sol2(filename):
    ips = get_input(filename)
    valid = 0
    for ip in ips:
        outside = '-'.join([x.split(']')[1] if ']' in x else x for x in ip.split('[')])
        inside = '-'.join([x.split(']')[0] if ']' in x else '' for x in ip.split('[')])
        for i in range(len(inside) - 2):
            is_aba = inside[i] == inside[i + 2] and inside[i] != inside[i + 1]
            if is_aba:
                bab = inside[i + 1] + inside[i] + inside[i + 1]
                if bab in outside:
                    valid += 1
                    break
    return valid


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
