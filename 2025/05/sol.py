#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    ranges_raw, ingredients_raw = f.read().strip().split('\n\n')
    f.close()
    ranges = []
    for r in ranges_raw.split('\n'):
        ranges.append((int(r.split('-')[0]), int(r.split('-')[1])))
    ingredients = [int(i) for i in ingredients_raw.split('\n')]
    return ranges, ingredients


def sol1(filename):
    ranges, ingredients = get_input(filename)
    tot = 0
    for ingredient in ingredients:
        for r in ranges:
            if r[0] <= ingredient <= r[1]:
                tot += 1
                break
    return tot


def sol2(filename):
    ranges, _ = get_input(filename)
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    simplified_ranges = [sorted_ranges[0]]
    for r in sorted_ranges[1:]:
        last_range = simplified_ranges[-1]
        if r[0] > last_range[1] + 1:
            simplified_ranges.append(r)
        elif r[1] > last_range[1]:
            simplified_ranges[-1] = (last_range[0], r[1])
    tot = 0
    for r in simplified_ranges:
        tot += r[1] - r[0] + 1
    return tot


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
