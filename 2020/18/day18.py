def evaluate(e):
    currentN = 0
    currentOp = ''
    length = len(e)
    finish = False
    i = 0
    while not finish:
        c = e[i]
        if c.isdigit():
            currentN = handleNumber(currentN, int(c), currentOp)
        if c in ['+', "*"]:
            currentOp = c
        if c == '(':
            counter = 1
            closed = False
            j = 1
            while not closed:
                if e[i+j] == '(':
                    counter = counter+1
                if e[i+j] == ')':
                    counter = counter-1
                if counter == 0:
                    closed = True
                j = j + 1
            number = evaluate(e[i+1:i+j-1])
            currentN = handleNumber(currentN, number, currentOp)
            i = i + j - 1
        i = i + 1
        if i == length:
            finish = True
    return currentN
            
def handleNumber(n, m, op):
    if op == '':
        return m
    else:
        if op == '+':
            return n + m
        if op == '*':
            return n * m

def evaluate2(e):
    currentN = 0
    currentOp = ''
    length = len(e)
    finish = False
    i = 0
    while not finish:
        c = e[i]
        if c.isdigit():
            currentN = handleNumber2(currentN, int(c), currentOp)
        elif c == '+':
            currentOp = c
        elif c == '*':
            currentOp = c
            parenteses = 0
            closed = False
            j = 1
            while not closed:
                if i+j == length:
                    closed = True
                else:
                    if e[i+j] == '(':
                        parenteses = parenteses + 1
                    if e[i+j] == ')':
                        parenteses = parenteses - 1
                    if (e[i+j] == '*' and parenteses <= 0):
                        closed = True
                j = j + 1
            number = evaluate2(e[i+1:i+j-1])
            currentN = handleNumber2(currentN, number, currentOp)
            i = i + j - 2
        elif c == '(':
            counter = 1
            closed = False
            j = 1
            while not closed:
                if e[i+j] == '(':
                    counter = counter+1
                if e[i+j] == ')':
                    counter = counter-1
                if counter == 0:
                    closed = True
                j = j + 1
            number = evaluate2(e[i+1:i+j-1])
            currentN = handleNumber2(currentN, number, currentOp)
            i = i + j - 1
        i = i + 1
        if i == length:
            finish = True
    return currentN
            
def handleNumber2(n, m, op):
    if op == '':
        return m
    else:
        if op == '+':
            return n + m
        if op == '*':
            return n * m



f = open("input.txt", "r")
expr = []
for l in f:
    expr.append(l.rstrip())
f.close()

sum = 0
for i in range(len(expr)):
    sum = sum + evaluate(expr[i])
print(sum)

sum = 0
for i in range(len(expr)):
    sum = sum + evaluate2(expr[i])
print(sum)