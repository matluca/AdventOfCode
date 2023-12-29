#!/usr/bin/env python3
import time


def get_input(filename):
    f = open(filename, 'r')
    instructions = []
    for line in f:
        instructions.append(line.strip())
    f.close()
    return instructions


digits = {
    complex(-1, -1): '1',
    complex(-1, 0): '2',
    complex(-1, 1): '3',
    complex(0, -1): '4',
    complex(0, 0): '5',
    complex(0, 1): '6',
    complex(1, -1): '7',
    complex(1, 0): '8',
    complex(1, 1): '9'
}

moves = {'U': complex(-1, 0), 'D': complex(1, 0), 'R': complex(0, 1), 'L': complex(0, -1)}


def sol1(filename):
    instructions = get_input(filename)
    pos = complex(0, 0)
    code = ''
    for instruction in instructions:
        for move in instruction:
            next_pos = pos + moves[move]
            if next_pos in digits.keys():
                pos = next_pos
        code += digits[pos]
    return code


digits_2 = {
    complex(-2, -0): '1',
    complex(-1, -1): '2',
    complex(-1, 0): '3',
    complex(-1, 1): '4',
    complex(0, -2): '5',
    complex(0, -1): '6',
    complex(0, 0): '7',
    complex(0, 1): '8',
    complex(0, 2): '9',
    complex(1, -1): 'A',
    complex(1, 0): 'B',
    complex(1, 1): 'C',
    complex(2, 0): 'D'
}


def sol2(filename):
    instructions = get_input(filename)
    pos = complex(0, -2)
    code = ''
    for instruction in instructions:
        for move in instruction:
            next_pos = pos + moves[move]
            if next_pos in digits_2.keys():
                pos = next_pos
        code += digits_2[pos]
    return code


if __name__ == '__main__':
    start = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    part1 = time.time()
    print(f'Elapsed time: {part1 - start}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
    part2 = time.time()
    print(f'Elapsed time: {part2 - part1}')
