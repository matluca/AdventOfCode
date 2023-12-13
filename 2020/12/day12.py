import numpy
f = open("input.txt", "r")
instr = []
for line in f:
    instr.append((line[0], int(line[1:])))
f.close()

pos = numpy.array([0,0])
waypoint = numpy.array([1,0])
for i in instr:
    #print(i, pos, dir)
    if i[0] == 'N':
        pos = pos + numpy.array([0,1])*i[1]
    elif i[0] == 'S':
        pos = pos + numpy.array([0,-1])*i[1]
    elif i[0] == 'E':
        pos = pos + numpy.array([1,0])*i[1]
    elif i[0] == 'W':
        pos = pos + numpy.array([-1,0])*i[1]
    elif i[0] == 'F':
        pos = pos + waypoint*i[1]
    elif i[0] == 'R':
        if i[1] == 90:
            m = numpy.array([[0,1],[-1,0]]),
            waypoint = numpy.matmul(m, waypoint)[0]
        elif i[1] == 270:
            m = numpy.array([[0,-1],[1,0]]),
            waypoint = numpy.matmul(m, waypoint)[0]
        elif i[1] == 180:
            waypoint = -waypoint
    elif i[0] == 'L':
        if i[1] == 90:
            m = numpy.array([[0, -1],[1, 0]]),
            waypoint = numpy.matmul(m, waypoint)[0]
        elif i[1] == 270:
            m = numpy.array([[0,1],[-1,0]]),
            waypoint = numpy.matmul(m, waypoint)[0]
        elif i[1] == 180:
            waypoint = -waypoint
print(pos)

mdist = abs(pos[0])+abs(pos[1])
print(mdist)

#part 2
pos = numpy.array([0,0])
waypoint = numpy.array([10,1])
for i in instr:
    #print(i, pos, waypoint)
    if i[0] == 'N':
        waypoint = waypoint + numpy.array([0,1])*i[1]
    elif i[0] == 'S':
        waypoint = waypoint + numpy.array([0,-1])*i[1]
    elif i[0] == 'E':
        waypoint = waypoint + numpy.array([1,0])*i[1]
    elif i[0] == 'W':
        waypoint = waypoint + numpy.array([-1,0])*i[1]
    elif i[0] == 'F':
        pos = pos + waypoint*i[1]
    elif i[0] == 'R':
        if i[1] == 90:
            m = numpy.array([[0,1],[-1,0]]),
            waypoint = numpy.matmul(m, waypoint)[0]
        elif i[1] == 270:
            m = numpy.array([[0,-1],[1,0]]),
            waypoint = numpy.matmul(m, waypoint)[0]
        elif i[1] == 180:
            waypoint = -waypoint
    elif i[0] == 'L':
        if i[1] == 90:
            m = numpy.array([[0, -1],[1, 0]]),
            waypoint = numpy.matmul(m, waypoint)[0]
        elif i[1] == 270:
            m = numpy.array([[0,1],[-1,0]]),
            waypoint = numpy.matmul(m, waypoint)[0]
        elif i[1] == 180:
            waypoint = -waypoint
print(pos)

mdist = abs(pos[0])+abs(pos[1])
print(mdist)

