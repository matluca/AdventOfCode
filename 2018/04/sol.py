#!/usr/bin/env python3
from functools import cmp_to_key


class Record:
    def __init__(self, line):
        timestamp = line.split('[')[1].split(']')[0]
        self.timestamp = timestamp
        self.year = int(timestamp.split('-')[0])
        self.month = int(timestamp.split('-')[1])
        self.day = int(timestamp.split('-')[2].split()[0])
        self.hour = int(timestamp.split()[1].split(':')[0])
        self.minute = int(timestamp.split()[1].split(':')[1])

        self.action = line.strip().split('] ')[1]


def is_before_cmp(record1, record2):
    if record2.year < record1.year:
        return 1
    if record2.year > record1.year:
        return -1
    if record2.month < record1.month:
        return 1
    if record2.month > record1.month:
        return -1
    if record2.day < record1.day:
        return 1
    if record2.day > record1.day:
        return -1
    if record2.hour < record1.hour:
        return 1
    if record2.hour > record1.hour:
        return -1
    if record2.minute < record1.minute:
        return 1
    if record2.minute > record1.minute:
        return -1
    return 0


def get_input(filename):
    records = []
    f = open(filename, 'r')
    for line in f.readlines():
        records.append(Record(line))
    f.close()
    return records


def get_asleep_intervals(records):
    records = sorted(records, key=cmp_to_key(is_before_cmp))
    guard = None
    start = -1
    asleep = {}
    for record in records:
        if 'begins shift' in record.action:
            guard = record.action.split('#')[1].split()[0]
            start = -1
        elif 'falls asleep' in record.action:
            start = record.minute
        elif 'wakes up' in record.action:
            if guard not in asleep.keys():
                asleep[guard] = []
            asleep[guard].append((start, record.minute))
    return asleep


def sol1(filename):
    records = get_input(filename)
    asleep = get_asleep_intervals(records)
    max_asleep_minutes = 0
    sleeper = None
    for k, v in asleep.items():
        tot_asleep = sum([p[1] - p[0] for p in v])
        if tot_asleep > max_asleep_minutes:
            max_asleep_minutes = tot_asleep
            sleeper = k
    times_asleep = {}
    for interval in asleep[sleeper]:
        for i in range(interval[0], interval[1]):
            if i not in times_asleep.keys():
                times_asleep[i] = 0
            times_asleep[i] += 1
    return int(sleeper) * max(times_asleep, key=times_asleep.get)


def sol2(filename):
    records = get_input(filename)
    asleep = get_asleep_intervals(records)
    stats = {}
    for minute in range(0, 59):
        for guard in asleep.keys():
            counter = 0
            for interval in asleep[guard]:
                counter += interval[0] <= minute < interval[1]
            stats[(minute, guard)] = counter
    m = max(stats, key=stats.get)
    return m[0] * int(m[1])


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
