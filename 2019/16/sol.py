#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    n_raw = f.read().strip()
    f.close()
    return [int(n) for n in n_raw]


def sol1(filename):
    signal = get_input(filename)
    pattern = [0, 1, 0, -1]
    for i in range(100):
        new_signal = []
        for j in range(len(signal)):
            x = 0
            for z in range(len(signal)):
                x += signal[z] * pattern[((z + 1) // (j + 1)) % 4]
            new_signal.append(abs(x) % 10)
        signal = new_signal.copy()
    return ''.join([str(n) for n in signal[:8]])


def sol2(filename):
    signal = get_input(filename)
    reversed_signal = list(reversed(signal))
    needed = len(signal) * 10000 - int(''.join([str(n) for n in signal[:7]]))
    simplified = []
    for i in range(needed):
        simplified.append(reversed_signal[i % len(signal)])
    for step in range(100):
        new_simplified = [simplified[0]]
        for i in range(1, len(simplified)):
            new_simplified.append(new_simplified[i - 1] + simplified[i])
        simplified = [abs(x) % 10 for x in new_simplified]
    return ''.join([str(n) for n in list(reversed(simplified[-8:]))])


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
