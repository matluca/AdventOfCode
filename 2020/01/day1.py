#part 1
f = open("input.txt", "r")
numbers = []
for line in f:
    x = int(line)
    if (2020-x) in numbers:
        print("Result: %d * %d = %d" % (x, 2020-x, x*(2020-x)))
        break
    numbers.append(x)
f.close()

#part 2
f = open("input.txt", "r")
numbers = []
for line in f:
    numbers.append(int(line))
f.close()

for i in range(1, len(numbers)):
    for j in range (i+1, len(numbers)):
        if (2020-numbers[i]-numbers[j]) in numbers:
            a = numbers[i]
            b = numbers[j]
            print("Result: %d * %d * %d = %d" % (a, b, 2020-a-b, (2020-a-b)*a*b ))
            break
