#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    graph = {}
    for line in f:
        s, t = line.split(': ')
        for q in t.strip().split(' '):
            if s not in graph.keys():
                graph[s] = []
            graph[s].append(q)
            if q not in graph.keys():
                graph[q] = []
            graph[q].append(s)
    f.close()
    return graph


def dijkstra_all(graph, start):
    distances = {node: float('infinity') for node in graph}
    predecessors = {node: None for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        queue.sort()
        current_distance, current_node = queue.pop(0)
        for neighbor in graph[current_node]:
            distance = current_distance + 1
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                queue.append((distance, neighbor))
    return distances, predecessors


def dijkstra_remove(graph, start, end):
    distances = {node: float('infinity') for node in graph}
    predecessors = {node: None for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        queue.sort()
        current_distance, current_node = queue.pop(0)
        for neighbor in graph[current_node]:
            distance = current_distance + 1
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                queue.append((distance, neighbor))
        if current_node == end:
            break

    current_node = end
    while current_node != start:
        next_node = predecessors[current_node]
        graph[current_node].remove(next_node)
        graph[next_node].remove(current_node)
        current_node = next_node
    return graph


def sol1(filename):
    graph = get_input(filename)
    s = list(graph.keys())[0]

    distances, predecessors = dijkstra_all(graph, s)
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    furthest = [x for x in sorted_distances[-3:]]
    for p in furthest:
        graph = dijkstra_remove(graph, s, p[0])

    distances, _ = dijkstra_all(graph, s)
    reachable = len([v for v in distances.values() if v < float('infinity')])
    unreachable = len(distances) - reachable
    return reachable * unreachable


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
