#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r').read()
    blocks = f.split('\n\n')
    seeds = [int(s) for s in blocks[0].split(': ')[1].split(' ')]
    maps = []
    for i in range(1, len(blocks)):
        m = []
        entries = blocks[i].split('\n')
        for e in entries[1:]:
            m.append([int(n) for n in e.split(' ')])
        maps.append(m)
    return seeds, maps


def get_locations(seeds, maps):
    values = seeds.copy()
    for m in maps:
        for i in range(len(values)):
            for line in m:
                if line[1] <= values[i] < line[1] + line[2]:
                    values[i] = line[0] + values[i] - line[1]
                    break
    return values


def sol1(filename):
    seeds, maps = get_input(filename)
    return min(get_locations(seeds, maps))


def sol2(filename):
    seeds, maps = get_input(filename)
    locations = get_locations(seeds, maps)
    even_locations = [locations[i] for i in range(0, len(locations), 2)]
    min_value = min(even_locations)
    maps.reverse()
    for v in range(min_value - 1):
        value = v
        for m in maps:
            for line in m:
                if line[0] <= value < line[0] + line[2]:
                    value = line[1] + value - line[0]
                    break
        for i in range(int(len(seeds) / 2)):
            if seeds[2 * i] <= value < seeds[2 * i] + seeds[2 * i + 1]:
                return v
    return min_value


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
