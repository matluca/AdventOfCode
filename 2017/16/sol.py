#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    instructions = f.read().strip().split(',')
    f.close()
    return instructions


def apply(s, instruction):
    if instruction[0] == 's':
        shift = int(instruction[1:])
        return s[-shift:] + s[:-shift]
    elif instruction[0] == 'x':
        idx1, idx2 = int(instruction[1:].split('/')[0]), int(instruction[1:].split('/')[1])
        p1, p2 = s[idx1], s[idx2]
        s[idx1] = p2
        s[idx2] = p1
        return s
    else:
        p1, p2 = instruction[1:].split('/')[0], instruction[1:].split('/')[1]
        idx1, idx2 = s.index(p1), s.index(p2)
        s[idx1] = p2
        s[idx2] = p1
        return s


def dance(s, instructions):
    sl = list(s)
    for instruction in instructions:
        sl = apply(sl, instruction)
    return ''.join(sl)


def sol1(filename, size):
    instructions = get_input(filename)
    s = ''.join([chr(o) for o in range(ord('a'), ord('a') + size)])
    s = dance(s, instructions)
    return s


def sol2(filename, size):
    instructions = get_input(filename)
    s = ''.join([chr(o) for o in range(ord('a'), ord('a') + size)])
    hits = {0: s}
    i = 0
    while True:
        i += 1
        s = dance(s, instructions)
        if s in hits.values():
            break
        hits[i] = s
    return hits[1000000000 % i]


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 5)}')
    print(f'Solution: {sol1("input.txt", 16)}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt", 16)}')
