#!/usr/bin/env python3

def get_input(filename):
    needs = {}
    all = set()
    f = open(filename, 'r')
    for line in f.readlines():
        a, b = line.split()[1], line.split()[7]
        if b not in needs.keys():
            needs[b] = []
        needs[b].append(a)
        all.add(a)
        all.add(b)
    f.close()
    return needs, all


def sol1(filename):
    needs, all = get_input(filename)
    path = ''
    while len(path) < len(all):
        possibilities = [l for l in all if l not in path and (l not in needs.keys() or len(needs[l]) == 0)]
        possibilities.sort()
        poss = possibilities[0]
        path += poss
        for l in needs.keys():
            if poss in needs[l]:
                needs[l].remove(poss)
    return path


def sol2(filename, workers, offset):
    needs, all = get_input(filename)
    t = -1
    free = {}
    for worker in range(workers):
        free[worker] = None
    path = ''
    waiting = set()
    while len(path) < len(all):
        t += 1
        for worker in free.keys():
            f = free[worker]
            if f is not None and f[1] == t:
                free[worker] = None
                path += f[0]
                waiting.remove(f[0])
                for l in needs.keys():
                    if f[0] in needs[l]:
                        needs[l].remove(f[0])
        free_workers = []
        for worker in range(workers):
            if free[worker] is None:
                free_workers.append(worker)
        if len(free_workers) == 0:
            continue
        possibilities = [l for l in all if l not in path and (l not in needs.keys() or len(needs[l]) == 0) and l not in waiting]
        possibilities.sort()
        while len(possibilities) > 0 and len(free_workers) > 0:
            poss = possibilities.pop(0)
            free_worker = free_workers.pop(0)
            free[free_worker] = (poss, t + offset + ord(poss) - ord('A') + 1)
            waiting.add(poss)
    return t


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt", 2, 0)}')
    print(f'Solution: {sol2("input.txt", 5, 60)}')
