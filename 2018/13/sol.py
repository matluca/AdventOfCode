#!/usr/bin/env python3

def symbol_to_direction(symbol):
    if symbol == '^':
        return -1, 0
    if symbol == 'v':
        return 1, 0
    if symbol == '<':
        return 0, -1
    if symbol == '>':
        return 0, 1
    return None


class Cart:
    def __init__(self, position, symbol):
        self.position = position
        self.symbol = symbol
        self.direction = symbol_to_direction(symbol)
        self.turn_count = 0

    def move(self, grid):
        next_pos = (self.position[0] + self.direction[0], self.position[1] + self.direction[1])
        self.position = next_pos
        if grid[next_pos] in ['|', '-']:
            return
        if self.symbol == '^':
            if grid[next_pos] == '/':
                self.turn_right()
            elif grid[next_pos] == '\\':
                self.turn_left()
        elif self.symbol == '>':
            if grid[next_pos] == '/':
                self.turn_left()
            elif grid[next_pos] == '\\':
                self.turn_right()
        elif self.symbol == 'v':
            if grid[next_pos] == '/':
                self.turn_right()
            elif grid[next_pos] == '\\':
                self.turn_left()
        elif self.symbol == '<':
            if grid[next_pos] == '/':
                self.turn_left()
            elif grid[next_pos] == '\\':
                self.turn_right()
        if grid[next_pos] == '+':
            if self.turn_count == 0:
                self.turn_left()
            if self.turn_count == 2:
                self.turn_right()
            self.turn_count = (self.turn_count + 1) % 3
        self.direction = symbol_to_direction(self.symbol)

    def turn_left(self):
        symbols = ['>', '^', '<', 'v']
        self.symbol = symbols[(symbols.index(self.symbol) + 1) % 4]

    def turn_right(self):
        symbols = ['>', '^', '<', 'v']
        self.symbol = symbols[(symbols.index(self.symbol) - 1) % 4]


def get_input(filename):
    f = open(filename, 'r')
    grid = {}
    carts = []
    for i, line in enumerate(f.readlines()):
        for j, c in enumerate(line):
            if c in ['>', '<', '^', 'v']:
                carts.append(Cart((i, j), c))
            if c in ['>', '<']:
                c = '-'
            if c in ['^', 'v']:
                c = '|'
            grid[(i, j)] = c
    f.close()
    return grid, carts


def sol1(filename):
    grid, carts = get_input(filename)
    while True:
        cart_positions = [c.position for c in carts]
        cart_positions.sort()
        for pos in cart_positions:
            cart = [c for c in carts if c.position == pos][0]
            cart.move(grid)
            if cart.position in [c.position for c in carts if c != cart]:
                return cart.position[1], cart.position[0]


def sol2(filename):
    grid, carts = get_input(filename)
    while len(carts) > 1:
        cart_positions = [c.position for c in carts]
        cart_positions.sort()
        for pos in cart_positions:
            if pos not in [c.position for c in carts]:
                continue
            cart = [c for c in carts if c.position == pos][0]
            cart.move(grid)
            new_pos = cart.position
            if cart.position in [c.position for c in carts if c != cart]:
                carts.remove(cart)
                carts.remove([c for c in carts if c.position == new_pos][0])
    return carts[0].position[1], carts[0].position[0]


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
