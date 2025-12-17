#!/usr/bin/env python3
import time


def get_input(filename):
    f = open(filename, 'r')
    lines_raw = f.readlines()
    f.close()
    intervals = []
    for line_raw in lines_raw:
        intervals.append(tuple([int(x) for x in line_raw.split('-')]))
    return intervals


def simplify_intervals(intervals):
    intervals.sort()
    simplified_intervals = [intervals[0]]
    for interval in intervals[1:]:
        c, d = interval
        if c > simplified_intervals[-1][1]:
            simplified_intervals.append(interval)
            continue
        for i, si in enumerate(simplified_intervals):
            a, b = si
            if b < c:
                continue
            if d >= a >= c:
                simplified_intervals[i] = (c, max(b, d))
                break
            if b >= c >= a:
                simplified_intervals[i] = (a, max(b, d))
                break
            else:
                simplified_intervals.append(interval)
                break
        simplified_intervals.sort()
    real_simplified_intervals = [simplified_intervals[0]]
    for si in simplified_intervals[1:]:
        if si[0] == real_simplified_intervals[-1][1] + 1:
            real_simplified_intervals[-1] = (real_simplified_intervals[-1][0], si[1])
        else:
            real_simplified_intervals.append(si)
    return real_simplified_intervals


def sol1(filename):
    intervals = get_input(filename)
    simplified_intervals = simplify_intervals(intervals)
    return simplified_intervals[0][1] + 1


def sol2(filename, maximum):
    intervals = get_input(filename)
    simplified_intervals = simplify_intervals(intervals)
    tot = 0
    for i in range(len(simplified_intervals) - 1):
        tot += simplified_intervals[i + 1][0] - simplified_intervals[i][1] - 1
    tot += maximum - simplified_intervals[-1][1]
    return tot


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt", 9)}')
    print(f'Solution: {sol2("input.txt", 4294967295)}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
