#!/usr/bin/env python3
import math
import time


def get_input(filename):
    f = open(filename, 'r')
    raw = f.read().strip()
    f.close()
    return int(raw)


def n_steps(elves):
    presents = {}
    for i in range(elves):
        presents[i] = 1
    pos = 0
    while sum([p != 0 for p in presents.values()]) > 1:
        if presents[pos] == 0:
            pos = (pos + 1) % elves
            continue
        for i in range(1, elves - 1):
            j = (pos + i) % elves
            if presents[j] != 0:
                presents[pos] += presents[j]
                presents[j] = 0
                break
        pos = (pos + 1) % elves
    return [x for x in presents.keys() if presents[x] != 0][0]


def sol1(filename):
    elves = get_input(filename)
    # for n in range(3, 65):
    #     print(n, n_steps(n), (n - 2**int(math.log2(n))) * 2)
    return (elves - 2**int(math.log2(elves))) * 2 + 1


def n_steps_2(elves):
    people = [i + 1 for i in range(elves)]
    current = 1
    while len(people) > 1:
        pos = people.index(current)
        steal = (pos + len(people) // 2) % len(people)
        people.remove(people[steal])
        pos = people.index(current)
        current = people[(pos + 1) % len(people)]
    return people[0]


def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))


def sol2(filename):
    elves = get_input(filename)
    # for n in range(2, 100):
    #     print(n, ternary(n - 1), n_steps_2(n), n - 3**int(math.log(n - 1, 3)))
    return elves - 3**int(math.log(elves - 1, 3))


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
