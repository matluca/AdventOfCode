#!/usr/bin/env python3

def get_input(filename):
    points = []
    f = open(filename, 'r')
    for line in f.readlines():
        points.append(tuple(reversed([int(x) for x in line.strip().split(',')])))
    f.close()
    return points


def distance(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def closest_point(q, points):
    if q == points[0]:
        return 'a'
    min_d = distance(points[0], q)
    closest = 'a'
    for i, point in enumerate(points):
        if i == 0:
            continue
        d = distance(point, q)
        if d == min_d:
            closest = '.'
        elif d < min_d:
            closest = chr(i + ord('a'))
            min_d = d
    return closest


def print_closest(closest):
    keys = closest.keys()
    for i in range(min([p[0] for p in keys]), max([p[0] for p in keys]) + 1):
        for j in range(min([p[1] for p in keys]), max([p[1] for p in keys]) + 1):
            print(closest[(i, j)], end='')
        print()


def sol1(filename):
    points = get_input(filename)
    closest = {}
    for i in range(min([p[0] for p in points]) - 1, max([p[0] for p in points]) + 2):
        for j in range(min([p[1] for p in points]) - 1, max([p[1] for p in points]) + 2):
            closest[(i, j)] = closest_point((i, j), points)
    labels = set(closest.values())
    labels.remove('.')
    for i in [min([p[0] for p in points]) - 1, max([p[0] for p in points]) + 1]:
        for j in [min([p[1] for p in points]) - 1, max([p[1] for p in points]) + 1]:
            if closest[(i, j)] in labels:
                labels.remove(closest[(i, j)])
    return max([sum([1 for v in closest.values() if v == label]) for label in labels])


def sol2(filename, limit):
    points = get_input(filename)
    res = 0
    for i in range(min([p[0] for p in points]) - 1, max([p[0] for p in points]) + 2):
        for j in range(min([p[1] for p in points]) - 1, max([p[1] for p in points]) + 2):
            d = 0
            for point in points:
                d += distance(point, (i, j))
                if d >= limit:
                    break
            if d < limit:
                res += 1
    return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt", 32)}')
    print(f'Solution: {sol2("input.txt", 10000)}')
