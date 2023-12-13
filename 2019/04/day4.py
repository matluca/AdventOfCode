# part 1
minimum = 236491
maximum = 713787

def isValid(n):
    last = n%10
    digits = []
    while n>0:
        d = n%10
        if d > last:
            return False
        digits.append(d)
        last = d
        n = n/10
    return len(list(set(digits)))<len(digits)

assert isValid(111111)
assert not isValid(223450)
assert not isValid(123789)
assert not isValid(713779)

tot = 0
for n in range(minimum, maximum+1):
    if isValid(n):
        tot += 1
print(tot)


# part 2
def isValid2(n):
    last = n%10
    digits = []
    while n>0:
        d = n%10
        if d > last:
            return False
        digits.append(d)
        last = d
        n = n/10
    occ = [0]*10
    for i in range(10):
        occ[i] = digits.count(i)
    return (2 in occ)

assert not isValid2(111111)
assert isValid2(111122)
assert not isValid2(123444)
assert isValid2(112233)

tot = 0
for n in range(minimum, maximum+1):
    if isValid2(n):
        tot += 1
print(tot)
