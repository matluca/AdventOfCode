#!/usr/bin/env python3

def sol1(filename):
    f = open(filename, 'r')
    res = 0
    for line in f:
        new_l = ""
        for c in line:
            if c.isdigit():
                new_l = new_l + c
        new_l = new_l[0] + new_l[len(new_l) - 1]
        res += int(new_l)
    f.close()
    return res


number_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def sol2(filename):
    f = open(filename, 'r')
    res = 0
    for line in f:
        for key, n in number_map.items():
            line = line.replace(key, key + str(n) + key)
        new_l = ""
        for c in line:
            if c.isdigit():
                new_l = new_l + c
        new_l = new_l[0] + new_l[len(new_l) - 1]
        res += int(new_l)
    f.close()
    return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
