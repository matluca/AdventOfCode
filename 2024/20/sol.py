#!/usr/bin/env python3

import time


def get_input(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    grid = {}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            grid[(i, j)] = lines[i][j]
    return grid


def find_path(grid):
    current = [p for p, v in grid.items() if v == 'S'][0]
    path = [current]
    while grid[path[-1]] != 'E':
        for next_pos in [(current[0] + d[0], current[1] + d[1]) for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]]:
            if grid[next_pos] != '#' and next_pos not in path:
                current = next_pos
                path.append(current)
                break
    return path


def find_cheats(path, max_cheat, min_save):
    cheats = {}
    for i in range(len(path)):
        for j in range(i + 2 + min_save, len(path)):
            p, q = path[i], path[j]
            dist = abs(p[0] - q[0]) + abs(p[1] - q[1])
            if dist <= max_cheat:
                save = j - i - dist
                if save >= min_save:
                    if save not in cheats.keys():
                        cheats[save] = 0
                    cheats[save] += 1
    return cheats


def sol1(filename, min_save):
    grid = get_input(filename)
    path = find_path(grid)
    cheats = find_cheats(path, 2, min_save)
    return sum(cheats.values())


def sol2(filename, min_save):
    grid = get_input(filename)
    path = find_path(grid)
    cheats = find_cheats(path, 20, min_save)
    return sum(cheats.values())


if __name__ == '__main__':
    start_time = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 64)}')
    print(f'Solution: {sol1("input.txt", 100)}')
    end1_time = time.time()
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt", 66)}')
    print(f'Solution: {sol2("input.txt", 100)}')
    end2_time = time.time()
    print(
        f'Part 1: {end1_time - start_time:.3f}s, Part 2: {end2_time - end1_time:.3f}s, Tot: {end2_time - start_time:.3f}s')
