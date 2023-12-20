#!/usr/bin/env python3
import math

flip_flop, conjunction, broadcast = 0, 1, 2
low, high = 0, 1
off, on = 0, 1


def get_input(filename):
    f = open(filename, 'r')
    modules = {}
    for line in f:
        m, n = line.strip().split(' -> ')
        mod_type = broadcast
        if m[0] == '%':
            mod_type = flip_flop
        elif m[0] == '&':
            mod_type = conjunction
        name = m if mod_type == broadcast else m[1:]
        modules[name] = (mod_type, n.split(', '))
        for x in modules[name][1]:
            if x not in modules.keys():
                modules[x] = (3, [])
    f.close()
    return modules


def send_pulse(pulse, modules, mod_name, on_off, con_pulse_status, origin):
    module = modules[mod_name]
    out_pulse = pulse
    if module[0] == flip_flop:
        if pulse == low:
            on_off[mod_name] = 1 - on_off[mod_name]
            out_pulse = high if on_off[mod_name] == on else low
        else:
            out_pulse = None
    elif module[0] == conjunction:
        con_pulse_status[mod_name][origin] = pulse
        if low in con_pulse_status[mod_name].values():
            out_pulse = high
        else:
            out_pulse = low
    return out_pulse, on_off, con_pulse_status


def press_button(modules, on_off, con_pulse_status, third_level, steps, cycles):
    low_pulses, high_pulses = 1, 0
    queue = [('broadcaster', low)]
    while queue:
        mod_name, pulse = queue.pop(0)
        for tl in third_level:
            if 0 not in con_pulse_status[tl].values():
                cycles[tl] = steps
        if pulse == low:
            low_pulses += len(modules[mod_name][1])
        else:
            high_pulses += len(modules[mod_name][1])
        for neighbour in modules[mod_name][1]:
            out_pulse, on_off, con_pulse_status = send_pulse(pulse, modules, neighbour, on_off, con_pulse_status, mod_name)
            if out_pulse is not None:
                queue.append((neighbour, out_pulse))
    return low_pulses, high_pulses


def sol1(filename):
    modules = get_input(filename)
    on_off = {}
    con_pulse_status = {}
    for mod_name, mod in modules.items():
        if mod[0] == flip_flop:
            on_off[mod_name] = off
        elif mod[0] == conjunction:
            con_pulse_status[mod_name] = {}
    for mod_name, mod in modules.items():
        for n in mod[1]:
            if modules[n][0] == conjunction:
                con_pulse_status[n][mod_name] = low
    lp_tot, hp_tot = 0, 0
    for i in range(1000):
        lp, hp = press_button(modules, on_off, con_pulse_status, [], 0, {})
        lp_tot += lp
        hp_tot += hp
    return lp_tot * hp_tot


def sol2(filename):
    modules = get_input(filename)
    on_off = {}
    con_pulse_status = {}
    for mod_name, mod in modules.items():
        if mod[0] == flip_flop:
            on_off[mod_name] = off
        elif mod[0] == conjunction:
            con_pulse_status[mod_name] = {}
    for mod_name, mod in modules.items():
        for n in mod[1]:
            if modules[n][0] == conjunction:
                con_pulse_status[n][mod_name] = low
    first_level = ''
    for mod_name, mod in modules.items():
        if mod[1] == ['rx']:
            first_level = mod_name
    second_level = list(con_pulse_status[first_level].keys())
    third_level = [list(con_pulse_status[p].keys())[0] for p in second_level]
    steps = 0
    cycles = {}
    for tl in third_level:
        cycles[tl] = 0
    while 0 in cycles.values():
        steps += 1
        _, _ = press_button(modules, on_off, con_pulse_status, third_level, steps, cycles)
    return math.lcm(*list(cycles.values()))


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Test: {sol1("test2.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
