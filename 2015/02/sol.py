#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    boxes = []
    for line in f:
        boxes.append([int(n) for n in line.strip().split('x')])
    f.close()
    return boxes


def sol1(filename):
    boxes = get_input(filename)
    res = 0
    for box in boxes:
        a, b, c = box[0], box[1], box[2]
        res += 2 * a * b + 2 * a * c + 2 * b * c + min([a * b, b * c, a * c])
    return res


def sol2(filename):
    boxes = get_input(filename)
    res = 0
    for box in boxes:
        a, b, c = box[0], box[1], box[2]
        res += a * b * c + 2 * min([a + b, b + c, a + c])
    return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
