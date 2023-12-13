# part 1
def toBinary(n, length):
    nBin = [int(x) for x in bin(n)[2:]]
    for i in range(len(nBin), length):
        nBin.insert(0, 0)
    return nBin

def toDecimal(nBin):
    return int("".join(str(i) for i in nBin),2)


def insert(value, mask):
    result = toBinary(value, 36)
    maskList = list(mask)
    for i in range(36):
        if maskList[i] != 'X':
            result[i] = maskList[i]
    return toDecimal(result)

def insert2(idx, val, mask):
    input = toBinary(idx, 36)
    add = []
    maskList = list(mask)
    length = 0
    for i in range(36):
        if maskList[i] == '1':
            input[i] = 1
        elif maskList[i] == 'X':
            input[i] = 0
            add.append(pow(2,36-i-1))
            if length == 0:
                length = 36-i
    target = 1
    for j in range(len(add)):
        target = target * 2
    i = 0
    while i < target:
        binI = toBinary(i, len(add))
        loc = toDecimal(input) + sum(x[0] * x[1] for x in zip(binI, add))
        mem[loc] = val
        i = i+1

f = open("input.txt", "r")
mem = {}
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
for line in f:
    split = line.split(" = ", 1)
    if split[0] == 'mask':
        mask = split[1].rstrip()
    else:
        idx = int(split[0][4:-1])
        val = int(split[1])
        mem[idx] = insert(val, mask)
f.close()

tot = 0
for m in mem.values():
    tot = tot + m
print(tot)

# part 2
f = open("input.txt", "r")
max = 0
mem = {}
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
for line in f:
    split = line.split(" = ", 1)
    if split[0] == 'mask':
        mask = split[1].rstrip()
    else:
        idx = int(split[0][4:-1])
        val = int(split[1])
        insert2(idx, val, mask)
f.close()

tot = 0
for m in mem.values():
    tot = tot + m
print(tot)

