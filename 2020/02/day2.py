#part 1
f = open("input.txt", "r")
n = 0
valid =0
for line in f:
    n = n+1
    firstSplit = line.split("-", 1)
    min = int(firstSplit[0])
    secondSplit = firstSplit[1].split(" ", 1)
    max = int(secondSplit[0])
    thirdSplit = secondSplit[1].split(": ", 1)
    letter = thirdSplit[0]
    password = thirdSplit[1]
    occurrences = password.count(letter)
    if (occurrences >= min) and (occurrences <= max):
        valid = valid + 1

print(valid)
f.close()

#part 2
f = open("input.txt", "r")
n = 0
valid =0
for line in f:
    n = n+1
    firstSplit = line.split("-", 1)
    min = int(firstSplit[0])
    secondSplit = firstSplit[1].split(" ", 1)
    max = int(secondSplit[0])
    thirdSplit = secondSplit[1].split(": ", 1)
    letter = thirdSplit[0]
    password = thirdSplit[1]
    occurrences = password.count(letter)
    if (password[min-1] == letter) != (password[max-1] == letter):
        valid = valid + 1

print(valid)
f.close()