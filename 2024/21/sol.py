#!/usr/bin/env python3
import functools
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
    def __init__(self, position, next_keypad, out):
        self.buttons = []
        self.position = position
        self.next_keypad = next_keypad
        self.out = out

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

    def reset(self, position, out):
        self.position = position
        self.out = out

    def press(self, value):
        self.out += value
        if self.next_keypad is None:
            return
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


class NumericKeypad(Keypad):
    def __init__(self, position, out):
        Keypad.__init__(self, position, None, out)
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


class DirectionalKeypad(Keypad):
    def __init__(self, position, next_keypad, out):
        Keypad.__init__(self, position, next_keypad, out)
        self.buttons = [
            Button('<', None, None, 'v', None),
            Button('v', '<', '^', '>', None),
            Button('>', 'v', 'A', None, None),
            Button('^', None, None, 'A', 'v'),
            Button('A', '^', None, None, '>')
        ]


def get_positions(keypads):
    positions = tuple([k.position for k in keypads])
    return positions


def get_outs(keypads):
    return keypads[0].out, keypads[1].out


def reset_keypads(keypads, positions, outs):
    for i, keypad in enumerate(keypads):
        keypad.position = positions[i]
        if i < 2:
            keypad.out = outs[i]
    return keypads


def find_best_first_sequence(value, level):
    first_keypad = DirectionalKeypad('A', None, '')
    if value[0].isdigit():
        first_keypad = NumericKeypad('A', '')
    keypads = [first_keypad]
    for l in range(1, level):
        keypads.append(DirectionalKeypad('A', keypads[l - 1], ''))
    start_positions = get_positions(keypads)
    outs = get_outs(keypads)
    queue = [(0, start_positions, outs)]
    distance = {(start_positions, ''): 0}
    while queue:
        queue.sort()
        current_distance, current_positions, current_outs = queue.pop(0)
        for c in ['<', 'v', '>', '^', 'A']:
            keypads = reset_keypads(keypads, current_positions, current_outs)
            try:
                keypads[level - 1].press(c)
            except AttributeError:
                continue
            next_positions = get_positions(keypads)
            next_outs = get_outs(keypads)
            if None in next_positions:
                continue
            if len(keypads[0].out) > len(value):
                continue
            if 0 < len(keypads[0].out) < len(value) and not value.startswith(keypads[0].out):
                continue
            if keypads[0].out == value:
                return next_outs[1], current_distance + 1
            if (next_positions, keypads[0].out) not in distance.keys():
                distance[(next_positions, keypads[0].out)] = current_distance + 1
                queue.append((current_distance + 1, next_positions, next_outs))


def find_substrings(string):
    substrings = string.split('A')
    return [s + 'A' for s in substrings[:-1]]


@functools.cache
def decompose(sub):
    if sub == {'A'}:
        return {'A': 0}
    first_seq, _ = find_best_first_sequence(sub, 5)
    subs_list = [s + 'A' for s in first_seq.split('A')[:-1]]
    subs = {}
    for sub in subs_list:
        if sub not in subs.keys():
            subs[sub] = 0
        subs[sub] += 1
    return subs


def find_sequence_length(string, levels):
    seq = {string: 1}
    for l in range(levels):
        new_seq = {}
        for k, v in seq.items():
            for kk, vv in decompose(k).items():
                if kk not in new_seq.keys():
                    new_seq[kk] = 0
                new_seq[kk] += vv * v
        seq = new_seq
    length = 0
    for k, v in seq.items():
        length += len(k) * v
    return length


def sol1(filename):
    lines = get_input(filename)
    tot = 0
    for line in lines:
        _, length = find_best_first_sequence(line, 4)
        value = int(line[:-1])
        tot += length * value
    return tot


def sol2(filename):
    lines = get_input(filename)
    tot = 0
    for line in lines:
        value = int(line[:-1])
        tot += value * find_sequence_length(line, 26)
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
