#!/usr/bin/env python3

Up, Down, Left, Right = (-1, 0), (1, 0), (0, -1), (0, 1)
dir_map = {'U': Up, 'D': Down, 'R': Right, 'L': Left}
dir_map_2 = {'3': Up, '1': Down, '0': Right, '2': Left}


def get_input(filename):
    f = open(filename, 'r')
    instructions = []
    for line in f:
        d, a, c = line.strip().split(' ')
        instructions.append((dir_map[d], int(a)))
    f.close()
    return instructions


def get_input_2(filename):
    f = open(filename, 'r')
    instructions = []
    for line in f:
        d, a, c = line.strip().split(' ')
        instructions.append((dir_map_2[c[-2]], int(c[2:-2], 16)))
    f.close()
    return instructions


def area(vertices):
    return 0.5 * abs(sum(p[0] * q[1] - p[1]*q[0] for (p, q) in zip(vertices, vertices[1:] + [vertices[0]])))


def perimeter(vertices):
    return sum([abs(p[0] - q[0]) + abs(p[1] - q[1]) for (p, q) in zip(vertices, vertices[1:] + [vertices[0]])])


def sol(instructions):
    start = (0, 0)
    p = start
    vertices = []
    for inst in instructions:
        vertices.append(p)
        direction, a = inst
        p = (p[0] + direction[0] * a, p[1] + direction[1] * a)
    return int(area(vertices) + perimeter(vertices)/2 + 1)


def sol1(filename):
    instructions = get_input(filename)
    return sol(instructions)


def sol2(filename):
    instructions = get_input_2(filename)
    return sol(instructions)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
