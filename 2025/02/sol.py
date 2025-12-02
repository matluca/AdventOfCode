#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    all = f.readline().strip()
    f.close()
    intervals = []
    for int_raw in all.split(','):
        ar, br = int_raw.split('-')
        a, b = int(ar), int(br)
        intervals.append((a, b))
    return intervals


def first_part(n, d):
    s = str(n)
    if len(s) % d == 0:
        return int(s[:len(s) // d])
    else:
        return pow(10, len(s) // d)


def full(n, d):
    s = str(n)
    return int(s * d)


def sol1(filename):
    intervals = get_input(filename)
    tot = 0
    for interval in intervals:
        a, b = interval
        h = first_part(a, 2)
        while full(h, 2) <= b:
            if full(h, 2) >= a:
                tot += full(h, 2)
            h += 1
    return tot


def sol2(filename):
    intervals = get_input(filename)
    found = set()
    for interval in intervals:
        a, b = interval
        for d in range(2, len(str(b)) + 1):
            h = first_part(a, d)
            while full(h, d) <= b:
                if full(h, d) >= a:
                    found.add( full(h, d))
                h += 1
    return sum(found)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
