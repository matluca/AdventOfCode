#!/usr/bin/env python3

def neighbours(p):
    return [(p[0] + 1, p[1]), (p[0] - 1, p[1]), (p[0], p[1] + 1), (p[0], p[1] - 1)]


def distance(start, end, grid):
    queue = [(0, start)]
    visited = set(start)
    while queue:
        queue.sort()
        current = queue.pop(0)
        current_length, current_node = current
        if current_node == end:
            return current_length
        visited.add(current_node)
        for n in neighbours(current_node):
            if n in grid.keys() and grid[n] == '.' and n not in visited and (current_length + 1, n) not in queue:
                queue.append((current_length + 1, n))
    return None


class Unit:
    def __init__(self, position, label):
        self.position = position
        self.label = label
        self.enemies = []
        self.attack_power = 3
        self.hit_points = 200
        self.dead = False

    def move_towards(self, target, grid):
        current_distance = distance(self.position, target, grid)
        if current_distance == 0:
            return
        moves = []
        for n in neighbours(self.position):
            if n in grid.keys() and grid[n] == '.':
                if distance(n, target, grid) == current_distance - 1:
                    moves.append(n)
        if len(moves) == 0:
            return
        moves.sort()
        grid[self.position] = '.'
        self.position = moves[0]
        grid[self.position] = self.label

    def enemy_positions(self):
        return [e.position for e in self.enemies]

    def in_range_to_target(self, grid):
        irtt = set()
        for enemy in self.enemies:
            for n in neighbours(enemy.position):
                if n in grid and n not in self.enemy_positions():
                    irtt.add(n)
        return irtt

    def move(self, grid):
        irtt = self.in_range_to_target(grid)
        ord_targets = []
        for target in irtt:
            d = distance(self.position, target, grid)
            if d is not None:
                ord_targets.append((distance(self.position, target, grid), target))
        if len(ord_targets) == 0:
            return
        min_distance = min([ot[0] for ot in ord_targets])
        ord_targets = [ot[1] for ot in ord_targets if ot[0] == min_distance]
        ord_targets.sort()
        selected_target = ord_targets[0]
        self.move_towards(selected_target, grid)

    def attack(self, grid):
        targets = []
        for enemy in self.enemies:
            if enemy.position in neighbours(self.position):
                targets.append(enemy)
        if len(targets) == 0:
            return
        min_hit_points = min([e.hit_points for e in targets])
        targets = [e for e in targets if e.hit_points == min_hit_points]
        targets = sorted(targets, key=lambda t: t.position)
        targets[0].hit_points -= self.attack_power
        if targets[0].hit_points <= 0:
            targets[0].die(grid)
        return

    def die(self, grid):
        grid[self.position] = '.'
        for enemy in self.enemies:
            if self in enemy.enemies:
                enemy.enemies.remove(self)
        self.dead = True

    def turn(self, grid):
        if self.dead:
            return
        if len(self.enemies) == 0:
            return
        irtt = self.in_range_to_target(grid)
        if len(irtt) == 0:
            return
        self.move(grid)
        if self.position in irtt:
            self.attack(grid)
            return


def print_grid(grid):
   size_x, size_y = max([k[0] for k in grid.keys()]), max([k[1] for k in grid.keys()])
   for i in range(size_x + 1):
       for j in range(size_y + 1):
           print(grid[(i, j)], end='')
       print()


def get_input(filename):
    grid = {}
    goblins, elves = [], []
    f = open(filename, 'r')
    for i, line in enumerate(f.readlines()):
        for j, c in enumerate(line.strip()):
            grid[(i, j)] = c
            if c == 'G':
                goblins.append(Unit((i, j), 'G'))
            if c == 'E':
                elves.append(Unit((i, j), 'E'))
    f.close()
    return grid, goblins, elves


def game(grid, goblins, elves, ap, part):
    for goblin in goblins:
        goblin.enemies = elves
    for elf in elves:
        elf.enemies = goblins
        elf.attack_power = ap
    r = 0
    n_elves = len(elves)
    end = False
    while True:
        units = goblins + elves
        units = sorted(units, key=lambda u: u.position)
        units = [u for u in units if not u.dead]
        for unit in units:
            if end:
                break
            if len(unit.enemies) == 0:
                end = True
                break
            unit.turn(grid)
        if len(elves) < n_elves and part == 2:
            return -1, None
        if end:
            break
        r += 1
    return len([e for e in elves if not e.dead]) - n_elves, r * sum([u.hit_points for u in units if not u.dead])


def sol1(filename):
    grid, goblins, elves = get_input(filename)
    result = game(grid, goblins, elves, 3, 1)
    return result[1]


def sol2(filename):
    ap = 4
    while True:
        grid, goblins, elves = get_input(filename)
        result = game(grid, goblins, elves, ap, 2)
        print(ap, result)
        if result[0] == 0:
            return result[1]
        ap += 1


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
