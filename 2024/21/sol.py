#!/usr/bin/env python3

import time


def get_input(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return [l.strip() for l in lines]


class Button:
    def __init__(self, value, left, up, right, down):
        self.value = value
        self.up = up
        self.down = down
        self.left = left
        self.right = right


class Keypad:
    def __init__(self, buttons):
        self.buttons = buttons

    def get_button(self, value):
        for b in self.buttons:
            if b.value == value:
                return b


numeric_keypad = Keypad([
    Button('0', None, '2', 'A', None),
    Button('1', None, '4', '2', None),
    Button('2', '1', '5', '3', '0'),
    Button('3', '2', '6', 'A', None),
    Button('4', None, '7', '5', '1'),
    Button('5', '4', '8', '6', '2'),
    Button('6', '5', '9', None, '3'),
    Button('7', None, None, '8', '4'),
    Button('8', '7', None, '9', '5'),
    Button('9', '8', None, None, '6'),
    Button('A', '0', '3', None, None)
])

arrow_keypad = Keypad([
    Button('<', None, None, 'v', None),
    Button('v', '<', '^', '>', None),
    Button('>', 'v', 'A', None, None),
    Button('^', None, None, 'A', 'v'),
    Button('A', '^', None, None, '>')
])


def sol1(filename):
    lines = get_input(filename)
    return 0


def sol2(filename):
    _ = get_input(filename)
    return 0


if __name__ == '__main__':
    start_time = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    # print(f'Solution: {sol1("input.txt")}')
    end1_time = time.time()
    # print('--- Part 2 ---')
    # print(f'Test: {sol2("test.txt")}')
    # print(f'Solution: {sol2("input.txt")}')
    end2_time = time.time()
    print(
        f'Part 1: {end1_time - start_time:.3f}s, Part 2: {end2_time - end1_time:.3f}s, Tot: {end2_time - start_time:.3f}s')
