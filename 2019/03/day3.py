f = open("input.txt", "r")
sets = f.read().split("\n\n")
f.close()

inLines = []
for s in sets:
    ls = s.split("\n", 2)
    inLines.append(ls)


lines = inLines[3]

# part 1
points = [[],[]]
for i in range(len(lines)):
    current = (0,0)
    for entry in lines[i].split(","):
        if entry[0] == "R":
            for j in range(int(entry[1:])):
                current = (current[0], current[1]+1)
                points[i].append(current)
        if entry[0] == 'L':
            for j in range(int(entry[1:])):
                current = (current[0], current[1]-1)
                points[i].append(current)
        if entry[0] == 'U':
            for j in range(int(entry[1:])):
                current = (current[0]+1, current[1])
                points[i].append(current)
        if entry[0] == 'D':
            for j in range(int(entry[1:])):
                current = (current[0]-1, current[1])
                points[i].append(current)

intersections = list(set(points[0]).intersection(set(points[1])))

min = 5000
for p in intersections:
    dist = abs(p[0]) + abs(p[1])
    if dist < min:
        min = dist
print(min)

# part 2
minSteps = 100000
for inter in intersections:
    steps = 0
    for p in points:
        for x in p:
            steps += 1
            if x == inter:
                break
    if steps < minSteps:
        minSteps = steps

print(minSteps)
