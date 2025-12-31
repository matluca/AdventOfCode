#!/usr/bin/env python3

class Particle:
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a

    def move(self):
        for i in range(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]


def get_input(filename):
    f = open(filename, 'r')
    particles = {}
    for i, line in enumerate(f.readlines()):
        p0_raw = line.split('<')[1].split('>')[0]
        p0 = [int(x) for x in p0_raw.split(',')]
        v0_raw = line.split('<')[2].split('>')[0]
        v0 = [int(x) for x in v0_raw.split(',')]
        a_raw = line.split('<')[3].split('>')[0]
        a = [int(x) for x in a_raw.split(',')]
        particles[i] = Particle(p0, v0, a)
    f.close()
    return particles


def sol1(filename):
    particles = get_input(filename)
    min_d = float('infinity')
    min_particle = -1
    for i, p in particles.items():
        if abs(p.a[0]) + abs(p.a[1]) + abs(p.a[2]) < min_d:
            min_d = abs(p.a[0]) + abs(p.a[1]) + abs(p.a[2])
            min_particle = i
    return min_particle


def sol2(filename):
    particles = get_input(filename)
    max_p = max(particles.keys())
    for t in range(50):
        for part in particles.values():
            part.move()
        for i in range(max_p):
            if i not in particles.keys():
                continue
            collision = False
            for j in range(i + 1, max_p + 1):
                if j not in particles.keys():
                    continue
                if particles[i].p == particles[j].p:
                    collision = True
                    del particles[j]
            if collision:
                del particles[i]
    return len(particles)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
