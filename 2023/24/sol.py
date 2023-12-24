#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    hailstones = []
    for line in f:
        pos, vel = line.strip().split(' @ ')
        hailstones.append(([int(p) for p in pos.split(', ')], [int(v) for v in vel.split(', ')]))
    f.close()
    return hailstones


def intersection(h1, h2):
    if h1 == h2:
        return None
    p1, v1 = h1
    p2, v2 = h2
    m1 = float(v1[1] / v1[0])
    b1 = p1[1] - float(v1[1] / v1[0] * p1[0])
    m2 = float(v2[1] / v2[0])
    b2 = p2[1] - float(v2[1] / v2[0] * p2[0])
    if m1 == m2:
        return None
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    t1 = (x - p1[0]) / v1[0]
    t2 = (x - p2[0]) / v2[0]
    return x, y, t1, t2


def sol1(filename, minimum, maximum):
    hailstones_full = get_input(filename)
    hailstones = [(h[0][:2], h[1][:2]) for h in hailstones_full]
    tot = 0
    for i, h1 in enumerate(hailstones):
        for h2 in hailstones[i + 1:]:
            inters = intersection(h1, h2)
            if inters is None:
                continue
            x, y, t1, t2 = inters
            if t1 < 0 or t2 < 0:
                continue
            if minimum <= x < maximum and minimum <= y < maximum:
                tot += 1
    return tot


def sol2(filename):
    hailstones = get_input(filename)
    for hailstone in hailstones[:4]:
        pos, vel = hailstone
        x, y, z = pos
        vx, vy, vz = vel
        eq = f'(x-{x})/(a-{vx})=(y-{y})/(b-{vy})=(z-{z})/(c-{vz})'
        eq = eq.replace('--', '+')
        print(eq)
    return "Solve with Wolfram Alpha"


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 7, 27)}')
    print(f'Solution: {sol1("input.txt", 200000000000000, 400000000000000)}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
