def result(program, input):
    op = 0
    while True:
        opcode = program[op]%100
        r = program[op]/100
        modes = [0] * 3
        i = 0
        while r>0:
            modes[i] = r%10
            r = r/10
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
            program[program[op+1]] = input
            op += 2
        elif opcode == 4:
            parameters = program[op+1:op+2]
            values = []
            for i in range(len(parameters)):
                if modes[i] == 0:
                    values.append(program[parameters[i]])
                elif modes[i] == 1:
                    values.append(parameters[i])
            print(values[0])
            op += 2
    return inp

# part 1
f = open("input.txt", "r")
input = []
for l in f:
    line = l.split(",")
    for i in range(len(line)):
        line[i] = int(line[i])
    input = line
f.close()

result(input, 1)

# part 2
def result2(program, input):
    op = 0
    while True:
        opcode = program[op]%100
        r = program[op]/100
        modes = [0] * 3
        i = 0
        while r>0:
            modes[i] = r%10
            r = r/10
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
            program[program[op+1]] = input
            op += 2
        elif opcode == 4:
            parameters = program[op+1:op+2]
            values = []
            for i in range(len(parameters)):
                if modes[i] == 0:
                    values.append(program[parameters[i]])
                elif modes[i] == 1:
                    values.append(parameters[i])
            print(values[0])
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

    return inp

f = open("input.txt", "r")
input = []
for l in f:
    line = l.split(",")
    for i in range(len(line)):
        line[i] = int(line[i])
    input = line
f.close()
result2(input, 5)