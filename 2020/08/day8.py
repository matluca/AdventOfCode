def endResultThis(i, acc):
    while True:
        if hit[i]:
            #print("hit already", i)
            break
        hit[i] = True
        if instr[i][0] == 'acc':
            acc = acc + instr[i][1]
            i = i + 1
        if instr[i][0] == 'jmp':
            i = i + instr[i][1]
        if instr[i][0] == 'nop':
            i = i + 1
    return i, acc

def endResultChange(i, acc):
    localHit = hit.copy()
    localHit[i] = True
    if instr[i][0] == 'nop':
        i = i + instr[i][1]
    if instr[i][0] == 'jmp':
        i = i + 1
    while True:
        if (i>=len(instr) or localHit[i]):
            #print("hit already", i)
            break
        localHit[i] = True
        if instr[i][0] == 'acc':
            acc = acc + instr[i][1]
            i = i + 1
            continue
        if instr[i][0] == 'jmp':
            i = i + instr[i][1]
            continue
        if instr[i][0] == 'nop':
            i = i + 1
    return i, acc

#part 1
f = open("input.txt", "r")

instr = []
for l in f:
    split = l.split(" ")
    instr.append( (split[0], int(split[1])) )

f.close()

hit = []
for i in range(len(instr)):
    hit.append(False)

acc = 0
i = 0
print(endResultThis(0,0))


# part 2

f = open("input.txt", "r")

instr = []
for l in f:
    split = l.split(" ")
    instr.append( (split[0], int(split[1])) )

f.close()

hit = []
for i in range(len(instr)):
    hit.append(False)

acc = 0
i = 0
last = len(instr)

while True:
    if hit[i]:
        #print("hit already", i)
        break
    hit[i] = True
    if instr[i][0] == 'acc':
        acc = acc + instr[i][1]
        i = i + 1
        continue
    else:
        res, acc2 = endResultChange(i, acc)
        if res == last:
            acc = acc2
            break
        else:
            if instr[i][0] == 'jmp':
                i = i + instr[i][1]
                continue
            if instr[i][0] == 'nop':
                i = i + 1

    #print(i, acc)

print(acc)