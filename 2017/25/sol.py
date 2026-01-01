#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    raw = f.read()
    start_state = raw.split('\n')[0][-2]
    steps = int(raw.split('\n')[1].split()[-2])
    f.close()
    states = {}
    for state_raw in raw.split('\n\n')[1:]:
        name = state_raw.split('\n')[0][-2]
        state = {}
        values_raw = state_raw.split('If')[1:]
        for value_raw in values_raw:
            value = int(value_raw.split(':')[0][-1])
            new_value = int(value_raw.split('.')[0][-1])
            move = value_raw.split('.')[1].split()[-1]
            new_state = value_raw.split('.')[2][-1]
            state[value] = (new_value, move, new_state)
        states[name] = state
    return start_state, steps, states


def sol1(filename):
    state, steps, states = get_input(filename)
    pos = 0
    on = set()
    for i in range(steps):
        v = 0
        if pos in on:
            v = 1
        to_do = states[state][v]
        if to_do[0] == 1:
            on.add(pos)
        elif pos in on:
            on.remove(pos)
        if to_do[1] == 'right':
            pos += 1
        else:
            pos -= 1
        state = to_do[2]
    return len(on)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
