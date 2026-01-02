#!/usr/bin/env python3
from collections import deque

def get_input(filename):
    games = []
    f = open(filename, 'r')
    for line in f.readlines():
        pl, lm = int(line.split()[0]), int(line.split()[-2])
        games.append((pl, lm))
    f.close()
    return games


def play(game):
    n_players, last_marble = game
    circle = deque([0])
    scores = {}
    for player in range(n_players):
        scores[player] = 0
    for marble in range(1, last_marble + 1):
        if marble % 23 != 0:
            circle.rotate(-1)
            circle.append(marble)
        else:
            circle.rotate(7)
            scores[marble % n_players] += marble + circle.pop()
            circle.rotate(-1)
    return max(scores.values())


def sol1(filename):
    games = get_input(filename)
    return [play(game) for game in games]


def sol2(filename):
    games = get_input(filename)
    return [play((game[0], game[1] * 100)) for game in games]


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
