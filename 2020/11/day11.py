def empty(grid, i, j):
    if grid[i][j] != 'L':
        return False
    free = True
    for a in range(i-1,i+2):
        for b in range(j-1,j+2):
            if (a<0 or a>=len(grid[i]) or b<0 or b>=len(grid)):
                continue
            free = free and (grid[a][b]!='#')
    return free

def occupied(grid, i, j):
    if grid[i][j] != '#':
        return False
    count = 0
    for a in range(i-1,i+2):
        for b in range(j-1,j+2):
            if (a<0 or a>=len(grid[i]) or b<0 or b>=len(grid)):
                continue
            if grid[a][b] == '#':
                count = count+1
    return (count>=5)

def numberVisibleOccupied(grid, i, j):
    count = 0
    for a in range(1, i+1):
        if grid[i-a][j] != '.':
            if grid[i-a][j] == '#':
                count = count + 1
            break
    for a in range(i+1, len(grid)):
        if grid[a][j] != '.':
            if grid[a][j] == '#':
                count = count + 1
            break
    for a in range(1, j+1):
        if grid[i][j-a] != '.':
            if grid[i][j-a] == '#':
                count = count + 1
            break
    for a in range(j+1, len(grid[i])):
        if grid[i][a] != '.':
            if grid[i][a] == '#':
                count = count + 1
            break
    for a in range(1, min(i,j)+1):
        if grid[i-a][j-a] != '.':
            if grid[i-a][j-a] == '#':
                count = count + 1
            break
    for a in range(1, min(len(grid)-i,len(grid)-j)):
        if grid[i+a][j+a] != '.':
            if grid[i+a][j+a] == '#':
                count = count + 1
            break
    for a in range(1, min(i+1,len(grid)-j)):
        if grid[i-a][j+a] != '.':
            if grid[i-a][j+a] == '#':
                count = count + 1
            break
    for a in range(1, min(j+1,len(grid)-i)):
        if grid[i+a][j-a] != '.':
            if grid[i+a][j-a] == '#':
                count = count + 1
            break
    return count

def newGrid(grid):
    diffs = 0
    newGrid = []
    for i in range(len(grid)):
        newRow = []
        for j in range(len(grid[i])):
            if empty(grid, i, j):
                newRow.append('#')
                diffs = diffs + 1
            elif occupied(grid, i, j):
                newRow.append('L')
                diffs = diffs + 1
            else:
                newRow.append(grid[i][j])
        newGrid.append(newRow)
    return newGrid, diffs

def newGrid2(grid):
    diffs = 0
    newGrid = []
    for i in range(len(grid)):
        newRow = []
        for j in range(len(grid[i])):
            if grid[i][j]=='L' and numberVisibleOccupied(grid, i, j)==0:
                newRow.append('#')
                diffs = diffs + 1
            elif grid[i][j]=='#' and numberVisibleOccupied(grid, i, j)>=5:
                newRow.append('L')
                diffs = diffs + 1
            else:
                newRow.append(grid[i][j])
        newGrid.append(newRow)
    return newGrid, diffs


f = open("input.txt", "r")
rows = []
i = 0
for line in f:
    rows.append(line.rstrip())
f.close()

grid = []
for r in rows:
    chars = []
    for c in r:
        chars.append(c)
    grid.append(chars)

diffs = 1
round = 0

while (diffs != 0):
    newG, diffs = newGrid(grid)
    grid = newG
    round = round + 1
    #print(diffs)

count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '#':
            count = count+1

print(count)

#part 2
f = open("input.txt", "r")
rows = []
i = 0
for line in f:
    rows.append(line.rstrip())
f.close()

grid = []
for r in rows:
    chars = []
    for c in r:
        chars.append(c)
    grid.append(chars)


diffs = 1
round = 0

while (diffs != 0):
    newG, diffs = newGrid2(grid)
    grid = newG
    round = round + 1
    #print(diffs)
    #print(grid)

count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '#':
            count = count+1
print(count)
#print(numberVisibleOccupied(grid, 8, 0))

