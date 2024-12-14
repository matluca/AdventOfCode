#!/usr/bin/env python3


import math
import time
import regex


def get_input(filename):
    f = open(filename, 'r')
    reg = "p=(?<x>-?\d+),(?<y>-?\d+) v=(?<v_x>-?\d+),(?<v_y>-?\d+)"
    robots = []
    for r in regex.finditer(reg, f.read()):
        robots.append((int(r.group('x')), int(r.group('y')), int(r.group('v_x')), int(r.group('v_y'))))
    f.close()
    return robots


def safety_factor(positions, size_x, size_y):
    quadrants = [0] * 4
    for p in positions:
        x, y, = p
        if x < (size_x / 2) - 1 and y < (size_y / 2) - 1:
            quadrants[0] += 1
        elif x < (size_x / 2) - 1 and y > (size_y / 2):
            quadrants[1] += 1
        elif x > (size_x / 2) and y < (size_y / 2) - 1:
            quadrants[2] += 1
        elif x > (size_x / 2) and y > (size_y / 2):
            quadrants[3] += 1
    return math.prod(quadrants)


def sol1(filename, size_x, size_y, seconds):
    robots = get_input(filename)
    positions = []
    for robot in robots:
        x, y, v_x, v_y = robot
        f_x = (x + seconds * v_x) % size_x
        f_y = (y + seconds * v_y) % size_y
        positions.append((f_x, f_y))
    return safety_factor(positions, size_x, size_y)


def next_positions(robots, size_x, size_y):
    new_robots = []
    for robot in robots:
        x, y, v_x, v_y = robot
        new_x, new_y = (x + v_x) % size_x, (y + v_y) % size_y
        new_robots.append((new_x, new_y, v_x, v_y))
    return new_robots


def print_region(region, robots):
    min_x = min([r[0] for r in region]) - 6
    max_x = max([r[0] for r in region]) + 6
    min_y = min([r[1] for r in region]) - 6
    max_y = max([r[1] for r in region]) + 6
    positions = set([(robot[0], robot[1]) for robot in robots])
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in positions:
                print(chr(0x1F916), end='')
            else:
                print('  ', end='')
        print()


def print_all_robots(robots, size_x, size_y):
    positions = set([(robot[0], robot[1]) for robot in robots])
    for y in range(size_y):
        for x in range(size_x):
            if (x, y) in positions:
                print('*', end='')
            else:
                print(' ', end='')
        print()


# looking for a region with many robots
def is_tree(robots):
    positions = set([(robot[0], robot[1]) for robot in robots])
    found = set()
    for robot in positions:
        if robot in found:
            continue
        found.add(robot)
        queue = [robot]
        region = {robot}
        while queue:
            r = queue.pop()
            x, y = r
            for n in [(x + d[0], y + d[1]) for d in [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)]]:
                if n in positions and n not in found:
                    region.add(n)
                    queue.append(n)
                    found.add(n)
        if len(region) > len(positions) / 3:
            print_region(region, robots)
            return True
    return False


def sol2(filename, size_x, size_y):
    robots = get_input(filename)
    step = 1
    average_sf = sol1(filename, size_x, size_y, 1)
    while step < size_x * size_y:
        robots = next_positions(robots, size_x, size_y)
        positions = [(robot[0], robot[1]) for robot in robots]
        sf = safety_factor(positions, size_x, size_y)
        # Check if safety factor is small e.g. if some quadrant is relatively empty.
        # If so, check if there is a big region of neighbouring robots
        if sf < average_sf * 9 / 10:
            if is_tree(robots):
                break
        step += 1
    return step


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 11, 7, 100)}')
    print(f'Solution: {sol1("input.txt", 101, 103, 100)}')
    end1 = time.time()
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt", 101, 103)}')
    end2 = time.time()
    print(f'Part 1: {end1 - start:.3f}s, Part 2: {end2 - end1:.3f}s, Tot: {end2 - start:.3f}s')
