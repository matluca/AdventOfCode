#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    ports = set()
    for line in f.readlines():
        ports.add(line.strip())
    f.close()
    return ports


def has(port, value):
    return value in [int(x) for x in port.split('/')]


def other(port, value):
    if int(port.split('/')[0]) == value:
        return int(port.split('/')[1])
    return int(port.split('/')[0])


def strength(bridge):
    s = 0
    for port in bridge:
        s += int(port.split('/')[0]) + int(port.split('/')[1])
    return s


def sol(filename, part):
    ports = get_input(filename)
    starts = [port for port in ports if has(port, 0)]
    max_strength = 0
    max_length = 0
    for start in starts:
        queue = [([start], other(start, 0))]
        while queue:
            current_path, current_free_end = queue.pop(0)
            possible_ports = [p for p in ports if p not in current_path and has(p, current_free_end)]
            if len(possible_ports) == 0:
                if part == 2 and len(current_path) < max_length:
                    continue
                if part == 2 and len(current_path) > max_length:
                    max_length = len(current_path)
                    max_strength = 0
                s = strength(current_path)
                if s > max_strength:
                    max_strength = s
            for port in possible_ports:
                next_path = current_path.copy()
                next_path.append(port)
                queue.append((next_path, other(port, current_free_end)))
    return max_strength


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol("test.txt", 1)}')
    print(f'Solution: {sol("input.txt", 1)}')
    print('--- Part 2 ---')
    print(f'Test: {sol("test.txt", 2)}')
    print(f'Solution: {sol("input.txt", 2)}')
