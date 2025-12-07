#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    lines_raw = f.readlines()
    f.close()
    grid = {}
    for i, lr in enumerate(lines_raw):
        for j, s in enumerate(lr.strip()):
            grid[(i, j)] = s
    return grid


def next_beam(beams, beam_ends, grid, split):
    p = beam_ends.pop(0)
    n = (p[0] + 1, p[1])
    if n not in grid.keys():
        return beams, beam_ends, split
    if grid[n] == '.':
        if n not in beam_ends:
            beam_ends.append(n)
        if n in beams.keys():
            beams[n] += beams[p]
        else:
            beams[n] = beams[p]
        return beams, beam_ends, split
    new_split = False
    for q in [(n[0], n[1] - 1), (n[0], n[1] + 1)]:
        if q in beams.keys():
            beams[q] += beams[p]
        else:
            new_split = True
            beam_ends.append(q)
            beams[q] = beams[p]
    if new_split:
        split += 1
    return beams, beam_ends, split


def sol1(filename):
    grid = get_input(filename)
    beams_ends = [p for p in grid.keys() if grid[p] == 'S']
    beams = {beams_ends[0]: 1}
    split = 0
    while len(beams_ends) > 0:
        beams, beams_ends, split = next_beam(beams, beams_ends, grid, split)
    return split


def sol2(filename):
    grid = get_input(filename)
    beams_ends = [p for p in grid.keys() if grid[p] == 'S']
    beams = {beams_ends[0]: 1}
    split = 0
    while len(beams_ends) > 0:
        beams, beams_ends, split = next_beam(beams, beams_ends, grid, split)
    last_line = max([p[0] for p in grid.keys()])
    return sum([beams[p] for p in grid.keys() if p in beams.keys() if p[0] == last_line])


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
