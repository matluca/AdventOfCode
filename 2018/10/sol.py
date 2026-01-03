#!/usr/bin/env python3
import itertools


def get_input(filename):
    particles = []
    f = open(filename, 'r')
    for line in f.readlines():
        x = int(line.split('<')[1].split(',')[0])
        y = int(line.split(',')[1].split('>')[0])
        vx = int(line.split('<')[2].split(',')[0])
        vy = int(line.split(',')[2].split('>')[0])
        particles.append((x, y, vx, vy))
    f.close()
    return particles


def score(particles):
    s = 0
    for pair in itertools.combinations(particles, 2):
        part1, part2 = pair
        s += abs(part1[0] - part2[0]) + abs(part1[1] - part2[1])
    return s


def move(p, t):
    return p[0] + p[2] * t, p[1] + p[3] * t, p[2], p[3]


def print_particles(particles):
    particles = [(p[0], p[1]) for p in particles]
    min_x, max_x = min([p[0] for p in particles]), max([p[0] for p in particles])
    min_y, max_y = min([p[1] for p in particles]), max([p[1] for p in particles])
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            if (x, y) in particles:
                print('#', end='')
            else:
                print('.', end='')
        print()


def sol(filename):
    particles = get_input(filename)
    min_score = score(particles)
    t = int(min([abs(p[0] / p[2]) for p in particles if p[2] != 0]))
    new_particles = []
    for particle in particles:
        new_particles.append(move(particle, t))
    particles = new_particles
    while True:
        t += 1
        new_particles = []
        for particle in particles:
            new_particles.append(move(particle, 1))
        if score(new_particles) < min_score:
            min_score = score(new_particles)
            particles = new_particles
        else:
            break
    print_particles(particles)
    return t - 1


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol("test.txt")}')
    print(f'Solution: {sol("input.txt")}')
