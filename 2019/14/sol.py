#!/usr/bin/env python3

def get_input(filename):
    reactions = []
    f = open(filename, 'r')
    for line in f.readlines():
        left, right = line.split(' => ')
        product = (right.split()[1], int(right.split()[0]))
        reagents = left.split(', ')
        resources = []
        for reagent in reagents:
            resources.append((reagent.split()[1], int(reagent.split()[0])))
        reactions.append((resources, product))
    f.close()
    return reactions


def is_over(needed):
    for k, v in needed.items():
        if k != 'ORE' and v > 0:
            return False
    return True


def get_resources(reactions, element):
    for reaction in reactions:
        if reaction[1][0] == element:
            return reaction[1][1], reaction[0]


def get_needed_ore(fuel, reactions, elements):
    needed = {e: 0 for e in elements}
    needed['FUEL'] = fuel
    rest = {e: 0 for e in elements}
    while not is_over(needed):
        element = [e for e in needed if needed[e] > 0 and e != 'ORE'][0]
        need_amount = needed[element]
        can_create, resources = get_resources(reactions, element)
        m = (need_amount - rest[element]) // can_create
        if (need_amount - rest[element]) % can_create > 0:
            m += 1
        for resource in resources:
            needed[resource[0]] += resource[1] * m
        rest[element] += m * can_create - need_amount
        needed[element] = 0
    return needed['ORE']


def sol1(filename):
    reactions = get_input(filename)
    elements = set()
    for reaction in reactions:
        for resource in reaction[0]:
            elements.add(resource[0])
        elements.add(reaction[1][0])
    return get_needed_ore(1, reactions, elements)


def sol2(filename):
    reactions = get_input(filename)
    elements = set()
    for reaction in reactions:
        for resource in reaction[0]:
            elements.add(resource[0])
        elements.add(reaction[1][0])
    a, b = 0, 1000000000000
    while b - a > 1:
        m = (a + b) // 2
        if get_needed_ore(m, reactions, elements) < 1000000000000:
            a = m
        else:
            b = m
    return a


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
