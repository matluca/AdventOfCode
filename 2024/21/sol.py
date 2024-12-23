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
    def __init__(self, position):
        self.buttons = []
        self.position = position
        self.out = None

    def get_button(self, value):
        for b in self.buttons:
            if b.value == value:
                return b

    def move_up(self):
        current_button = self.get_button(self.position)
        self.position = current_button.up

    def move_down(self):
        current_button = self.get_button(self.position)
        self.position = current_button.down

    def move_left(self):
        current_button = self.get_button(self.position)
        self.position = current_button.left

    def move_right(self):
        current_button = self.get_button(self.position)
        self.position = current_button.right


class NumericKeypad(Keypad):
    def __init__(self, position, out):
        Keypad.__init__(self, position)
        self.buttons = [
            Button('0', None, '2', 'A', None),
            Button('1', None, '4', '2', None),
            Button('2', '1', '5', '3', '0'),
            Button('3', '2', '6', None, 'A'),
            Button('4', None, '7', '5', '1'),
            Button('5', '4', '8', '6', '2'),
            Button('6', '5', '9', None, '3'),
            Button('7', None, None, '8', '4'),
            Button('8', '7', None, '9', '5'),
            Button('9', '8', None, None, '6'),
            Button('A', '0', '3', None, None)
        ]
        self.out = out

    def press(self, value):
        self.out += value


class DirectionalKeypad(Keypad):
    def __init__(self, position, next_keypad):
        Keypad.__init__(self, position)
        self.buttons = [
            Button('<', None, None, 'v', None),
            Button('v', '<', '^', '>', None),
            Button('>', 'v', 'A', None, None),
            Button('^', None, None, 'A', 'v'),
            Button('A', '^', None, None, '>')
        ]
        self.next_keypad = next_keypad

    def press(self, value):
        if value == '^':
            self.next_keypad.move_up()
        elif value == '<':
            self.next_keypad.move_left()
        elif value == 'v':
            self.next_keypad.move_down()
        elif value == '>':
            self.next_keypad.move_right()
        elif value == 'A':
            self.next_keypad.press(self.next_keypad.position)


def get_positions(dk, nk):
    positions = tuple([d.position for d in dk])
    positions += (nk.position,)
    return positions


def reset_keypads(positions, out):
    n_keypads = len(positions)
    nk = NumericKeypad(positions[n_keypads - 1], out)
    dk = []
    for i in range(n_keypads - 1):
        dk.append(DirectionalKeypad(positions[i], None))
    for i in range(1, n_keypads - 1):
        dk[i - 1].next_keypad = dk[i]
    dk[n_keypads - 2].next_keypad = nk
    return dk, nk


def find_sequence_length(dk, nk, value):
    start_positions = get_positions(dk, nk)
    distance = {(start_positions, ''): 0}
    queue = [(0, start_positions, '')]
    while queue:
        queue.sort()
        current_distance, current_positions, current_out = queue.pop(0)
        for c in ['<', 'v', '>', '^', 'A']:
            new_dk, new_nk = reset_keypads(current_positions, current_out)
            try:
                new_dk[0].press(c)
            except AttributeError:
                continue
            if len(new_nk.out) > len(value):
                continue
            if len(new_nk.out) < len(value) and not value.startswith(new_nk.out):
                continue
            if new_nk.out == value:
                return current_distance + 1
            next_positions = get_positions(new_dk, new_nk)
            if None in next_positions:
                continue
            if (next_positions, new_nk.out) not in distance.keys():
                distance[(next_positions, new_nk.out)] = current_distance + 1
                queue.append((current_distance + 1, next_positions, new_nk.out))


def sol1(filename):
    lines = get_input(filename)
    tot = 0
    for line in lines:
        dk, nk = reset_keypads(('A',) * 4, '')
        length = find_sequence_length(dk, nk, line)
        value = int(line[:-1])
        tot += length * value
    return tot


def sol2(filename):
    lines = get_input(filename)
    tot = 0
    for line in lines:
        dk, nk = reset_keypads(('A',) * 8, '')
        length = find_sequence_length(dk, nk, line)
        value = int(line[:-1])
        tot += length * value
        print(length, value)
    return tot


if __name__ == '__main__':
    start_time = time.time()
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    end1_time = time.time()
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
    end2_time = time.time()
    print(
        f'Part 1: {end1_time - start_time:.3f}s, Part 2: {end2_time - end1_time:.3f}s, Tot: {end2_time - start_time:.3f}s')
