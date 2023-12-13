f = open("input.txt", "r")
input = []
for l in f:
    line = l.split(",")
    for i in range(len(line)):
        line[i] = int(line[i])
    input.append(line)
f.close()

# part 1
def result(inp):
    for op in range(0, len(inp), 4):
        if inp[op] == 99:
            return inp
        if inp[op] == 1:
            inp[inp[op+3]] = inp[inp[op+1]] + inp[inp[op+2]]
        if inp[op] == 2:
            inp[inp[op+3]] = inp[inp[op+1]] * inp[inp[op+2]]
    return inp

print(result(input[5].copy())[0])

# part 2
def result2(inp, noun, verb):
    inp[1] = noun
    inp[2] = verb
    for op in range(0, len(inp), 4):
        if inp[op] == 99:
            return inp[0]
        if inp[op] == 1:
            inp[inp[op+3]] = inp[inp[op+1]] + inp[inp[op+2]]
        if inp[op] == 2:
            inp[inp[op+3]] = inp[inp[op+1]] * inp[inp[op+2]]
    return inp[0]

for noun in range(0, 100):
    for verb in range(0,100):
        res = result2(input[5].copy(), noun, verb)
        if res == 19690720:
            print(100 * noun + verb)
            break