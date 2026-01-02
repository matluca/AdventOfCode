#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    rects = []
    for line in f.readlines():
        vertex = tuple([int(x) for x in line.split()[2].split(':')[0].split(',')])
        size = tuple([int(x) for x in line.split(': ')[1].split('x')])
        rects.append((vertex, size))
    f.close()
    return rects


def is_in(x, y, rect):
    return rect[0][0] <= x < rect[0][0] + rect[1][0] and rect[0][1] <= y < rect[0][1] + rect[1][1]


def intersection(rect1, rect2):
    for i in range(rect1[0][0], rect1[0][0] + rect1[1][0]):
        for j in range(rect1[0][1], rect1[0][1] + rect1[1][1]):
            if is_in(i, j, rect2):
                return True
    return False


def sol1(filename):
    rects = get_input(filename)
    intersections = {}
    size_x = max([rect[0][0] + rect[1][0] for rect in rects]) + 1
    size_y = max([rect[0][0] + rect[1][0] for rect in rects]) + 1
    for i in range(size_x):
        for j in range(size_y):
            for rect in rects:
                if is_in(i, j, rect):
                    if (i, j) not in intersections.keys():
                        intersections[(i, j)] = 0
                    intersections[(i, j)] += 1
    return sum([1 for v in intersections.values() if v > 1])


def sol2(filename):
    rects = get_input(filename)
    for i, rect1 in enumerate(rects):
        found = True
        for j, rect2 in enumerate(rects):
            if i == j:
                continue
            if intersection(rect1, rect2):
                found = False
                break
        if found:
            return i + 1
    return 0


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
