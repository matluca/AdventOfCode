#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    digits = []
    for c in data:
        digits.append(int(c))
    return digits


def sol1(filename, width, height):
    size = width * height
    digits = get_input(filename)
    min_n_zeros = size
    layer = 0
    for i in range(int(len(digits)/size)):
        n_zeros = digits[size*i: size*(i+1)].count(0)
        if n_zeros < min_n_zeros:
            min_n_zeros = n_zeros
            layer = i
    return digits[size*layer: size*(layer+1)].count(1) * digits[size*layer: size*(layer+1)].count(2)


def sol2(filename, width, height):
    size = width * height
    digits = get_input(filename)
    for j in range(height):
        for i in range(width):
            for layer in range(int(len(digits)/size)):
                c = digits[size*layer+i+j*width]
                if c == 1:
                    print('#', end=' ')
                    break
                if c == 0:
                    print(' ', end=' ')
                    break
        print()
    return 0


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 3, 2)}')
    print(f'Solution: {sol1("input.txt", 25, 6)}')
    print('--- Part 2 ---')
    print(f'Test:')
    sol2("test2.txt", 2, 2)
    print(f'Solution:')
    sol2("input.txt", 25, 6)
