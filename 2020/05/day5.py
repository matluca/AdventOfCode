f = open("input.txt", "r")

max = 0
min = 1000
seats = []

for l in f:
    row = ''
    for i in range(7):
        row = row + str(int(l[i] == 'B'))
    decRow = int(row, 2)
    column = ''
    for i in range(7, 10):
        column = column + str(int(l[i] == 'R'))
    decCol = int(column, 2)
    id = decRow * 8 + decCol
    if id > max:
        max = id
    if id < min:
        min = id
    seats.append(id)
f.close()

print(max)

for n in range(min, max):
    if n not in seats:
        print(n)
