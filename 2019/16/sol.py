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
                # print(signal[z], pattern[((z + 1) // (j + 1)) % 4])
                x += signal[z] * pattern[((z + 1) // (j + 1)) % 4]
            new_signal.append(abs(x) % 10)
        signal = new_signal.copy()
    return ''.join([str(n) for n in signal[:8]])


def sol2(filename):
    _ = get_input(filename)
    return 0


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    # print('--- Part 2 ---')
    # print(f'Test: {sol2("test.txt")}')
    # print(f'Solution: {sol2("input.txt")}')
