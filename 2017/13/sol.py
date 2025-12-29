#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    layers = {}
    for line in f.readlines():
        layers[int(line.split(':')[0])] = int(line.strip().split()[1])
    f.close()
    return layers


def sol1(filename):
    layers = get_input(filename)
    tot = 0
    for i in range(max(layers.keys()) + 1):
        if i in layers.keys() and i % (2 * layers[i] - 2) == 0:
            tot += i * layers[i]
    return tot


def sol2(filename):
    layers = get_input(filename)
    delay = 0
    while True:
        caught = False
        for i in range(max(layers.keys()) + 1):
            if i in layers.keys() and (i + delay) % (2 * layers[i] - 2) == 0:
                caught = True
                break
        if not caught:
            return delay
        delay += 1


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
