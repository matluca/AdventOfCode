#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r').read()
    return f.strip()


def next_seq(seq):
    occ = [[seq[0], 1]]
    for c in seq[1:]:
        if c == occ[-1][0]:
            occ[-1][1] += 1
        else:
            occ.append([c, 1])
    s = ''
    for o in occ:
        s += str(o[1]) + o[0]
    return s


def sol(filename, steps):
    seq = get_input(filename)
    for _ in range(steps):
        seq = next_seq(seq)
    return len(seq)


def sol2(filename):
    _ = get_input(filename)
    return 0


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol("test.txt", 4)}')
    print(f'Solution: {sol("input.txt", 40)}')
    print('--- Part 2 ---')
    print(f'Solution: {sol("input.txt", 50)}')
