#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    n_steps = [line.strip() for line in f.readlines()]
    f.close()
    return n_steps


def sol1(filename):
    n_steps = get_input(filename)
    res = []
    for steps in n_steps:
        recipes = '37'
        positions = [0, 1]
        while len(recipes) < int(steps) + 10:
            v0, v1 = int(recipes[positions[0]]), int(recipes[positions[1]])
            sc = str(v0 + v1)
            recipes += sc
            positions[0] = (positions[0] + 1 + v0) % len(recipes)
            positions[1] = (positions[1] + 1 + v1) % len(recipes)
        res.append(int(recipes[int(steps): int(steps) + 10]))
    return res


def sol2(filename):
    n_steps = get_input(filename)
    res = []
    for steps in n_steps:
        recipes = '37'
        positions = [0, 1]
        while True:
            v0, v1 = int(recipes[positions[0]]), int(recipes[positions[1]])
            sc = str(v0 + v1)
            recipes += sc
            positions[0] = (positions[0] + 1 + v0) % len(recipes)
            positions[1] = (positions[1] + 1 + v1) % len(recipes)
            l = len(str(steps))
            if len(recipes) < l:
                continue
            check1 = recipes[-l:]
            check2 = recipes[-l - 1:-1]
            if steps == check1:
                res.append(len(recipes) - l)
                break
            if steps == check2:
                res.append(len(recipes) - l - 1)
                break
    return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
