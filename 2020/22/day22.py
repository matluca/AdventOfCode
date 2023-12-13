f = open("input.txt", "r")
players = f.read().split("\n\n")
f.close()

decks = []
for p in players:
    rows = p.split("\n")
    decks.append(rows[1:])

for p in decks:
    for n in range(len(p)):
        p[n] = int(p[n])

def nextRound(d):
    a = d[0][0]
    b = d[1][0]
    d[0].pop(0)
    d[1].pop(0)
    if a>b:
        d[0].append(a)
        d[0].append(b)
    else:
        d[1].append(b)
        d[1].append(a)
    return d

r = 1
while len(decks[0])>0 and len(decks[1])>0:
    decks = nextRound(decks)
    r +=1

res = 0
winner = 0
if len(decks[0])==0:
    winner = 1
for i in range(len(decks[winner])):
    res += decks[winner][i]*(len(decks[winner])-i)

print(res)
