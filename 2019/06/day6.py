# part 1
orbits = {}
f = open("input.txt", "r")
for l in f:
    a, b = l.rstrip().split(")")
    orbits[b] = a
f.close()

tot = 0
for pl in orbits.keys():
    planet = pl
    while planet != 'COM':
        tot += 1
        planet = orbits[planet]

print(tot)

# part 2
you = []
planet = 'YOU'
while planet != 'COM':
    planet = orbits[planet]
    you.append(planet)

san = 'SAN'
while True:
    san = orbits[san]
    if san in you:
        break
print(san)

def distance(pl1, pl2):
    planet = orbits[pl1]
    steps = 0
    while planet != pl2:
        steps += 1
        planet = orbits[planet]
    return steps

print(distance("YOU", san) + distance("SAN", san))
