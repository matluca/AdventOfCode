#!/usr/bin/env python3

def get_input(filename):
    connections = {}
    f = open(filename, 'r')
    for line in f.readlines():
        node = line.split(' <-> ')[0]
        leaves = line.split(' <-> ')[1].strip().split(', ')
        connections[node] = leaves
        for leaf in leaves:
            if leaf not in connections.keys():
                connections[leaf] = [node]
            elif node not in connections[leaf]:
                connections[leaf].append(node)
    f.close()
    return connections


def find_group(node, groups):
    for group in groups:
        if node in group:
            return group
    return None


def build_groups(connections):
    groups = []
    for node, leaves in connections.items():
        gn = find_group(node, groups)
        if gn is None:
            for leaf in leaves:
                gl = find_group(leaf, groups)
                if gl is not None:
                    groups.remove(gl)
                    groups.append(gl | {node})
            if find_group(node, groups) is None:
                g = {node} | set(connections[node])
                groups.append(g)
        for leaf in leaves:
            gnn = find_group(node, groups)
            gl = find_group(leaf, groups)
            if gl is not None and gl != gnn:
                groups.remove(gnn)
                groups.remove(gl)
                groups.append(gnn | gl)
    new_groups = []
    for group in groups:
        match = False
        for new_group in new_groups:
            if len(group & new_group) > 0:
                new_groups.remove(new_group)
                new_groups.append(group & new_group)
                match = True
                break
        if not match:
            new_groups.append(group)
    return new_groups


def sol1(filename):
    connections = get_input(filename)
    groups = build_groups(connections)
    return len(find_group('0', groups))


def sol2(filename):
    connections = get_input(filename)
    groups = build_groups(connections)
    return len(groups)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
