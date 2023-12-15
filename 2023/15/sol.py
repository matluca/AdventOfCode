#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r').read()
    return f.strip().split(',')


def get_hash(step):
    res = 0
    for c in step:
        res = ((res + ord(c)) * 17) % 256
    return res


def sol1(filename):
    steps = get_input(filename)
    return sum([get_hash(step) for step in steps])


def sol2(filename):
    steps = get_input(filename)
    boxes = [[] for _ in range(256)]
    for step in steps:
        label = step.split('-')[0] if '-' in step else step.split('=')[0]
        box_n = get_hash(label)
        if step[len(label)] == '-':
            lenses = boxes[box_n]
            for i in range(len(lenses)):
                if lenses[i][0] == label:
                    boxes[box_n] = boxes[box_n][:i] + boxes[box_n][i + 1:]
        elif step[len(label)] == '=':
            n = int(step.split('=')[1])
            lenses = boxes[box_n]
            found = False
            for i in range(len(lenses)):
                if lenses[i][0] == label:
                    boxes[box_n][i] = (label, n)
                    found = True
            if not found:
                boxes[box_n].append((label, n))
    res = 0
    for i, box in enumerate(boxes):
        for j, l in enumerate(box):
            res += (i + 1) * (j + 1) * l[1]
    return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
