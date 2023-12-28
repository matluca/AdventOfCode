#!/usr/bin/env python3
import functools


def get_input(filename):
    f = open(filename, 'r')
    data = []
    for line in f:
        data.append(int(line.strip().split(': ')[1]))
    f.close()
    return data[0], data[1]


spell_cost = [53, 73, 113, 173, 229]


@functools.cache
def min_cost(points, mana, opp_points, opp_damage, spells_tuple, turn, cost, part):
    if part == 2 and turn == 0:
        points -= 1
    if points <= 0:
        return float('infinity')
    if opp_points <= 0:
        return cost

    spells = list(spells_tuple)
    if spells[2] > 0:  # apply shield
        spells[2] -= 1
    if spells[3] > 0:  # apply poison
        opp_points -= 3
        spells[3] -= 1
    if spells[4] > 0:  # apply recharge
        mana += 101
        spells[4] -= 1

    if opp_points <= 0:
        return cost

    # do boss turn
    if turn == 1:
        armor = 0
        if spells[2] > 0:
            armor = 7
        points -= max(opp_damage - armor, 1)
        if points <= 0:
            return float('infinity')
        return min_cost(points, mana, opp_points, opp_damage, tuple(spells), 0, cost, part)

    # do player's turn - select new spell
    allowed_spells = []
    for i in range(len(spell_cost)):
        if spells[i] == 0 and spell_cost[i] <= mana:
            allowed_spells.append(i)
    minimum_cost = float('infinity')
    for selected_spell in allowed_spells:
        new_opp_points = opp_points
        new_points = points
        new_spells = spells.copy()
        if selected_spell == 0:  # apply magic missile
            new_opp_points -= 4
        if selected_spell == 1:  # apply drain
            new_opp_points -= 2
            new_points += 2
        if selected_spell == 2:  # start shield
            new_spells[2] = 6
        if selected_spell == 3:  # start poison
            new_spells[3] = 6
        if selected_spell == 4:  # start recharge
            new_spells[4] = 5
        new_cost = min_cost(new_points, mana - spell_cost[selected_spell], new_opp_points, opp_damage, tuple(new_spells), 1, cost + spell_cost[selected_spell], part)
        if new_cost < minimum_cost:
            minimum_cost = new_cost
    return minimum_cost


def sol1(filename):
    opp_points, opp_damage = get_input(filename)
    points, mana, armor = 50, 500, 0
    spells = (0, 0, 0, 0, 0)
    turn = 0
    cost = 0
    print("Test: " + str(min_cost(2, 1000, 2, 5, (0, 0, 0, 3, 0), 0, 5, 1)))
    print("Test: " + str(min_cost(10, 250, 13, 8, spells, 0, 0, 1)))
    print("Test: " + str(min_cost(10, 250, 14, 8, spells, 0, 0, 1)))
    return min_cost(points, mana, opp_points, opp_damage, tuple(spells), turn, cost, 1)


def sol2(filename):
    opp_points, opp_damage = get_input(filename)
    points, mana, armor = 50, 500, 0
    spells = (0, 0, 0, 0, 0)
    turn = 0
    cost = 0
    return min_cost(points, mana, opp_points, opp_damage, tuple(spells), turn, cost, 2)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
