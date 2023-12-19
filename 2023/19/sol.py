#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r').read()
    workflows = {}
    parts = []
    w, p = f.split('\n\n')
    for x in w.split('\n'):
        key = x.split('{')[0]
        workflows[key] = x[len(key) + 1:-1].split(',')
    for q in p.split('\n'):
        d = {}
        pp = q[1:-1].split(',')
        for qq in pp:
            d[qq.split('=')[0]] = int(qq.split('=')[1])
        parts.append(d)
    return workflows, parts


def apply_workflow(part, workflows, workflow):
    conditions = workflows[workflow]
    for condition in conditions[:-1]:
        l, s, n, r = condition[0], condition[1], int(condition.split(':')[0][2:]), condition.split(':')[1]
        if s == '<' and part[l] < n:
            return r
        if s == '>' and part[l] > n:
            return r
    return conditions[-1]


def sol1(filename):
    workflows, parts = get_input(filename)
    res = 0
    for part in parts:
        workflow = 'in'
        while workflow not in ['A', 'R']:
            workflow = apply_workflow(part, workflows, workflow)
        if workflow == 'A':
            res += part['x'] + part['m'] + part['a'] + part['s']
    return res


def sol2(filename):
    workflows, _ = get_input(filename)
    intervals = {'in': [{'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}]}
    queue = ['in']
    while queue:
        workflow = queue.pop()
        conditions = workflows[workflow]
        ints = intervals[workflow]
        for condition in conditions:
            if ':' in condition:
                l, s, n, r = condition[0], condition[1], int(condition.split(':')[0][2:]), condition.split(':')[1]
                for i in ints:
                    if s == '>' and n < i[l][1]:
                        new_int = i.copy()
                        new_int[l] = (max(n + 1, i[l][0]), i[l][1])
                        i[l] = (min(n + 1, i[l][0]), n)
                        if r not in intervals:
                            intervals[r] = []
                        intervals[r].append(new_int)
                    if s == '<' and n > i[l][0]:
                        new_int = i.copy()
                        new_int[l] = (i[l][0], min(n - 1, i[l][1]))
                        i[l] = (n, max(n - 1, i[l][1]))
                        if r not in intervals:
                            intervals[r] = []
                        intervals[r].append(new_int)
                if r not in ['A', 'R']:
                    queue.append(r)
            else:
                if condition not in intervals:
                    intervals[condition] = []
                intervals[condition] += ints
                if condition not in ['A', 'R']:
                    queue.append(condition)
    res = 0
    for i in intervals['A']:
        partial = 1
        for k in i.values():
            partial *= k[1] - k[0] + 1
        res += partial
    return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
