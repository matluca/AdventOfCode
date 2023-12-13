#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    grid = []
    for line in f:
        grid.append(line.strip())
    f.close()
    return grid


def get_numbers(grid):
    numbers = []
    for i in range(len(grid)):
        line = grid[i]
        current_number = {}
        for j in range(len(line)):
            if line[j].isdigit():
                current_number[(i, j)] = line[j]
            if j == len(line) - 1 or not line[j].isdigit():
                if current_number:
                    numbers.append(current_number)
                current_number = {}
    return numbers


def neighbours(pos, a, b):
    neigh = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            n = (pos[0] + i, pos[1] + j)
            if (i, j) != (0, 0) and a > n[0] >= 0 and b > n[1] >= 0:
                neigh.append(n)
    return neigh


def sol1(filename):
    grid = get_input(filename)
    numbers = get_numbers(grid)
    res = 0
    x = len(grid)
    y = len(grid[0])
    for number in numbers:
        is_part = False
        for pos in number.keys():
            for n in neighbours(pos, x, y):
                if grid[n[0]][n[1]] != '.' and not grid[n[0]][n[1]].isdigit():
                    is_part = True
                    break
        num = ''
        for d in number.values():
            num = num + d
        if is_part:
            res += int(num)
    return res


def sol2(filename):
    grid = get_input(filename)
    numbers = get_numbers(grid)
    res = 0
    x = len(grid)
    y = len(grid[0])
    gears = {}
    for number in numbers:
        touches_gear = (0, 0)
        for pos in number.keys():
            for n in neighbours(pos, x, y):
                if grid[n[0]][n[1]] == '*':
                    touches_gear = n
                    break
        num = ''
        for d in number.values():
            num = num + d
        if touches_gear == (0, 0):
            continue
        if touches_gear not in gears.keys():
            gears[touches_gear] = [int(num)]
        else:
            gears[touches_gear].append(int(num))
    for gear in gears.values():
        if len(gear) == 2:
            res += gear[0] * gear[1]
    return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
