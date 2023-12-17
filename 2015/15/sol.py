#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    ingredients = []
    calories = []
    for line in f:
        s = line.strip().split(': ')[1].split(', ')
        properties = [r.split(' ') for r in s][:-1]
        ingredients.append(tuple([int(p[1]) for p in properties]))
        calories.append(int(s[-1].split(' ')[-1]))
    f.close()
    return ingredients, calories


def find_combinations(target_sum, num_elements, current_combination, result):
    if target_sum == 0 and num_elements == 0:
        result.append(current_combination.copy())
        return
    if target_sum < 0 or num_elements == 0:
        return
    for i in range(1, target_sum + 1):
        current_combination.append(i)
        find_combinations(target_sum - i, num_elements - 1, current_combination, result)
        current_combination.pop()


def all_combinations(target_sum, num_elements):
    result = []
    find_combinations(target_sum, num_elements, [], result)
    return result


def sol1(filename):
    ingredients, _ = get_input(filename)
    max_res = 0
    for comb in all_combinations(100, len(ingredients)):
        res = 1
        for i in range(len(ingredients[0])):
            s = sum([comb[j] * ingredients[j][i] for j in range(len(comb))])
            res *= max(s, 0)
        if res > max_res:
            max_res = res
    return max_res


def sol2(filename):
    ingredients, calories = get_input(filename)
    max_res = 0
    for comb in all_combinations(100, len(ingredients)):
        res = 1
        for i in range(len(ingredients[0])):
            s = sum([comb[j] * ingredients[j][i] for j in range(len(comb))])
            res *= max(s, 0)
        tot_calories = sum([comb[j] * calories[j] for j in range(len(comb))])
        if res > max_res and tot_calories == 500:
            max_res = res
    return max_res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
