#!/usr/bin/env python3


def get_input(filename):
    f = open(filename, 'r').read()
    return f.split('\n')


def possible(direction):
    if direction == (-1, 0):
        return ['7', '|', 'F']
    if direction == (1, 0):
        return ['J', '|', 'L']
    if direction == (0, 1):
        return ['J', '-', '7']
    if direction == (0, -1):
        return ['L', '-', 'F']
    return None


def next_direction(p, grid, direction):
    s = grid[p[0]][p[1]]
    if s == '|' or s == '-':
        return direction
    if s == '7':
        if direction == (-1, 0):
            return 0, -1
        if direction == (0, 1):
            return 1, 0
    if s == 'F':
        if direction == (-1, 0):
            return 0, 1
        if direction == (0, -1):
            return 1, 0
    if s == 'J':
        if direction == (0, 1):
            return -1, 0
        if direction == (1, 0):
            return 0, -1
    if s == 'L':
        if direction == (1, 0):
            return 0, 1
        if direction == (0, -1):
            return -1, 0
    return []


def next_point(p, direction):
    return p[0] + direction[0], p[1] + direction[1]


def replace_start(start_direction, end_direction):
    if start_direction == (-1, 0):
        if end_direction == (-1, 0):
            return '|'
        if end_direction == (0, 1):
            return 'J'
        if end_direction == (0, -1):
            return 'L'
    if start_direction == (1, 0):
        if end_direction == (1, 0):
            return '|'
        if end_direction == (0, 1):
            return '7'
        if end_direction == (0, -1):
            return 'F'
    if start_direction == (0, 1):
        if end_direction == (0, 1):
            return '-'
        if end_direction == (1, 0):
            return 'L'
        if end_direction == (-1, 0):
            return 'F'
    if start_direction == (0, -1):
        if end_direction == (0, -1):
            return '-'
        if end_direction == (1, 0):
            return 'J'
        if end_direction == (-1, 0):
            return '7'


def sol(filename, part):
    grid = get_input(filename)
    only_loop = [['.' for j in grid[0]] for i in grid]
    start = (0, 0)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i, j)
                only_loop[start[0]][start[1]] = 'S'
                break
    direction = (0, 0)
    start_direction = (0, 0)
    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_p = next_point(start, d)
        if grid[next_p[0]][next_p[1]] in possible(d):
            direction = d
            start_direction = d
            break
    p = next_point(start, direction)
    steps = 1
    while p != start:
        only_loop[p[0]][p[1]] = grid[p[0]][p[1]]
        direction = next_direction(p, grid, direction)
        p = next_point(p, direction)
        steps += 1
    if part == 1:
        return int(steps / 2)
    only_loop[start[0]][start[1]] = replace_start(start_direction, direction)

    n_inside = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if only_loop[i][j] == '.':
                n_jumps = 0
                for k in range(i):
                    ol = only_loop[k][j]
                    if ol == '-':
                        n_jumps += 2
                    if ol == 'F' or ol == 'J':
                        n_jumps += 1
                    if ol == 'L' or ol == '7':
                        n_jumps -= 1
                if n_jumps % 4 == 2:
                    n_inside += 1
                    only_loop[i][j] = 'O'
    return n_inside


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol("test.txt", 1)}')
    print(f'Test 2: {sol("test2.txt", 1)}')
    print(f'Solution: {sol("input.txt", 1)}')
    print('--- Part 2 ---')
    print(f'Test 3: {sol("test3.txt", 2)}')
    print(f'Test 4: {sol("test4.txt", 2)}')
    print(f'Test 5: {sol("test5.txt", 2)}')
    print(f'Solution: {sol("input.txt", 2)}')
