#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    reindeers = []
    for line in f:
        speed = int(line.split(' ')[3])
        time = int(line.split(' ')[6])
        rest = int(line.split(' ')[13])
        reindeers.append((speed, time, rest))
    f.close()
    return reindeers


def get_leaders(reindeers, tot_time):
    max_distance = 0
    winning_reindeers = []
    for i, reindeer in enumerate(reindeers):
        speed, time, rest = reindeer
        n_cycle = tot_time // (time + rest)
        distance = n_cycle * speed * time + min(time, tot_time % (time + rest)) * speed
        if distance == max_distance:
            winning_reindeers.append(i)
        if distance > max_distance:
            max_distance = distance
            winning_reindeers = [i]
    return max_distance, winning_reindeers


def sol1(filename, tot_time):
    reindeers = get_input(filename)
    max_distance, _ = get_leaders(reindeers, tot_time)
    return max_distance


def sol2(filename, tot_time):
    reindeers = get_input(filename)
    points = [0] * len(reindeers)
    for t in range(1, tot_time + 1):
        _, leaders = get_leaders(reindeers, t)
        for leader in leaders:
            points[leader] += 1
    return max(points)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 1)}')
    print(f'Test: {sol1("test.txt", 10)}')
    print(f'Test: {sol1("test.txt", 1000)}')
    print(f'Solution: {sol1("input.txt", 2503)}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt", 1000)}')
    print(f'Solution: {sol2("input.txt", 2503)}')
