import math

orientation = 0 # has to be 1 or zero

def borders(tile):
    res = [tile[0], tile[0][::-1], tile[9], tile[9][::-1]]
    right = ''
    for i in range(10):
        right = right + tile[i][9]
    left = ''
    for i in range(10):
        left = left + tile[9-i][0]
    res.append(right)
    res.append(right[::-1])
    res.append(left)
    res.append(left[::-1])
    return res

f = open("input.txt", "r")
rawTiles = f.read().split("\n\n")
f.close()

tiles = {}
for t in rawTiles:
    title, tile = t.split(":\n")
    number = int(title.split(" ")[1])
    raws = tile.split("\n")
    tiles[number] = raws

neighN = {}
neigh = {}
for k in tiles.keys():
    neigh[k] = []
    tot = 0
    for h in tiles.keys():
        if (set(borders(tiles[k])) & set(borders(tiles[h]))) and (k != h):
            neigh[k].append(h)
            tot += 1
    neighN[k] = tot

res = 1
corners = []
for k in neighN.keys():
    if neighN[k] == 2:
        corners.append(k)
        res = res * k
print(res)

# build keys grid
size = math.isqrt(len(neighN))
numberGrid = [[0 for x in range(size)] for x in range(size)]

def printGrid(g, s = size):
    for i in range(s):
        line = ""
        for j in range(s):
            line = line + str(g[i][j]) + " "
        print(line)

numberGrid[0][0] = corners[0]
numberGrid[0][1] = neigh[corners[0]][orientation]
numberGrid[1][0] = neigh[corners[0]][1-orientation]
neigh[corners[0]] = []
neigh[numberGrid[0][1]].remove(corners[0])
neigh[numberGrid[1][0]].remove(corners[0])
next = list(set(neigh[numberGrid[0][1]]) & set(neigh[numberGrid[1][0]]))[0]
numberGrid[1][1] = next
neigh[next].remove(numberGrid[0][1])
neigh[next].remove(numberGrid[1][0])
neigh[numberGrid[0][1]].remove(next)
neigh[numberGrid[1][0]].remove(next)

for i in range(2, size):
    next = neigh[numberGrid[i-1][0]][0]
    numberGrid[i][0] = next
    neigh[numberGrid[i-1][0]].remove(next)
    neigh[next].remove(numberGrid[i-1][0])
    next = neigh[numberGrid[0][i-1]][0]
    numberGrid[0][i] = next
    neigh[numberGrid[0][i-1]].remove(next)
    neigh[next].remove(numberGrid[0][i-1])
    for j in range(1, i):
        next = list(set(neigh[numberGrid[i-1][j]]) & set(neigh[numberGrid[i][j-1]]))[0]
        numberGrid[i][j] = next
        neigh[numberGrid[i-1][j]].remove(next)
        neigh[numberGrid[i][j-1]].remove(next)
        neigh[next].remove(numberGrid[i-1][j])
        neigh[next].remove(numberGrid[i][j-1])
        next = list(set(neigh[numberGrid[j-1][i]]) & set(neigh[numberGrid[j][i-1]]))[0]
        numberGrid[j][i] = next
        neigh[numberGrid[j-1][i]].remove(next)
        neigh[numberGrid[j][i-1]].remove(next)
        neigh[next].remove(numberGrid[j-1][i])
        neigh[next].remove(numberGrid[j][i-1])
    next = list(set(neigh[numberGrid[i-1][i]]) & set(neigh[numberGrid[i][i-1]]))[0]
    numberGrid[i][i] = next
    neigh[next].remove(numberGrid[i-1][i])
    neigh[next].remove(numberGrid[i][i-1])
    neigh[numberGrid[i-1][i]].remove(next)
    neigh[numberGrid[i][i-1]].remove(next)

print()
printGrid(numberGrid)

# build transformation grid
transformations = ['0', '90', '180', '270', 'f-0', 'f-90', 'f-180', 'f-270']
def listToString(list):
    res = ''
    for c in list:
        res += c
    return res

