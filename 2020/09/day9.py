def valid(n, size):
    sums = []
    for i in range(size):
        for j in range(i, size):
            if data[n-size+i] != data[n-size+j]:
                sums.append(data[n-size+i] + data[n-size+j])
    return (data[n] in sums)

f = open("input.txt", "r")

data = []
for l in f:
    data.append(int(l))
f.close()

size = 25
target = 0
for i in range(size, len(data)):
    if (not valid(i, size)):
        target = data[i]
        break
print("target:", target)

for i in range(len(data)):
    j = i+1
    sum = data[i] + data[j]
    while sum < target:
        j = j + 1
        sum = sum + data[j]
    if sum == target:
        print("start:", data[i], "end:", data[j])
        subset = data[i:j]
        print("min:", min(subset), "max:", max(subset), "sum:", min(subset) + max(subset))
        break
