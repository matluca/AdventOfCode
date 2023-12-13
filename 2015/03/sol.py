#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r').read()
    return f


def get_positions(inp):
    pos = (0, 0)
    visited = {pos}
    for c in inp:
        if c == '^':
            new = (pos[0], pos[1] + 1)
        elif c == 'v':
            new = (pos[0], pos[1] - 1)
        elif c == '>':
            new = (pos[0] + 1, pos[1])
        else:
            new = (pos[0] - 1, pos[1])
        visited.add(new)
        pos = new
    return visited


def sol1(filename):
    inp = get_input(filename)
    return len(get_positions(inp))


def sol2(filename):
    inp = get_input(filename)
    santa = [inp[i] for i in range(len(inp)) if i % 2 == 0]
    robot = [inp[i] for i in range(len(inp)) if i % 2 == 1]
    santa_pos = get_positions(santa)
    robot_pos = get_positions(robot)
    return len(santa_pos | robot_pos)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
