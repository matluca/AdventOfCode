f = open("input.txt", "r")
lines = []
for line in f:
    lines.append(line)
length = len(lines[0])-1

trees1 = 0
for i in range (0, len(lines)):
    j = (i) % length
    if (lines[i][j] == '#'):
        trees1 = trees1 + 1

trees2 = 0
for i in range (0, len(lines)):
    j = (3*i) % length
    if (lines[i][j] == '#'):
        trees2 = trees2 + 1

trees3 = 0
for i in range (0, len(lines)):
    j = (5*i) % length
    if (lines[i][j] == '#'):
        trees3 = trees3 + 1

trees4 = 0
for i in range (0, len(lines)):
    j = (7*i) % length
    if (lines[i][j] == '#'):
        trees4 = trees4 + 1

trees5 = 0
for i in range (0, int(len(lines)/2)+1):
    j = i % length
    if (lines[2*i][j] == '#'):
        trees5 = trees5 + 1

print(trees1, trees2, trees3, trees4, trees5)
print (trees1*trees2*trees3*trees4*trees5)