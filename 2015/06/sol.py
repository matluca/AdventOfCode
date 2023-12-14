#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    instructions = []
    for line in f:
        inst = line.split(' ')[0]
        a = [int(n) for n in line.split(' ')[1].split(',')]
        b = [int(n) for n in line.strip().split(' ')[3].split(',')]
        instructions.append((inst, a, b))
    f.close()
    return instructions


def sol1(filename):
    instructions = get_input(filename)
    grid = [[False] * 1000 for _ in range(1000)]
    for inst in instructions:
        a, b = inst[1], inst[2]
        for x in range(a[0], b[0] + 1):
            for y in range(a[1], b[1] + 1):
                if inst[0] == 'on':
                    grid[x][y] = True
                elif inst[0] == 'off':
                    grid[x][y] = False
                else:
                    grid[x][y] = not grid[x][y]
    return sum([line.count(True) for line in grid])


def sol2(filename):
    instructions = get_input(filename)
    grid = [[0] * 1000 for _ in range(1000)]
    for inst in instructions:
        a, b = inst[1], inst[2]
        for x in range(a[0], b[0] + 1):
            for y in range(a[1], b[1] + 1):
                if inst[0] == 'on':
                    grid[x][y] += 1
                elif inst[0] == 'off':
                    grid[x][y] = max(grid[x][y] - 1, 0)
                else:
                    grid[x][y] += 2
    return sum([sum(line) for line in grid])


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
