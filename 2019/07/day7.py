import itertools

def intcode(program, input):
    op = 0
    while True:
        opcode = program[op]%100
        r = int(program[op]/100)
        modes = [0] * 3
        i = 0
        while r>0:
            modes[i] = r%10
            r = int(r/10)
            i += 1
        if opcode == 99:
            return program
        elif opcode == 1:
            parameters = program[op+1:op+4]
            values = []
            for i in range(len(parameters)):
                if modes[i] == 0:
                    values.append(program[parameters[i]])
                elif modes[i] == 1:
                    values.append(parameters[i])
            program[program[op+3]] = values[0] + values[1]
            op += 4
        elif opcode == 2:
            parameters = program[op+1:op+4]
            values = []
            for i in range(len(parameters)):
                if modes[i] == 0:
                    values.append(program[parameters[i]])
                elif modes[i] == 1:
                    values.append(parameters[i])
            program[program[op+3]] = values[0] * values[1]
            op += 4
        elif opcode == 3:
            parameters = program[op+1:op+2]
            values = []
            for i in range(len(parameters)):
                if modes[i] == 0:
                    values.append(program[parameters[i]])
                elif modes[i] == 1:
                    values.append(parameters[i])
            program[program[op+1]] = input.pop()
            op += 2
        elif opcode == 4:
            parameters = program[op+1:op+2]
            values = []
            for i in range(len(parameters)):
                if modes[i] == 0:
                    values.append(program[parameters[i]])
                elif modes[i] == 1:
                    values.append(parameters[i])
            return values[0]
            op += 2
        elif opcode == 5:
            parameters = program[op+1:op+3]
            values = []
            for i in range(len(parameters)):
                if modes[i] == 0:
                    values.append(program[parameters[i]])
                elif modes[i] == 1:
                    values.append(parameters[i])
            if values[0] != 0:
                op = values[1]
            else:
                op += 3
        elif opcode == 6:
            parameters = program[op+1:op+3]
            values = []
            for i in range(len(parameters)):
                if modes[i] == 0:
                    values.append(program[parameters[i]])
                elif modes[i] == 1:
                    values.append(parameters[i])
            if values[0] == 0:
                op = values[1]
            else:
                op +=3
        elif opcode == 7:
            parameters = program[op+1:op+4]
            values = []
            for i in range(len(parameters)):
                if modes[i] == 0:
                    values.append(program[parameters[i]])
                elif modes[i] == 1:
                    values.append(parameters[i])
            if values[0] < values[1]:
                program[program[op+3]] = 1
            else:
                program[program[op+3]] = 0
            op += 4
        elif opcode == 8:
            parameters = program[op+1:op+4]
            values = []
            for i in range(len(parameters)):
                if modes[i] == 0:
                    values.append(program[parameters[i]])
                elif modes[i] == 1:
                    values.append(parameters[i])
            if values[0] == values[1]:
                program[program[op+3]] = 1
            else:
                program[program[op+3]] = 0
            op += 4

f = open("input.txt", "r")
input = []
for l in f:
    line = l.split(",")
    for i in range(len(line)):
        line[i] = int(line[i])
    input = line
f.close()

def value(phases):
    v = 0
    for i in range(5):
        v = intcode(input.copy(), [v, phases[i]])
    return v

possiblePhases = list(itertools.permutations([0,1,2,3,4]))

maxValue = 0
for p in possiblePhases:
    v = value(p)
    if v > maxValue:
        maxValue = v

print(maxValue)