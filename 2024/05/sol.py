#!/usr/bin/env python3

import time


def get_input(filename):
    f = open(filename, 'r')
    rules_raw, updates_raw = f.read().strip().split('\n\n')
    f.close()
    rules = []
    for r in rules_raw.split('\n'):
        rules.append((int(r.split('|')[0]), int(r.split('|')[1])))
    updates = []
    for u in updates_raw.split('\n'):
        updates.append([int(x) for x in u.split(',')])
    return rules, updates


def build_graph(rules):
    graph = {}
    for rule in rules:
        a, b = rule
        if a not in graph.keys():
            graph[a] = [b]
        else:
            graph[a].append(b)
    return graph


def is_valid(update, graph):
    valid = True
    for i in range(len(update) - 1):
        a = update[i]
        for b in update[i + 1:]:
            if b in graph.keys() and a in graph[b]:
                valid = False
                break
    return valid


def sol1(filename):
    rules, updates = get_input(filename)
    tot = 0
    graph = build_graph(rules)
    for update in updates:
        if is_valid(update, graph):
            tot += update[int((len(update) - 1) / 2)]
    return tot


def get_order(update, graph):
    ordered = []
    for b in update:
        for a in ordered:
            if b in graph.keys() and a in graph[b]:
                i_a = ordered.index(a)
                ordered.insert(i_a, b)
                break
        if b not in ordered:
            ordered.append(b)
    return ordered


def sol2(filename):
    rules, updates = get_input(filename)
    graph = build_graph(rules)
    tot = 0
    for update in updates:
        if not is_valid(update, graph):
            ordered = get_order(update, graph)
            tot += ordered[int((len(ordered) - 1) / 2)]
    return tot


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    end1 = time.time()
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    end2 = time.time()
    print(f'Part 1: {end1 - start:.3f}s, Part 2: {end2 - end1:.3f}s, Tot: {end2 - start:.3f}s')
