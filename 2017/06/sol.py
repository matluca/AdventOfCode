#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    raw = f.read().strip()
    f.close()
    return [int(x) for x in raw.split()]


def next_blocks(blocks):
    max_value = max(blocks)
    idx = blocks.index(max_value)
    blocks[idx] = 0
    for i in range(1, max_value + 1):
        blocks[(idx + i) % len(blocks)] += 1
    return blocks


def sol1(filename):
    blocks = get_input(filename)
    seen = {tuple(blocks)}
    steps = 0
    while True:
        blocks = next_blocks(blocks)
        steps += 1
        if tuple(blocks) in seen:
            return steps
        seen.add(tuple(blocks))


def sol2(filename):
    blocks = get_input(filename)
    seen = {tuple(blocks): 0}
    steps = 0
    while True:
        blocks = next_blocks(blocks)
        steps += 1
        if tuple(blocks) in seen.keys():
            return steps - seen[tuple(blocks)]
        seen[tuple(blocks)] = steps


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
