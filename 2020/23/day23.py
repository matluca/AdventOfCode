import array

# part 1
f = open("input.txt", "r")
cups = []
for l in f:
    for c in l:
        cups.append(int(c))
f.close()


round = 0
size = len(cups)
while round < 100:
    round += 1
    subCups = []
    for i in range(4, size):
        subCups.append(cups[i])
    foundDestination = False
    d = cups[0]
    id = 0
    while (not foundDestination) and d>0:
        d = d-1
        for i in range(size-4):
            if subCups[i] == d:
                foundDestination = True
                id = i+4
    if not foundDestination:
        for i in range(size-4):
            if subCups[i]> d:
                d = subCups[i]
                id = i+4
    newCups = []
    
    for i in range(4, size):
        newCups.append(cups[i])
        if i == id:
            newCups.append(cups[1])
            newCups.append(cups[2])
            newCups.append(cups[3])
    newCups.append(cups[0])
    cups = newCups

id1 = 0
for i in range(size):
    if cups[i] == 1:
        id1 = i
        break


resPart1 = ''
for i in range(size-1):
    resPart1 = resPart1 + str(cups[(id1+i+1)%size])
print(resPart1)


# part 2
f = open("input.txt", "r")
input = ''
for l in f:
    for c in l:
        input = l
f.close()

cups = 1000000
a = array.array('I', range(1, cups+2))
b = array.array('I', map(int, input))
a[0] = a[-1] = b[0]
for i in range(len(b) - 1):
    a[b[i]] = b[i + 1]
a[b[len(b) - 1]] = b[0] if cups == len(b) else len(b) + 1

cur = 0
for _ in range(10000000):
    cur = a[cur]
    nxt = cur - 1 if cur != 1 else cups

    while True:
        i = cur
        found = False
        for _ in range(3):
            if (i := a[i]) == nxt:
                found = True
                nxt = nxt - 1 if nxt != 1 else cups
                break
        if not found:
            break

    a[i], a[nxt], a[cur] = a[nxt], a[cur], a[i]

print(a[1]*a[a[1]])

