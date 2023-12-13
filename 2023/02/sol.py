#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    games = {}
    for line in f:
        line = line.strip()
        game = int(line.split(':')[0].split(' ')[1])
        selections = []
        for s in line.split(':')[1].split(';'):
            selection = {'red': 0, 'green': 0, 'blue': 0}
            for single in s.split(','):
                selection[single.split(' ')[2]] = int(single.split(' ')[1])
            selections.append(selection)
        games[game] = selections
    f.close()
    return games


def sol1(filename):
    games = get_input(filename)
    res = 0
    for game, selections in games.items():
        allowed = True
        for sel in selections:
            if sel['red'] > 12 or sel['green'] > 13 or sel['blue'] > 14:
                allowed = False
                break
        if allowed:
            res += game
    return res


def sol2(filename):
    games = get_input(filename)
    res = 0
    for selections in games.values():
        reds, greens, blues = [], [], []
        for sel in selections:
            reds.append(sel['red'])
            greens.append(sel['green'])
            blues.append(sel['blue'])
        res += max(reds) * max(greens) * max(blues)
    return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
