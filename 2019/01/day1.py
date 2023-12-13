f = open("input.txt", "r")
num = []
for l in f:
    num.append(int(l))
f.close()

# part 1
sum = 0
for n in num:
    r = int(n/3) - 2
    sum += r
print(sum)

# part 2
sum = 0
for n in num:
    r = n
    while r>0:
        r = int(r/3) - 2
        if r>0:
            sum += r
print(sum)