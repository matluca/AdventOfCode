yourTicket = False
nearbyTickets = False
allowed = {}
tic = []
nearby = []
for line in f:
    if line == "your ticket:\n":
        yourTicket = True
    elif line == "nearby tickets:\n":
        nearbyTickets = True
    elif (not yourTicket and not nearbyTickets and len(line) != 1):
        split = line.split(": ")
        key = split[0]
        allowed[key] = [False] * 1000
        split2 = split[1].split(" or ")
        split3 = split2[0].split("-")
        for i in range(int(split3[0]), int(split3[1])+1):
            allowed[key][i] = True
        split4 = split2[1].split("-")
        for i in range(int(split4[0]), int(split4[1])+1):
            allowed[key][i] = True
    elif (yourTicket and not nearbyTickets and len(line) != 1):
        for i in line.split(","):
            tic.append(int(i))
    elif (yourTicket and nearbyTickets and len(line) != 1):
        t = []
        for i in line.split(","):
            t.append(int(i))
        nearby.append(t)          
f.close()

# part 1
globalAllow = [False] * 1000
for v in allowed.values():
    for i in range(1000):
        globalAllow[i] = globalAllow[i] or v[i]

totInvalid = 0
for t in nearby:
    for n in t:
        if (not globalAllow[n]):
            totInvalid = totInvalid + n

print(totInvalid)

# part 2
goodTics = []
for t in nearby:
    good = True
    for n in t:
        if (not globalAllow[n]):
            good = False
            break
    if good:
        goodTics.append(t)

nFields = len(tic)
canBe = {}
for i in range (len(tic)):
    canBe[i] = []
    for k in allowed.keys():
        valid = True
        for t in goodTics:
            valid = valid and allowed[k][t[i]]
        if valid:
            canBe[i].append(k)

isMacth = {}
while len(isMacth) != len(tic):
    for k, v in canBe.items():
        if len(v) == 1:
            isMacth[k] = v[0]
            for l, w in canBe.items():
                if (k != l) and (v[0] in w):
                    w.remove(v[0])

print(isMacth)
result = 1
for i in range(len(isMacth)):
    if isMacth[i].startswith("departure"):
        print(isMacth[i], tic[i])
        result = result * tic[i]

print(result)