#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    raw = f.read().strip()
    f.close()
    return raw


def sparse_hash(elements, current_position, skip_size, lengths):
    for length in lengths:
        tmp = []
        for j in range(length):
            tmp.append(elements[(current_position + j) % len(elements)])
        for j in range(length):
            elements[(current_position + length - j - 1) % len(elements)] = tmp[j]
        current_position = (current_position + length + skip_size) % len(elements)
        skip_size += 1
    return elements, current_position, skip_size


def dense(elements):
    res = []
    for i in range(16):
        x = elements[16 * i] ^ elements[16 * i + 1]
        for j in range(2, 16):
            x = x ^ elements[16 * i + j]
        res.append(hex(x))
    to_hex = ""
    for x in res:
        if len(str(x)) == 4:
            to_hex += str(x)[2:]
        else:
            to_hex += "0" + str(x)[2:]
    return to_hex


def dense_hash(inp):
    elements = list(range(256))
    current_position = 0
    skip_size = 0
    for i in range(64):
        elements, current_position, skip_size = sparse_hash(elements, current_position, skip_size, inp)
    return dense(elements)


def to_bin(hex_string):
    res = ""
    for c in hex_string:
        b = bin(int(c, 16))
        res += "0" * (6 - len(str(b))) + str(b)[2:]
    return res


def sol1(filename):
    raw = get_input(filename)
    grid = []
    for i in range(128):
        inp = raw + '-' + str(i)
        h = dense_hash([ord(x) for x in inp] + [17, 31, 73, 47, 23])
        grid.append(to_bin(h))
    return sum([sum([int(x) for x in line]) for line in grid])


def neighbours(p, grid_set):
    a, b = p
    n = []
    for q in [(a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)]:
        if q in grid_set:
            n.append(q)
    return n


def sol2(filename):
    raw = get_input(filename)
    grid = []
    for i in range(128):
        inp = raw + '-' + str(i)
        h = dense_hash([ord(x) for x in inp] + [17, 31, 73, 47, 23])
        grid.append(to_bin(h))
    grid_set = set()
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == '1':
                grid_set.add((i, j))
    regions = 0
    while len(grid_set) > 0:
        p = grid_set.pop()
        queue = [p]
        visited = set()
        while queue:
            current = queue.pop()
            visited.add(current)
            for n in neighbours(current, grid_set):
                grid_set.remove(n)
                if n not in visited:
                    queue.append(n)
        regions += 1
    return regions


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
