#!/usr/bin/env python3

def get_input(filename):
    galaxies = []
    f = open(filename, 'r')
    i = 0
    for line in f:
        for j in range(len(line)):
            if line[j] == '#':
                galaxies.append((i, j))
        i += 1
    f.close()
    return galaxies, i


def man_distance(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def sol(filename, expansion_rate):
    galaxies, size = get_input(filename)
    empty_rows, empty_columns = [], []
    for i in range(size):
        if i not in [p[0] for p in galaxies]:
            empty_rows.append(i)
        if i not in [p[1] for p in galaxies]:
            empty_columns.append(i)
    for i in range(len(empty_rows)):
        r = empty_rows[i]
        galaxies = [(p[0], p[1]) if p[0] < r else (p[0] + expansion_rate, p[1]) for p in galaxies]
        empty_rows = [e if e <= r else e + expansion_rate for e in empty_rows]
    for i in range(len(empty_columns)):
        c = empty_columns[i]
        galaxies = [(p[0], p[1]) if p[1] < c else (p[0], p[1] + expansion_rate) for p in galaxies]
        empty_columns = [e if e <= c else e + expansion_rate for e in empty_columns]
    return sum(
        [man_distance(galaxies[i], galaxies[j]) for i in range(len(galaxies)) for j in range(i + 1, len(galaxies))])


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol("test.txt", 1)}')
    print(f'Solution: {sol("input.txt", 1)}')
    print('--- Part 2 ---')
    print(f'Test: {sol("test.txt", 9)}')
    print(f'Test: {sol("test.txt", 99)}')
    print(f'Solution: {sol("input.txt", 999999)}')
