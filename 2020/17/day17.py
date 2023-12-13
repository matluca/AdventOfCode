# part 1

def next(a):
    nActive = 0
    for i in range(a[0]-1, a[0]+2):
        for j in range(a[1]-1, a[1]+2):
            for k in range(a[2]-1, a[2]+2):
                act = '.'
                try:
                    act = active[(i,j,k)]
                except:
                    pass
                if (act == '#' and (i,j,k) != a):
                    nActive = nActive + 1
    current = '.'
    try:
        current = active[a]
    except:
        pass
    if current == '#':
        if (nActive == 2 or nActive == 3):
            return '#'
        else:
            return '.'
    if current == '.':
        if nActive == 3:
            return '#'
        else:
            return '.'

def next2(a):
    nActive = 0
    for i in range(a[0]-1, a[0]+2):
        for j in range(a[1]-1, a[1]+2):
            for l in range(a[2]-1, a[2]+2):
                for k in range(a[3]-1, a[3]+2):
                    act = '.'
                    try:
                        act = active[(i,j,l,k)]
                    except:
                        pass
                    if (act == '#' and (i,j,l,k) != a):
                        nActive = nActive + 1
    current = '.'
    try:
        current = active[a]
    except:
        pass
    if current == '#':
        if (nActive == 2 or nActive == 3):
            return '#'
        else:
            return '.'
    if current == '.':
        if nActive == 3:
            return '#'
        else:
            return '.'

def printSlice(k, grid, size):
    for i in range(-size, size+1):
        toPrint = ''
        for j in range(-size, size+1):
            toPrint = toPrint + grid[(i,j,k)] + ' '
        print(toPrint)

def printSlice2(z, w, grid, size):
    for i in range(-size, size+1):
        toPrint = ''
        for j in range(-size, size+1):
            toPrint = toPrint + grid[(i,j,z,w)] + ' '
        print(toPrint)


active = {}

startDim = 1
f = open("day17-test.txt", "r")
i = 0
for line in f:
    for j in range(len(line)-1):
        active[(i-startDim,j-startDim,0)] = line[j]
    i = i+1
f.close()

dim = i

border = 10

for cycle in range(1, 7):
    newActive = {}
    #border = int((dim + 2*cycle-1)/2)
    for i in range(-border, border + 1):
        for j in range(-border, border + 1):
            for k in range(-cycle, cycle+1):
                newActive[(i,j,k)] = next((i,j,k))
    active = newActive

tot = 0
for i in range(-border, border + 1):
    for j in range(-border, border + 1):
        for k in range(-6, 6+1):
            if active[(i,j,k)] == '#':
                tot = tot + 1
print(tot)

# part 2
active = {}

startDim = 3
f = open("input.txt", "r")
i = 0
for line in f:
    for j in range(len(line)-1):
        active[(i-startDim,j-startDim,0,0)] = line[j]
    i = i+1
f.close()

dim = i

border = 10

for cycle in range(1, 7):
    newActive = {}
    for i in range(-border, border + 1):
        for j in range(-border, border + 1):
            for l in range(-border, border + 1):
                for k in range(-cycle, cycle+1):
                    newActive[(i,j,l,k)] = next2((i,j,l,k))
    active = newActive

tot = 0
for i in range(-border, border + 1):
    for j in range(-border, border + 1):
        for l in range(-border, border + 1):
            for k in range(-6, 6+1):
                if active[(i,j,l,k)] == '#':
                    tot = tot + 1
print(tot)