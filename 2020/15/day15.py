f = open("input.txt", "r")
input = []
for l in f:
    input = l.split(",")
f.close()
for i in range(len(input)):
    input[i] = int(input[i])

lastSpoken = {}
for i in range(len(input)-1):
    lastSpoken[input[i]] = i+1
round = len(input) + 1
last = input[len(input)-1]

while round <= 30000000:
    next = 0
    try:
        next = round - lastSpoken[last] - 1
    except:
        pass
    lastSpoken[last] = round - 1
    last = next
    round = round + 1

print(last)
