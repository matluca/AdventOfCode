def isValid(key, value):
    if key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if key == 'pid':
        return (value.isnumeric() and (len(value) == 9))
    if key == 'eyr':
        return (value.isnumeric() and (int(value) >= 2020) and (int(value) <= 2030))
    if key == 'hcl':
        if ((len(value) != 7) or (value[0] != '#')):
            return False
        v = True
        for c in value[1:]:
            v = v and c in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        return v
    if key == 'byr':
        return (value.isnumeric() and (int(value) >= 1920) and (int(value) <= 2002))
    if key == 'iyr':
        return (value.isnumeric() and (int(value) >= 2010) and (int(value) <= 2020))
    if key == 'hgt':
        n = value[:-2]
        unit = value[-2:]
        if unit == 'cm':
            return (n.isnumeric() and (int(n) >= 150) and (int(n) <= 193))
        if unit == 'in':
            return (n.isnumeric() and (int(n) >= 59) and (int(n) <= 76))
        return False
    return key == 'cid'

f = open("input.txt", "r")
lines = []
passports = [""]
pID = 0
for line in f:
    if len(line) != 1:
        passports[pID] = passports[pID] + " " + line.rstrip()
    else:
        pID = pID + 1
        passports.append("")

f.close()

want_keys=['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

valid = 0
for p in passports:
    pairs = p.split(" ")
    keys = []
    v = True
    for pair in pairs[1:]:
        split = pair.split(":")
        key = split[0]
        try:
            value = split[1]
        except:
            break
        keys.append(key)
        v = v and isValid(key, value)
    if (v and (set(want_keys) <= set(keys))):
        valid = valid + 1

print(valid)
