#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r').read()
    return f.split('\n')


def find_beams(grid, start, start_dir):
    size_x, size_y = len(grid), len(grid[0])
    visited = []
    exits = set()
    queue = [(start, start_dir)]
    while True:
        if not queue:
            break
        current = queue.pop(0)
        pos = current[0]
        direction = current[1]
        if (pos, direction) in visited:
            continue
        if 0 <= pos[0] < size_x and 0 <= pos[1] < size_y:
            visited.append((pos, direction))
        next_pos = [pos[0] + direction[0], pos[1] + direction[1]]
        if next_pos[0] < 0 or next_pos[0] >= size_x:
            exits.add(tuple(next_pos))
            continue
        if next_pos[1] < 0 or next_pos[1] >= size_y:
            exits.add(tuple(next_pos))
            continue
        if grid[next_pos[0]][next_pos[1]] == '.':
            queue.append((next_pos, direction))
        elif grid[next_pos[0]][next_pos[1]] == '-' and direction in [[0, 1], [0, -1]]:
            queue.append((next_pos, direction))
        elif grid[next_pos[0]][next_pos[1]] == '|' and direction in [[1, 0], [-1, 0]]:
            queue.append((next_pos, direction))
        elif grid[next_pos[0]][next_pos[1]] == '|' and direction in [[0, 1], [0, -1]]:
            queue.append((next_pos, [1, 0]))
            queue.append((next_pos, [-1, 0]))
        elif grid[next_pos[0]][next_pos[1]] == '-' and direction in [[1, 0], [-1, 0]]:
            queue.append((next_pos, [0, 1]))
            queue.append((next_pos, [0, -1]))
        elif grid[next_pos[0]][next_pos[1]] == '\\':
            if direction == [0, 1]:
                queue.append((next_pos, [1, 0]))
            elif direction == [0, -1]:
                queue.append((next_pos, [-1, 0]))
            elif direction == [1, 0]:
                queue.append((next_pos, [0, 1]))
            elif direction == [-1, 0]:
                queue.append((next_pos, [0, -1]))
        elif grid[next_pos[0]][next_pos[1]] == '/':
            if direction == [0, 1]:
                queue.append((next_pos, [-1, 0]))
            elif direction == [0, -1]:
                queue.append((next_pos, [1, 0]))
            elif direction == [1, 0]:
                queue.append((next_pos, [0, -1]))
            elif direction == [-1, 0]:
                queue.append((next_pos, [0, 1]))
    return len(set([tuple(v[0]) for v in visited])), exits


def sol1(filename):
    grid = get_input(filename)
    visited, _ = find_beams(grid, [0, -1], [0, 1])
    return visited


def sol2(filename):
    grid = get_input(filename)
    res = 0
    tried = set()
    for i in range(len(grid)):
        if (i, -1) not in tried:
            c, exits = find_beams(grid, [i, -1], [0, 1])
            tried.add((i, -1))
            tried = tried | exits
            if c > res:
                res = c
        if (i, len(grid[0])) not in tried:
            c, exits = find_beams(grid, [i, len(grid[0])], [0, -1])
            tried.add((i, len(grid[0])))
            tried = tried | exits
            if c > res:
                res = c
    for j in range(len(grid[0])):
        if (-1, j) not in tried:
            c, exits = find_beams(grid, [-1, j], [1, 0])
            tried.add((-1, j))
            tried = tried | exits
            if c > res:
                res = c
        if (len(grid), j) not in tried:
            c, exits = find_beams(grid, [len(grid), j], [-1, 0])
            tried.add((len(grid), j))
            tried = tried | exits
            if c > res:
                res = c
    return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
