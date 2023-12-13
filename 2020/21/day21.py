f = open("input.txt", "r")
ingredients = []
allergens = []
for line in f:
    ing, al = line.split(" (contains ")
    ingredients.append(ing.split(" "))
    allergens.append(al.replace(")\n", "").split(", "))
f.close()

possibilities = {}
for i in range(len(ingredients)):
    for a in allergens[i]:
        try:
            possibilities[a] = list(set(possibilities[a]) & set(ingredients[i]))
        except:
            possibilities[a] = ingredients[i]

def isPossible(ingredient):
    for v in possibilities.values():
        if ingredient in v:
            return True
    return False

tot = 0
for i in range(len(ingredients)):
    for j in ingredients[i]:
        if (not isPossible(j)):
            tot = tot + 1
print(tot)

# part 2

def isSimplified(possib):
    for v in possib.values():
        if len(v) != 1:
            return False
    return True

max_iter = 30
i = 0
while (not isSimplified(possibilities) and i != max_iter):
    i = i+1
    for k in possibilities.keys():
        if len(possibilities[k]) == 1:
            value = possibilities[k][0]
            for h in possibilities.keys():
                if h != k:
                    try:
                        possibilities[h].remove(value)
                    except:
                        pass

resKeys = ""
result = ""
for k in sorted(possibilities):
    resKeys = resKeys + k + ","
    result = result + possibilities[k][0] + ","
print(resKeys[:-1])
print(result[:-1])
