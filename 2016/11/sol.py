#!/usr/bin/env python3
import functools
import json
import time
import copy


def get_input(filename):
    f = open(filename, 'r')
    floors = {}
    for line in f:
        floor = int(line.split(':')[0])
        floors[floor] = line.split(':')[1].strip().split()
    f.close()
    return floors


def min_steps(floors, visited, steps):
    #if floors_to_string(floors) in visited:
    #    return float('infinity')
    if not is_valid(floors):
        return float('infinity')
    #new_visited = visited.copy()
    #new_visited.add(floors_to_string(floors))
    if steps > 13:
        return float('infinity')
    if len(floors[1]) == 0 and len(floors[2]) == 0 and len(floors[3]) == 0:
        return steps
    possibilities = next_possibilities(floors)
    poss_steps = []
    for poss in possibilities:
        poss_steps.append(min_steps(poss, visited, steps + 1))
    if len(poss_steps) > 0:
        return min(poss_steps)
    return float('infinity')


def is_valid(floors):
    for floor, objects in floors.items():
        microchips = [x.split('-')[0] for x in objects if x != 'E' and x.split('-')[1] == 'M']
        generators = [x.split('-')[0] for x in objects if x != 'E' and x.split('-')[1] == 'G']
        for elem in microchips:
            if elem not in generators and len(generators) > 0:
                return False
    return True


def floors_to_string(floors):
    s = '{'
    for floor in range(1, 5):
        objects = floors[floor]
        objects.sort()
        s += '"' + str(floor) + '": ' + json.dumps(objects) + ', '
    return s[:-2] + '}'


def string_to_floors(fl_string):
    floors = json.loads(fl_string)
    for i in range(1, 5):
        floors[i] = floors[str(i)]
        del floors[str(i)]
    return floors


def next_possibilities(floors):
    elevator_floor = 0
    for i in range(1, 5):
        if 'E' in floors[i]:
            elevator_floor = i
    objects = floors[elevator_floor].copy()
    objects.remove('E')
    if len(objects) == 0:
        return float('infinity')
    alternatives = []
    for obj in objects:
        if elevator_floor < 4:
            new_floors = copy.deepcopy(floors)
            new_floors[elevator_floor].remove(obj)
            new_floors[elevator_floor].remove('E')
            new_floors[elevator_floor + 1].append(obj)
            new_floors[elevator_floor + 1].append('E')
            alternatives.append(new_floors)
        if elevator_floor > 1:
            new_floors = copy.deepcopy(floors)
            new_floors[elevator_floor].remove(obj)
            new_floors[elevator_floor].remove('E')
            new_floors[elevator_floor - 1].append(obj)
            new_floors[elevator_floor - 1].append('E')
            alternatives.append(new_floors)
        for obj2 in objects:
            if obj == obj2:
                continue
            if elevator_floor < 4:
                new_floors = copy.deepcopy(floors)
                new_floors[elevator_floor].remove(obj)
                new_floors[elevator_floor].remove(obj2)
                new_floors[elevator_floor].remove('E')
                new_floors[elevator_floor + 1].append(obj)
                new_floors[elevator_floor + 1].append(obj2)
                new_floors[elevator_floor + 1].append('E')
                alternatives.append(new_floors)
            if elevator_floor > 1:
                new_floors = copy.deepcopy(floors)
                new_floors[elevator_floor].remove(obj)
                new_floors[elevator_floor].remove(obj2)
                new_floors[elevator_floor].remove('E')
                new_floors[elevator_floor - 1].append(obj)
                new_floors[elevator_floor - 1].append(obj2)
                new_floors[elevator_floor - 1].append('E')
                alternatives.append(new_floors)
    return alternatives


def sol1(filename):
    floors = get_input(filename)
    floors[1].append('E')
    visited = set()
    visited.add(floors_to_string(floors))
    return min_steps(floors, visited, 0)


def sol2(filename):
    _ = get_input(filename)
    return 0


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    #print(f'Solution: {sol1("input.txt")}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    # print('--- Part 2 ---')
    # print(f'Test: {sol2("test.txt")}')
    # print(f'Solution: {sol2("input.txt")}')
    # part2 = time.time()
    # print(f'Elapsed time: {part2 - part1}')
