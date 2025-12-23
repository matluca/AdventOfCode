#!/usr/bin/env python3

def get_input(filename):
    graph = {}
    weights = {}
    f = open(filename, 'r')
    for line in f.readlines():
        if "->" in line:
            base, leaves = line.split(" -> ")
            graph[base.split()[0]] = leaves.strip().split(", ")
            weights[base.split()[0]] = int(base.split()[1][1:-1])
        else:
            weights[line.split()[0]] = int(line.strip().split()[1][1:-1])
    f.close()
    return graph, weights


def sol1(filename):
    graph, weights = get_input(filename)
    children = set()
    for leaves in graph.values():
        children |= set(leaves)
    return [k for k in graph.keys() if k not in children][0]


def total_weight(graph, weights, node):
    if node not in graph.keys():
        return weights[node]
    return sum([total_weight(graph, weights, leaf) for leaf in graph[node]]) + weights[node]


def is_balanced(graph, weights, node):
    different_weights = set([total_weight(graph, weights, leaf) for leaf in graph[node]])
    return len(different_weights) == 1


def sol2(filename):
    graph, weights = get_input(filename)
    for node in graph.keys():
        if not is_balanced(graph, weights, node):
            children_balanced = True
            for leaf in graph[node]:
                if not is_balanced(graph, weights, leaf):
                    children_balanced = False
            if not children_balanced:
                continue
            different_weights = set([total_weight(graph, weights, leaf) for leaf in graph[node]])
            diff = max(different_weights) - min(different_weights)
            culprit = [leaf for leaf in graph[node] if total_weight(graph, weights, leaf) == max(different_weights)][0]
            return weights[culprit] - diff
    return None


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
