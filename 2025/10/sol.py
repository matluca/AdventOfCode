#!/usr/bin/env python3
import sympy as sp
import pulp
import math

def get_input(filename):
    f = open(filename, 'r')
    machines = []
    for lr in f.readlines():
        diagram = lr.split(']')[0][1:]
        schematics_raw = lr.split(']')[1].split('{')[0].split()
        schematics = []
        for sr in schematics_raw:
            schematics.append([int(x) for x in sr[1:-1].split(',')])
        joltage = [int(x) for x in lr.split(']')[1].split('{')[1].split('}')[0].split(',')]
        machines.append((diagram, schematics, joltage))
    f.close()
    return machines


def apply_schematic(diagram, schematic):
    d = list(diagram)
    for s in schematic:
        if d[s] == '.':
            d[s] = '#'
        else:
            d[s] = '.'
    return ''.join(d)


def next_diagrams(diagram, schematics):
    nd = []
    for schematic in schematics:
        nd.append(apply_schematic(diagram, schematic))
    return nd


def solve_machine_1(machine):
    diagram, schematics, _ = machine
    start = diagram.replace('#', '.')
    visited = {start}
    queue = [(start, 0)]
    while queue:
        node = queue.pop(0)
        current_diagram, steps = node
        visited.add(current_diagram)
        for nd in next_diagrams(current_diagram, schematics):
            if nd == diagram:
                return steps + 1
            if nd in visited:
                continue
            queue.append((nd, steps + 1))
    return None


def sol1(filename):
    machines = get_input(filename)
    tot = 0
    for i, machine in enumerate(machines):
        tot += solve_machine_1(machine)
    return tot


def solve_machine_2(machine):
    _, schematics, joltage = machine
    m = []
    d = []
    for i in range(len(joltage)):
        line = []
        for schematic in schematics:
            if i in schematic:
                line.append(1)
            else:
                line.append(0)
        m.append(line)
        d.append(joltage[i])
    sol = sp.linsolve((sp.Matrix(m), sp.Matrix(d)))
    return sol


def is_int(x):
    return x - int(x) <= 0.00001


def minimize(s, presses):
    if "tau" not in str(presses):
        return int(presses)
    prob = pulp.LpProblem("MinimizePresses", pulp.LpMinimize)
    tau0 = pulp.LpVariable("tau0", lowBound=0, cat="Integer")
    tau1 = pulp.LpVariable("tau1", lowBound=0, cat="Integer")
    tau2 = pulp.LpVariable("tau2", lowBound=0, cat="Integer")
    var_dict = {"tau0": tau0, "tau1": tau1, "tau2": tau2}
    constraints = [eval(str(e), var_dict) >= 0 for e in s]
    constraints.append(tau0 >= 0)
    constraints.append(tau1 >= 0)
    constraints.append(tau2 >= 0)
    for c in constraints:
        prob += c
    prob += eval(str(presses), var_dict)
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    res = pulp.value(prob.objective)
    t1, t2, t3 = int(pulp.value(tau0)), int(pulp.value(tau1)), int(pulp.value(tau2))
    is_valid = True
    for p in s:
        if not is_int(eval(str(p), {"tau0": t1, "tau1": t2, "tau2": t3})):
            is_valid = False
    if not is_valid or not is_int(res):
        return int(res) + 1
    return int(res)


def sol2(filename):
    machines = get_input(filename)
    tot = 0
    for i, machine in enumerate(machines):
        s = next(iter(solve_machine_2(machine)))
        presses = sp.simplify(sum(s))
        m = minimize(s, presses)
        tot += m
    return tot


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
