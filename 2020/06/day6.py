#part 1
f = open("input.txt", "r")
lines = []
groups = [""]
groupID = 0
for line in f:
    if len(line) != 1:
        groups[groupID] = groups[groupID] + line.rstrip()
    else:
        groupID = groupID + 1
        groups.append("")

f.close()

sum = 0

for group in groups:
    sum = sum + len(set(group))

print(sum)

#part 2
f = open("input.txt", "r")
lines = []
groups = [[]]
groupID = 0
for line in f:
    if len(line) != 1:
        groups[groupID].append(line.rstrip())
    else:
        groupID = groupID + 1
        groups.append([])

f.close()

sum = 0

for group in groups:
    s = set(group[0])
    for p in group:
        s = s.intersection(set(p))
    sum = sum + len(s)

print(sum)