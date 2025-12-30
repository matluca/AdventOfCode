#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    steps = int(f.read().strip())
    f.close()
    return steps


def sol1(filename):
    steps = get_input(filename)
    spinlock = [0]
    current_pos = 0
    for i in range(1, 2018):
        current_pos = (current_pos + steps) % len(spinlock)
        spinlock.insert(current_pos + 1, i)
        current_pos += 1
    return spinlock[spinlock.index(2017) + 1]


def sol2(filename):
    steps = get_input(filename)
    spinlock_size = 1
    current_pos = 0
    next_value = None
    for i in range(1, 50000001):
        current_pos = (current_pos + steps) % spinlock_size
        if current_pos == 0:
            next_value = i
        spinlock_size += 1
        current_pos += 1
    return next_value


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
