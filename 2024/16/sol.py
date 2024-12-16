#!/usr/bin/env python3

import time
from termcolor import colored


def get_input(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    grid = {}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            grid[(i,j)] = lines[i][j]
    return grid


def next_in_direction(status):
    position, direction = status
    return (position[0] + direction[0], position[1] + direction[1]), direction


def rotate(status, grid):
    position, direction = status
    next_status = []
    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if d == direction or (d[0] == -direction[0] and d[1] == -direction[1]):
            continue
        if grid[(position[0] + d[0], position[1] + d[1])] != '#':
            next_status.append((position, d))
    return next_status


def dijkstra(grid, status, end):
    scores = {(node, d): float('infinity') for node in grid for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]}
    best_seats = {(node, d): {node} for node in grid for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]}
    queue = [(0, status, status[0], status[1])]
    while queue:
        queue.sort()
        current_score, current_status, predecessor, previous_dir = queue.pop(0)
        if current_score > scores[current_status]:
            continue
        scores[current_status] = current_score
        if current_score < scores[current_status]:
            best_seats[current_status] = set(current_status[0])
        for b in best_seats[(predecessor, previous_dir)]:
            best_seats[current_status].add(b)
        if current_status[0] == end:
            return scores[current_status], best_seats[current_status]
        next_status_in_direction = next_in_direction(current_status)
        if grid[next_status_in_direction[0]] != '#':
            if next_status_in_direction:
                queue.append((current_score + 1, next_status_in_direction, current_status[0], current_status[1]))
        for next_status_rotate in rotate(current_status, grid):
            if grid[next_status_rotate[0]] != '#':
                queue.append((current_score + 1000, next_status_rotate, current_status[0], current_status[1]))


def print_path(grid, best_seats):
    size_x = max([p[0] for p in grid.keys()])
    size_y = max([p[1] for p in grid.keys()])
    for i in range(size_x + 1):
        for j in range(size_y):
            if (i, j) in best_seats:
                print(colored('O', 'red'), end='')
            else:
                print(grid[(i, j)], end='')
        print()


def sol(filename):
    grid = get_input(filename)
    start = [p for p in grid.keys() if grid[p] == 'S'][0]
    end = [p for p in grid.keys() if grid[p] == 'E'][0]
    direction = (0, 1)
    status = (start, direction)
    best_score, best_seats =  dijkstra(grid, status, end)
    # print_path(grid, best_seats)
    return best_score, len(best_seats)


if __name__ == '__main__':
    start_time = time.time()
    print('--- Both parts ---')
    print(f'Test 1: {sol("test1.txt")}')
    print(f'Test 2: {sol("test2.txt")}')
    print(f'Solution: {sol("input.txt")}')
    end_time = time.time()
    print(f'Both parts: {end_time - start_time:.3f}s')
