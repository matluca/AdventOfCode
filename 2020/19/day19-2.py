import re

max_depth = 6
rules = {}

with open("input.txt", "r") as fp:
    rawRules, vals = fp.read().split("\n\n")


mrules = re.findall(r"([\d]+): (.*)", rawRules)

for r in mrules:
    rules[r[0]] = r[1].split(" ")

messages = vals.split("\n")

def resolveRule(ruleset, rn, depth = 0):
    s = ""

    for r in ruleset[rn]:
        if r.isdigit():
            if r == rn:
                depth += 1
            if depth != max_depth:
                s += resolveRule(ruleset, r, depth)
        elif r == "|":
            s += r
        else:
            s += re.search(r'"([ab])"', r)[1]
    return "(?:{})".format(s)


reg = resolveRule(rules, "0")

print(reg)


tot = 0
for msg in messages:
    m = re.match("^{}$".format(reg), msg)
    if m:
        tot += 1

print("Tot", tot)