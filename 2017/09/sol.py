#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    streams = []
    for line in f.readlines():
        streams.append(line.strip())
    f.close()
    return streams


def compute(stream):
    groups = {}
    garbage = False
    pos = 0
    level = 0
    garbage_len = 0
    while pos < len(stream):
        c = stream[pos]
        if garbage and c not in ['>', '!']:
            garbage_len += 1
        if c == '{' and not garbage:
            level += 1
        elif c == '}' and not garbage:
            if level not in groups.keys():
                groups[level] = 1
            else:
                groups[level] += 1
            level -= 1
        elif c == '<':
            garbage = True
        elif c == '>':
            garbage = False
        elif c == '!':
            pos += 1
        pos += 1
    return groups, garbage_len


def sol1(filename):
    streams = get_input(filename)
    scores = []
    for stream in streams:
        groups, _ = compute(stream)
        scores.append(sum([key * value for key, value in groups.items()]))
    return scores


def sol2(filename):
    streams = get_input(filename)
    garbage_lens = []
    for stream in streams:
        _, garbage_len = compute(stream)
        garbage_lens.append(garbage_len)
    return garbage_lens


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
