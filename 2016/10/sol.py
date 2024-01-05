#!/usr/bin/env python3
import time


def get_input(filename):
    f = open(filename, 'r')
    values = {}
    links = {}
    for line in f:
        if line.startswith('value'):
            v, bot = int(line.split()[1]), int(line.split()[5])
            if bot not in values.keys():
                values[bot] = []
            values[bot].append(v)
        else:
            bot, low, high = int(line.split()[1]), int(line.split()[6]), int(line.split()[11])
            if line.split()[5] == 'output':
                low += 1000
            if line.split()[10] == 'output':
                high += 1000
            links[bot] = (low, high)
    f.close()
    return values, links


def apply_rules(values, links):
    queue = []
    for bot, v in values.items():
        if len(v) == 2:
            queue.append(bot)
    while queue:
        bot = queue.pop(0)
        low = min(values[bot])
        high = max(values[bot])
        if links[bot][0] not in values.keys():
            values[links[bot][0]] = []
        values[links[bot][0]].append(low)
        if links[bot][0] < 1000 and len(values[links[bot][0]]) == 2:
            queue.append(links[bot][0])
        if links[bot][1] not in values.keys():
            values[links[bot][1]] = []
        values[links[bot][1]].append(high)
        if links[bot][1] < 1000 and len(values[links[bot][1]]) == 2:
            queue.append(links[bot][1])
    return values


def sol1(filename, a, b):
    values, links = get_input(filename)
    values = apply_rules(values, links)
    for bot, v in values.items():
        if a in v and b in v:
            return bot
    return 0


def sol2(filename):
    values, links = get_input(filename)
    values = apply_rules(values, links)
    return values[1000][0] * values[1001][0] * values[1002][0]


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 2, 5)}')
    print(f'Solution: {sol1("input.txt", 17, 61)}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
