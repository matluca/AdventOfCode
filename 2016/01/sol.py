#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r').read()
    return f.strip().split(', ')


north, east, south, west = complex(-1, 0), complex(0, 1), complex(1, 0), complex(0, -1)


def apply_move(move, pos, direction):
    turn = move[0]
    amount = int(move[1:])
    if turn == 'R':
        if direction == north:
            direction = east
        elif direction == east:
            direction = south
        elif direction == south:
            direction = west
        elif direction == west:
            direction = north
    elif turn == 'L':
        if direction == north:
            direction = west
        elif direction == east:
            direction = north
        elif direction == south:
            direction = east
        elif direction == west:
            direction = south
    pos = pos + amount * direction
    return pos, direction


def apply_move_2(move, pos, direction, visited):
    turn = move[0]
    amount = int(move[1:])
    if turn == 'R':
        if direction == north:
            direction = east
        elif direction == east:
            direction = south
        elif direction == south:
            direction = west
        elif direction == west:
            direction = north
    elif turn == 'L':
        if direction == north:
            direction = west
        elif direction == east:
            direction = north
        elif direction == south:
            direction = east
        elif direction == west:
            direction = south
    for _ in range(amount):
        pos = pos + direction
        if pos in visited:
            return pos, direction, visited, pos
        visited.add(pos)
    return pos, direction, visited, None


def man_distance(pos):
    return int(abs(pos.real) + abs(pos.imag))


def sol1(filename):
    moves = get_input(filename)
    pos = complex(0, 0)
    direction = north
    for move in moves:
        pos, direction = apply_move(move, pos, direction)
    return man_distance(pos)


def sol2(filename):
    moves = get_input(filename)
    pos = complex(0, 0)
    visited = {pos}
    direction = north
    for move in moves:
        pos, direction, visited, found = apply_move_2(move, pos, direction, visited)
        if found is not None:
            return man_distance(found)
    return 0


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
