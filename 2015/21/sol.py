#!/usr/bin/env python3
from itertools import chain, combinations


weapons = [(8, 4), (10, 5), (25, 6), (40, 7), (74, 8)]
armors = [(0, 0), (13, 1), (31, 2), (53, 3), (75, 4), (102, 5)]
rings_damage = [(25, 1), (50, 2), (100, 3)]
rings_armor = [(20, 1), (40, 2), (80, 3)]


def get_input(filename):
    f = open(filename, 'r')
    data = []
    for line in f:
        data.append(int(line.strip().split(': ')[1]))
    f.close()
    return data


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def sol1(filename):
    data = get_input(filename)
    _, opp_damage, opp_armor = data[0], data[1], data[2]
    min_cost = 1000
    for weapon in weapons:
        for armor in armors:
            for ring_armor in powerset(rings_armor):
                for ring_damage in powerset(rings_damage):
                    cost = weapon[0] + armor[0] + sum(ra[0] for ra in ring_armor) + sum(rd[0] for rd in ring_damage)
                    my_damage = weapon[1] + sum(rd[1] for rd in ring_damage)
                    my_armor = armor[1] + sum(ra[1] for ra in ring_armor)
                    if my_damage + my_armor >= opp_damage + opp_armor and cost < min_cost:
                        min_cost = cost
    return min_cost


def sol2(filename):
    data = get_input(filename)
    _, opp_damage, opp_armor = data[0], data[1], data[2]
    max_cost = 0
    for weapon in weapons:
        for armor in armors:
            for ring_armor in powerset(rings_armor):
                for ring_damage in powerset(rings_damage):
                    cost = weapon[0] + armor[0] + sum(ra[0] for ra in ring_armor) + sum(rd[0] for rd in ring_damage)
                    my_damage = weapon[1] + sum(rd[1] for rd in ring_damage)
                    my_armor = armor[1] + sum(ra[1] for ra in ring_armor)
                    if my_damage + my_armor < opp_damage + opp_armor and cost > max_cost:
                        max_cost = cost
    return max_cost


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
