import copy

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

# returns the winner and the final decks situation
def winnerGame(d, gameID):
    roundID = 0
    thisGameID = gameID
    used = []
    while len(d[0])>0 and len(d[1])>0:
        roundID += 1
        print(thisGameID, roundID)
        print(d)
        #if d in used:
        #    return 0, d
        #used.append(copy.deepcopy(d))
        if roundID > 600:
            return 0, d
        draws = (d[0][0], d[1][0])
        d[0].pop(0)
        d[1].pop(0)
        if draws[0] <= len(d[0]) and draws[1] <= len(d[1]):
            newD = [[], []]
            for i in range(draws[0]):
                newD[0].append(d[0][i])
            for i in range(draws[1]):
                newD[1].append(d[1][i])
            gameID += 1
            w, _ = winnerGame(newD, gameID)
            d[w].append(draws[w])
            d[w].append(draws[1-w])
        else:
            if draws[0]>draws[1]:
                d[0].append(draws[0])
                d[0].append(draws[1])
            else:
                d[1].append(draws[1])
                d[1].append(draws[0])
    if len(d[0]) == 0:
        return 1, d
    else:
        return 0, d

finalWinner, finalDecks = winnerGame(decks, 1)
res = 0
for i in range(len(finalDecks[finalWinner])):
    res += (len(finalDecks[finalWinner])-i)*finalDecks[finalWinner][i]

print(res)