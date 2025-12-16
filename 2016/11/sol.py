#!/usr/bin/env python3
import json
import time
import copy
from functools import cmp_to_key
from cachetools import cached
from cachetools.keys import hashkey


def get_input(filename):
    f = open(filename, 'r')
    floors = {}
    for line in f:
        floor = int(line.split(':')[0])
        floors[floor] = line.split(':')[1].strip().split()
    f.close()
    return floors


def is_valid(floors):
    for floor, objects in floors.items():
        microchips = [x.split('-')[0] for x in objects if x != 'E' and x.split('-')[1] == 'M']
        generators = [x.split('-')[0] for x in objects if x != 'E' and x.split('-')[1] == 'G']
        for elem in microchips:
            if elem not in generators and len(generators) > 0:
                return False
    return True


def combinations(floors):
    locations = {}
    elements = set()
    for floor, objects in floors.items():
        for obj in objects:
            locations[obj] = floor
            elements.add(obj.split('-')[0])
    combs = []
    for element in elements:
        if element == 'E':
            continue
        a, b = locations[element + '-M'], locations[element + '-G']
        combs.append((min(a, b), max(a, b)))
    combs.sort()
    return locations['E'], tuple(combs)


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
    for i, obj in enumerate(objects):
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
        for j, obj2 in enumerate(objects):
            if j <= i:
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
                if obj.split('-')[0] != obj2.split('-')[0]:
                    continue
                new_floors = copy.deepcopy(floors)
                new_floors[elevator_floor].remove(obj)
                new_floors[elevator_floor].remove(obj2)
                new_floors[elevator_floor].remove('E')
                new_floors[elevator_floor - 1].append(obj)
                new_floors[elevator_floor - 1].append(obj2)
                new_floors[elevator_floor - 1].append('E')
                alternatives.append(new_floors)
    return [alt for alt in alternatives if is_valid(alt)]


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


def state_distance(state):
    floors_str, _ = state
    return distance(floors_str)


def distance(floors_str):
    d = 0
    floors = string_to_floors(floors_str)
    for i, floor in floors.items():
        d += (4 - i) * len(floor)
    return d


def compare_states(state1, state2):
    floors1, steps1 = state1
    floors2, steps2 = state2
    if distance(floors1) < distance(floors2):
        return -1
    if distance(floors1) > distance(floors2):
        return 1
    if steps1 < steps2:
        return -1
    if steps1 > steps2:
        return 1
    return 0


@cached(cache={}, key=lambda floors: hashkey(floors_to_string(floors)))
def bfs(floors):
    queue = [(floors_to_string(floors), 0)]
    visited = set(floors_to_string(floors))
    visited_combs = set(combinations(floors))
    while queue:
        queue.sort(key=cmp_to_key(compare_states))
        current_state = queue.pop(0)
        current_floors_str, current_steps = current_state
        if distance(current_floors_str) == 0:
            return current_steps
        current_floors = string_to_floors(current_floors_str)
        for poss in next_possibilities(current_floors):
            poss_str = floors_to_string(poss)
            if poss_str not in visited and combinations(poss) not in visited_combs:
                visited.add(poss_str)
                queue.append((poss_str, current_steps + 1))
    return None



def sol1(filename):
    floors = get_input(filename)
    floors[1].append('E')
    return bfs(floors)


def sol2(filename):
    floors = get_input(filename)
    floors[1].append('E')
    return bfs(floors) + 12 + 12


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
