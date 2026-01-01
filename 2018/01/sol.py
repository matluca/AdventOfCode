#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    freqs = []
    for line in f.readlines():
        freqs.append(line.strip())
    f.close()
    return freqs


def sol1(filename):
    freqs = get_input(filename)
    freqs.insert(0, '0')
    return eval(''.join(freqs))


def sol2(filename):
    freqs = get_input(filename)
    hits = set()
    value = 0
    pos = 0
    while True:
        value = eval(str(value) + freqs[pos])
        pos = (pos + 1) % len(freqs)
        if value in hits:
            return value
        hits.add(value)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
