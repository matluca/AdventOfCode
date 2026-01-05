#!/usr/bin/env python3

def get_input(filename):
    rules = set()
    f = open(filename, 'r')
    lines_raw = f.readlines()
    initial_state = lines_raw[0].strip().split(": ")[1]
    for line in lines_raw[2:]:
        if line.strip().split(' => ')[1] == '#':
            rules.add(line.split()[0])
    f.close()
    return initial_state, rules


def evolve(state, rules):
    new_state = set()
    for x in range(min(state) - 2, max(state) + 3):
        state_str = ''
        for i in range(x - 2, x + 3):
            if i in state:
                state_str += '#'
            else:
                state_str += "."
        if state_str in rules:
            new_state.add(x)
    return new_state


def sol1(filename):
    initial_state, rules = get_input(filename)
    state = set()
    for i, c in enumerate(initial_state):
        if c == '#':
            state.add(i)
    for i in range(20):
        state = evolve(state, rules)
    return sum(state)


def sol2(filename):
    initial_state, rules = get_input(filename)
    state = set()
    for i, c in enumerate(initial_state):
        if c == '#':
            state.add(i)
    d = 0
    for i in range(150):
        previous = sum(state)
        state = evolve(state, rules)
        current = sum(state)
        if current - previous != d:
            d = current - previous
            continue
        return current + d * (50000000000 - 1 - i)
    return 0


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
