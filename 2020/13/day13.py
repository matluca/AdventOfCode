f = open("input.txt", "r")
i = 0
timestamp = 0
buses = []
offsets = []
for l in f:
    if i == 0:
        timestamp = int(l)
        i = i + 1
    else:
        split = l.split(",")
        for b in range(len(split)):
            if split[b] != 'x':
                buses.append(int(split[b]))
                offsets.append(b)
f.close()
print(buses)
print(offsets)

min = timestamp
bus = 0
for b in buses:
    diff = b-timestamp%b
    if diff < min:
        min = diff
        bus = b

print(bus, "*", min, "=", bus*min)

#part 2
for i in range(1, len(buses)):
    s = str(buses[0])
    for j in range(i-1):
        s = s + " 0"
    s = s + " -" + str(buses[i])
    for j in range(len(buses)-i-1):
        s = s + " 0"
    s = s + " " + str(offsets[i])
    print(s)

# http://www.numbertheory.org/php/axb.html


