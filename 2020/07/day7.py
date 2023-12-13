#part 1

f = open("day7-test.txt", "r")
associations = {}
types = []
for line in f:
    line = line[:-2]
    split = line.split(" contain ", 1)
    parent = split[0]
    if parent[-1] == 's':
        parent = parent[:-5]
    else:
        parent = parent[:-4]
    types.append(parent)
    content = {}
    if split[1] != "no other bags":
        split2 = split[1].split(", ")
        for entry in split2:
            split3 = entry.split(" ", 1)
            n = split3[0]
            bag = split3[1]
            if bag[-1] == 's':
                bag = bag[:-5]
            else:
                bag = bag[:-4]
            content[bag] = int(n)
            types.append(bag)
    associations[parent] = content

f.close()

#print(associations)
types = set(types)
#print(len(types))

wanted = ['shiny gold']
found = []
total = 0
for i in range(10):
    typesNew = []
    wantedNew = []
    for t in types:
        if set(wanted) & set(associations[t].keys()):
            total = total + 1
            wantedNew.append(t)
            found.append(t)
        else:
            typesNew.append(t)
    types = typesNew
    wanted = wantedNew
    #print(i, len(found))

#print(len(found))


#part 2
f = open("input.txt", "r")
associations = {}
types = []
for line in f:
    line = line[:-2]
    split = line.split(" contain ", 1)
    parent = split[0]
    if parent[-1] == 's':
        parent = parent[:-5]
    else:
        parent = parent[:-4]
    types.append(parent)
    content = {}
    if split[1] != "no other bags":
        split2 = split[1].split(", ")
        for entry in split2:
            split3 = entry.split(" ", 1)
            n = split3[0]
            bag = split3[1]
            if bag[-1] == 's':
                bag = bag[:-5]
            else:
                bag = bag[:-4]
            content[bag] = int(n)
            #types.append(bag)
    associations[parent] = content

f.close()


values = {}
for t in types:
    values[t] = 0
for i in range(10):
    associationsNew = associations.copy()
    for t in types:
        if (len(associations[t]) == 0):
            for t2 in types:
                if t in associations[t2].keys():
                    values[t2] = values[t2] + associations[t2][t] + associations[t2][t]*values[t]
                    del (associationsNew[t2])[t]
    print(i, values['shiny gold'])