def applyTransf(tile, transf, s=10):
    if transf == '0':
        return tile
    if transf == '90':
        newTile = [['.' for x in range(s)] for x in range(s)]
        for i in range(s):
            for j in range(s):
                newTile[i][j] = tile[s-1-j][i]
        return newTile
    if transf == '180':
        return applyTransf(applyTransf(tile, '90', s), '90', s)
    if transf == '270':
        return applyTransf(applyTransf(tile, '180', s), '90', s)
    if transf == 'f-0':
        newTile = [['.' for x in range(s)] for x in range(s)]
        for i in range(s):
            for j in range(s):
                newTile[i][j] = tile[s-1-i][j]
        return newTile
    if transf == 'f-90':
        return applyTransf(applyTransf(tile, 'f-0', s), '90', s)
    if transf == 'f-180':
        return applyTransf(applyTransf(tile, 'f-0', s), '180', s)
    if transf == 'f-270':
        return applyTransf(applyTransf(tile, 'f-0', s), '270', s)

def leftBorder(tile, transf):
    newTile = applyTransf(tile, transf)
    return listToString([newTile[x][0] for x in range(9)])

def rightBorder(tile, transf):
    newTile = applyTransf(tile, transf)
    return listToString([newTile[x][9] for x in range(9)])

def topBorder(tile, transf):
    newTile = applyTransf(tile, transf)
    return newTile[0]

def bottomBorder(tile, transf):
    newTile = applyTransf(tile, transf)
    return newTile[9]

transfGrid = [['.' for x in range(size)] for x in range(size)]

for t1 in transformations:
    for t2 in transformations:
        for t3 in transformations:
            if rightBorder(tiles[numberGrid[0][0]], t1) == leftBorder(tiles[numberGrid[0][1]], t2):
                if bottomBorder(tiles[numberGrid[0][0]], t1) == topBorder(tiles[numberGrid[1][0]], t3):
                    transfGrid[0][0] = t1
                    transfGrid[0][1] = t2

for i in range(2, size):
    for t in transformations:
        if rightBorder(tiles[numberGrid[0][i-1]], transfGrid[0][i-1]) == leftBorder(tiles[numberGrid[0][i]], t):
            transfGrid[0][i] = t

for i in range(1, size):
    for t in transformations:
        if bottomBorder(tiles[numberGrid[i-1][0]], transfGrid[i-1][0]) == topBorder(tiles[numberGrid[i][0]], t):
            transfGrid[i][0] = t
    for j in range (1, size):
        for t in transformations:
            if rightBorder(tiles[numberGrid[i][j-1]], transfGrid[i][j-1]) == leftBorder(tiles[numberGrid[i][j]], t):
                transfGrid[i][j] = t

print()
printGrid(transfGrid)

finalGrid = [['.' for x in range(size*10)] for x in range(size*10)]

for i in range(size*10):
    for j in range(size*10):
        tileN = numberGrid[int(i/10)][int(j/10)]
        tile = applyTransf(tiles[tileN], transfGrid[int(i/10)][int(j/10)])
        finalGrid[i][j] = tile[i%10][j%10]

finalNormalizedGrid = [['.' for x in range(size*8)] for x in range(size*8)]

for i in range(size*8):
    for j in range(size*8):
        tileN = numberGrid[int(i/8)][int(j/8)]
        tile = applyTransf(tiles[tileN], transfGrid[int(i/8)][int(j/8)])
        finalNormalizedGrid[i][j] = tile[i%8+1][j%8+1]

print()

monster = ['                  # ','#    ##    ##    ###',' #  #  #  #  #  #   ']

width = 20
height = 3

topLeft = []
totMonsters = 0
finalTransf = ''
for t in transformations:
    tot = 0
    for i in range(size*8-3):
        for j in range(size*8-20):
            check = True
            for a in range(3):
                for b in range(20):
                    if monster[a][b] == '#' and applyTransf(finalNormalizedGrid, t, size*8)[i+a][j+b] != '#':
                        check = False
            if check:
                tot = tot+1
                topLeft.append((i,j))
    if tot > 0:
        finalTransf = t
        totMonsters = tot
        break

gridWithMonsters = applyTransf(finalNormalizedGrid, t, size*8)
for point in topLeft:
    for a in range(3):
        for b in range(20):
            if monster[a][b] == '#':
                gridWithMonsters[point[0]+a][point[1]+b] = 'O'

printGrid(gridWithMonsters, size*8)

tot = 0
for i in range(size*8):
    for j in range(size*8):
        if gridWithMonsters[i][j] == '#':
            tot += 1

print()
print(tot)
