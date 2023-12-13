instr = []
f = open("input.txt", "r")
for l in f:
    ins = []
    i = 0
    while i < len(l)-1:
        if l[i] in ['n', 's']:
            ins.append(l[i:i+2])
            i += 2
        else:
            ins.append(l[i])
            i += 1
    instr.append(ins)
f.close()

colors = {}
for ins in instr:
    a = 0
    b = 0
    for step in ins:
        if step == 'e':
            a += 1
        elif step == 'se':
            a += 1
            b -= 1
        elif step == 'sw':
            b -=1
        elif step == 'w':
            a -= 1
        elif step == 'nw':
            a -= 1
            b += 1
        elif step == 'ne':
            b += 1
    existingColor = 0
    try:
        existingColor = colors[(a,b)]
    except:
        pass
    colors[(a,b)] = 1-existingColor

tot = 0
for c in colors.values():
    tot += c

print(tot)

# part 2
def blackNeigh(r):
    res = 0
    for n in [(r[0]+1,r[1]), (r[0]+1,r[1]-1), (r[0],r[1]-1), (r[0]-1,r[1]), (r[0]-1,r[1]+1), (r[0],r[1]+1)]:
        existingColor = 0
        try:
            existingColor = colors[n]
        except:
            pass
        if existingColor == 1:
            res += 1
    return res

#fill borders
minX, maxX, minY, maxY = 0, 0, 0, 0
for k in colors.keys():
    if k[0] < minX:
        minX = k[0]
    if k[1] < minY:
        minY = k[1]
    if k[0] > maxX:
        maxX = k[0]
    if k[1] > maxY:
        maxY = k[1]
for a in range(minX-1, maxX+2):
    for b in range(minY-1, maxY+2):
        try:
            something = colors[(a,b)]
        except:
            colors[(a,b)] = 0


for round in range(100):
    print(round+1)
    toFlip = {}
    minX, maxX, minY, maxY = 0, 0, 0, 0
    for k in colors.keys():
        if k[0] < minX:
            minX = k[0]
        if k[1] < minY:
            minY = k[1]
        if k[0] > maxX:
            maxX = k[0]
        if k[1] > maxY:
            maxY = k[1]
        nBlackNeigh = blackNeigh(k)
        if colors[k] == 1 and (nBlackNeigh == 0 or nBlackNeigh > 2):
            toFlip[k] = True
        if colors[k] == 0 and nBlackNeigh == 2:
            toFlip[k] = True
    for k in toFlip.keys():
        colors[k] = 1-colors[k]
    for a in range(minX-1, maxX+2):
        for b in range(minY-1, maxY+2):
            try:
                something = colors[(a,b)]
            except:
                colors[(a,b)] = 0

tot = 0
for c in colors.values():
    tot += c

print(tot)
