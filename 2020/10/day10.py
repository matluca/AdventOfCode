f = open("input.txt", "r")
data = []
for l in f:
    data.append(int(l))
f.close()
data.sort()

joltage = 0
diffs = []
for i in data:
    diff = i - joltage
    joltage = i
    diffs.append(diff)
diffs.append(3)
print("product:", diffs.count(1)*diffs.count(3))

streaks = []
streak = 0
for i in range(len(diffs)-1):
    if diffs[i] == 1:
        streak = streak + 1
    else:
        if streak > 0:
            streaks.append(streak)
        streak = 0
if streak > 0:
    streaks.append(streak)
value = 1
for s in streaks:
    if s<4:
        value = value * pow(2,s-1)
    else:
        value = value * pow(2,s-4) * 7
print(value)