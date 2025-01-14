#!/usr/bin/env python3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from intcode import Intcode


def get_input(filename):
    f = open(filename, 'r')
    memory = [int(x) for x in f.read().strip().split(',')]
    f.close()
    return memory


def neighbours(x, y, size_x, size_y):
    neighbours = []
    if x > 0:
        neighbours.append((x - 1, y))
    if x < size_x - 1:
        neighbours.append((x + 1, y))
    if y > 0:
        neighbours.append((x, y - 1))
    if y < size_y - 1:
        neighbours.append((x, y + 1))
    return neighbours


def is_intersection(grid, x, y):
    size_x, size_y = len(grid), len(grid[0])
    for p in neighbours(x, y, size_x, size_y):
        if grid[p[0]][p[1]] != '#':
            return False
    return True


def sol1(filename):
    memory = get_input(filename)
    intcode = Intcode(memory)
    intcode.run()
    grid = [[]]
    row = 0
    for x in intcode.output[:-2]:
        if x != 10:
            grid[row].append(chr(x))
        else:
            row += 1
            grid.append([])
    size_x, size_y = len(grid), len(grid[0])
    tot = 0
    for x in range(size_x):
        for y in range(size_y):
            if is_intersection(grid, x, y):
                tot += x * y
    return tot


def are_connected(p, q, grid):
    if p[0] != q[0] and p[1] != q[1]:
        return False
    if p == q:
        return False
    if p[0] == q[0]:
        for y in range(min(q[1], p[1]) + 1, max(p[1], q[1]) - 1):
            if grid[p[0]][y] != '#':
                return False
        return True
    if p[1] == q[1]:
       for x in range(min(q[0], p[0]) + 1, max(p[0], q[0]) - 1):
           if grid[x][p[1]] != '#':
               return False
       return True


def is_angle(grid, x, y):
    size_x, size_y = len(grid), len(grid[0])
    if grid[x][y] != '#':
        return False
    neigh = []
    for p in neighbours(x, y, size_x, size_y):
        if grid[p[0]][p[1]] == '#':
            neigh.append((p[0], p[1]))
    if len(neigh) == 2 and neigh[0][0] != neigh[1][0] and neigh[0][1] != neigh[1][1]:
        return True
    return False


def is_end(grid, x, y):
    size_x, size_y = len(grid), len(grid[0])
    if grid[x][y] != '#':
        return False
    neigh = []
    for p in neighbours(x, y, size_x, size_y):
        if grid[p[0]][p[1]] == '#':
            neigh.append((p[0], p[1]))
    if len(neigh) == 1:
        return True
    return False


def sol2(filename):
    memory = get_input(filename)
    intcode = Intcode(memory.copy())
    intcode.run()
    grid = [[]]
    row = 0
    for x in intcode.output[:-2]:
        if x != 10:
            grid[row].append(chr(x))
        else:
            row += 1
            grid.append([])
    size_x, size_y = len(grid), len(grid[0])
    angles = []
    robot = ()
    for x in range(size_x):
        for y in range(size_y):
            if grid[x][y] in ['^', '<', '>', 'v']:
                robot = (x, y)
            if is_angle(grid, x, y) or is_end(grid, x, y):
                angles.append((x, y))
    path = [robot]
    for n in neighbours(robot[0], robot[1], size_x, size_y):
        if n in angles:
            angles.remove(n)
    while len(angles) > 0:
        p = path[-1]
        next_node = None
        for q in angles:
            if are_connected(p, q, grid):
                next_node = q
                break
        path.append(next_node)
        angles.remove(next_node)
    direction = '^'
    output = []
    for i in range(len(path) - 1):
        a, b = path[i], path[i + 1]
        new_direction = '^'
        if b[0] == a[0]:
            if b[1] < a[1]:
                new_direction = '<'
            else:
                new_direction = '>'
        if b[1] == a[1]:
            if b[0] > a[0]:
                new_direction = 'v'
        dirs = ['^', '>', 'v', '<']
        if dirs.index(new_direction) - dirs.index(direction) in [1, -3]:
            output.append('R')
        if dirs.index(new_direction) - dirs.index(direction) in [-1, 3]:
            output.append('L')
        if a[0] == b[0]:
            output.append(abs(a[1] - b[1]))
        if a[1] == b[1]:
            output.append(abs(a[0] - b[0]))
        direction = new_direction
    print(output)
    # Manual inspection
    main_routine = ['A', 'B', 'A', 'B', 'C', 'C', 'B', 'A', 'B', 'C']
    mov_a = ['L', 12, 'L', 10, 'R', 8, 'L', 12]
    mov_b = ['R', 8, 'R', 10, 'R', 12]
    mov_c = ['L', 10, 'R', 12, 'R', 8]
    inp = []
    for x in main_routine:
        inp.append(ord(x))
        inp.append(ord(','))
    inp[-1] = ord('\n')
    for mov in [mov_a, mov_b, mov_c]:
        for x in mov:
            if isinstance(x, int):
                s = str(x)
                for c in s:
                    inp.append(ord(c))
            else:
                inp.append(ord(x))
            inp.append(ord(','))
        inp[-1] = ord('\n')
    inp.append(ord('n'))
    inp.append(ord('\n'))
    memory = get_input(filename)
    memory[0] = 2
    intcode = Intcode(memory, inp)
    intcode.run()
    return intcode.output[-1]


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
