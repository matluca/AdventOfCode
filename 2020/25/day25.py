cpk = 17773298 # card's public key
dpk = 15530095 # door's public key

subject = 1
# finding card's loop size
found = False
cardLoop = 0
while not found:
    subject = subject * 7
    subject = subject % 20201227
    cardLoop += 1
    #print(cardLoop, subject)
    if subject == cpk:
        found = True

# finding door's loop size
subject = 1
found = False
doorLoop = 0
while not found:
    subject = subject * 7
    subject = subject % 20201227
    doorLoop += 1
    #print(doorLoop, subject)
    if subject == dpk:
        found = True

# finding encryption key
def transform(s, ls):
    res = 1
    for i in range(ls):
        res = res * s
        res = res % 20201227
    return res

print(transform(dpk, cardLoop))
print(transform(cpk, doorLoop))
