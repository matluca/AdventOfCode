#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    lines = (line.rstrip() for line in f.readlines())
    reports = []
    for line in lines:
        if not line:
            continue
        reports.append([int(n) for n in line.split(' ')])
    f.close()
    return reports


def is_report_safe(report):
    safe = True
    d1 = report[1] - report[0]
    if not (0 < abs(d1) < 4):
        safe = False
    for i in range(len(report)-2):
        d = report[i+2] - report[i+1]
        if (d1 * d < 0) or not (0 < abs(d) < 4):
            safe = False
            break
    return safe


def sol1(filename):
    reports = get_input(filename)
    n_safe = 0
    for report in reports:
        if is_report_safe(report):
            n_safe += 1
    return n_safe


def sol2(filename):
    reports = get_input(filename)
    n_safe = 0
    for report in reports:
        if is_report_safe(report):
            n_safe += 1
            continue
        for i in range(len(report)):
            if is_report_safe(report[:i] + report[i+1:]):
                n_safe += 1
                break
    return n_safe


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
