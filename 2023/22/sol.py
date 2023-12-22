#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    cubes = []
    for line in f:
        a_raw, b_raw = line.strip().split('~')
        a, b = [int(n) for n in a_raw.split(',')], [int(n) for n in b_raw.split(',')]
        cubes.append(((a[0], a[1], a[2]), (b[0], b[1], b[2])))
    f.close()
    return cubes


def get_points(cube):
    a, b = cube
    points = []
    for x in range(a[0], b[0] + 1):
        for y in range(a[1], b[1] + 1):
            for z in range(a[2], b[2] + 1):
                points.append((x, y, z))
    return points


def get_under(cubes):
    under = {}
    for i, cube in cubes.items():
        under[i] = []
        for p in get_points(cube):
            for j, other in cubes.items():
                for q in get_points(other):
                    if (p[0], p[1]) == (q[0], q[1]) and q[2] == p[2] - 1:
                        if i != j and j not in under[i]:
                            under[i].append(j)
    return under


def get_steps_down(cubes, i):
    all_other_points = []
    for j in cubes.keys():
        if j != i:
            all_other_points += get_points(cubes[j])
    ap = set(all_other_points)
    a, b = cubes[i]
    min_z = min(a[2], b[2])
    if min_z == 1:
        return 0
    surface = set([(p[0], p[1]) for p in get_points(cubes[i])])
    under_surface = [p for p in ap if (p[0], p[1]) in surface and p[2] < min_z]
    if len(under_surface) == 0:
        return min_z - 1
    steps = min_z - max([q[2] for q in under_surface]) - 1
    return max(steps, 0)


def move_down(cubes):
    moves = 0
    for i in cubes.keys():
        sd = get_steps_down(cubes, i)
        if sd == 0:
            continue
        a, b = cubes[i]
        cubes[i] = ((a[0], a[1], a[2] - sd), (b[0], b[1], b[2] - sd))
        moves += 1
    return cubes, moves


def settle_down(filename_in, filename_out):
    cubes_list = get_input(filename_in)
    cubes = {}
    for i, cube in enumerate(cubes_list):
        cubes[i] = cube
    while True:
        cubes, moves = move_down(cubes)
        if moves == 0:
            break
    with open(filename_out, 'w') as f:
        for i in range(len(cubes)):
            a, b = cubes[i]
            f.write(str(a[0]) + ',' + str(a[1]) + ',' + str(a[2]) + '~' + str(b[0]) + ',' + str(b[1]) + ',' + str(b[2]))
            f.write('\n')


def will_collapse(cubes, remove, under):
    collapse = set()
    for i in cubes.keys():
        if i in remove:
            continue
        a, b = cubes[i]
        if min(a[2], b[2]) == 1:
            continue
        needs = under[i].copy()
        for r in remove:
            if r in needs:
                needs.remove(r)
        if len(needs) == 0:
            collapse.add(i)
    return collapse


def sol(filename):
    cubes_list = get_input(filename)
    cubes = {}
    for i, cube in enumerate(cubes_list):
        cubes[i] = cube
    under = get_under(cubes)
    tot_safe = 0
    tot_collapse = 0
    for i in range(len(cubes)):
        collapse = {i}
        new_collapse = {i}
        part_collapse = 0
        while len(new_collapse) > 0:
            new_collapse = will_collapse(cubes, collapse, under)
            part_collapse += len(new_collapse)
            collapse = collapse | new_collapse
        tot_collapse += part_collapse
        if part_collapse == 0:
            tot_safe += 1
    return tot_safe, tot_collapse


if __name__ == '__main__':
    print('--- Settling down ... ---')
    settle_down("test.txt", "settled_test.txt")
    settle_down("input.txt", "settled_input.txt")
    print('--- Parts 1 and 2 ---')
    print(f'Test: {sol("settled_test.txt")}')
    print(f'Solution: {sol("settled_input.txt")}')
