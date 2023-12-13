def isAlpha(l):
    for e in l:
        f = e.replace(" ","")
        if not f.isalpha():
            return False
    return True



f = open("input.txt", "r")
rules = [[]] * 133
messages = []
for l in f:
    if l[0].isdigit():
        split = l.split(":")
        rules[int(split[0])] = split[1].rstrip() + " "
    else:
        if len(l)>1:
            messages.append(l.rstrip())
f.close()

for i in range(len(rules)):
    if rules[i][1] == '"':
        rules[i] = [rules[i][2]]
    else:
        split = rules[i].split("|")
        rules[i] = split

count = 0
while (not isAlpha(rules[0]) and count <10):
    print(count)
    count = count+1
    for i in range(len(rules)):
        if isAlpha(rules[i]):
            for j in range(len(rules)):
                if not isAlpha(rules[j]):
                    for elem in rules[j]:
                        if (" "+str(i)+" ")  in elem:
                            for repl in rules[i]:
                                rules[j].append(elem.replace((" "+str(i)+" "), (" "+repl+" ")))
                            rules[j].remove(elem)
    alphas = 0
    for i in range(len(rules)):
        if isAlpha(rules[i]):
            alphas = alphas + 1
            for j in range(len(rules[i])):
                rules[i][j] = rules[i][j].replace(" ", "")
    print(count, alphas)

print(isAlpha(rules[11]))
print(rules[0])

tot = 0
for m in messages:
    if m in rules[0]:
        tot = tot+1

print(tot)


