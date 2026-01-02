#!/usr/bin/env python3

class Node:
    def __init__(self):
        self.children = []
        self.metadata = []


def get_input(filename):
    f = open(filename, 'r')
    l = [int(x) for x in f.read().split()]
    f.close()
    return l


def read_node(l, pos):
    n_children, n_metadata = l[pos], l[pos + 1]
    node = Node()
    new_pos = pos + 2
    for i in range(n_children):
        child, new_pos = read_node(l, new_pos)
        node.children.append(child)
    node.metadata = l[new_pos: new_pos + n_metadata]
    return node, new_pos + n_metadata


def sum_metadata(node):
    res = sum(node.metadata)
    for child in node.children:
        res += sum_metadata(child)
    return res


def sol1(filename):
    l = get_input(filename)
    node, _ = read_node(l, 0)
    return sum_metadata(node)


def value(node):
    if len(node.children) == 0:
        return sum(node.metadata)
    res = 0
    for n in node.metadata:
        if n <= len(node.children):
            res += value(node.children[n - 1])
    return res


def sol2(filename):
    l = get_input(filename)
    node, _ = read_node(l, 0)
    return value(node)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
