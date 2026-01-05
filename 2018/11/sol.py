#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    serial = int(f.read().strip())
    f.close()
    return serial


def sol1(filename):
    serial = get_input(filename)
    grid = {}
    for i in range(1, 301):
        for j in range(1, 301):
            rack_id = i + 10
            pl = (rack_id * j + serial) * rack_id
            grid[(i, j)] = pl % 1000 // 100 - 5
    max_value = 0
    res = None
    for i in range(1, 298):
        for j in range(1, 298):
            value = sum([sum([grid[(x, y)] for x in range(i, i + 3)]) for y in range(j, j + 3)])
            if value > max_value:
                max_value = value
                res = (i, j)
    return res


def sol2(filename):
    serial = get_input(filename)
    grid = {}
    for i in range(1, 301):
        for j in range(1, 301):
            rack_id = i + 10
            pl = (rack_id * j + serial) * rack_id
            grid[(i, j)] = pl % 1000 // 100 - 5
    max_value = 0
    res = None
    for i in range(1, 301):
        for j in range(1, 301):
            value = grid[(i, j)]
            for size in range(2, 301):
                if (i + size > 300) or (j + size) > 300:
                    continue
                value += sum([grid[(x, j + size)] for x in range(i, i + size)])
                value += sum([grid[(i + size, y)] for y in range(j, j + size - 1)])
                if value > max_value:
                    max_value = value
                    res = (i, j, size + 1)
    return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
