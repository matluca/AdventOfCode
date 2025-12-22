#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    passphrases = []
    for line in f.readlines():
        passphrases.append(line.split())
    f.close()
    return passphrases


def sol1(filename):
    passphrases = get_input(filename)
    return sum([len(set(passphrase)) == len(passphrase) for passphrase in passphrases])


def sol2(filename):
    passphrases = get_input(filename)
    ordered_passphrases = [[''.join(sorted(word)) for word in passphrase] for passphrase in passphrases]
    return sum([len(set(passphrase)) == len(passphrase) for passphrase in ordered_passphrases])


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
