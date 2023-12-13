# teorema cinese del resto
f = open("input.txt", "r")
data = f.read()
data = data.split('\n')

buses = data[1].split(',')
busesCopy = []
for k in range(len(buses)):
    bus = buses[k]
    if bus != 'x':
        busesCopy.append([int(bus),k])

N=1
listN=[]
listy=[]
sum=0

for bus in busesCopy:
    N=N*bus[0]
    
for bus in busesCopy:
    listN.append(int(N/bus[0]))
    found = False
    k=N/bus[0]
    while not found:
        if k%bus[0]==1:
            listy.append(int(k*bus[0]/N))
            found=True
        k = k + N/bus[0]

for k in range(len(listy)):
    a = listy[k]*listN[k]*(busesCopy[k][0]-busesCopy[k][1])
    sum = sum + a

print(sum%N)