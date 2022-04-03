def traverse(map, current_loc, caves, reverse, time):
    if current_loc==caves["end"]:
        return 1

    temp=bool(time)
    total=0
    for i in range(len(map)):
        # if path can be traversed, will try to traverse it
        # indexing is map[from][to]
        if map[current_loc][i]>0:
            a=[]
            temp=bool(time)
            for y in map:
                a.append(list(y))  
            if reverse[i].islower():
                for j in range(len(a)):
                    a[j][i]-=1
                    if a[j][i]==0 and not temp:
                        for x in range(len(a)):
                            for y in range(len(a)):
                                a[x][y] -= 1
                        temp=True 

            total += traverse(a, i, caves, reverse, temp)

    return(total)

file = open('./input4.txt', 'r')
connections = []
line = file.readline().strip()
while line:
    connections.append([i for i in line.split("-")])
    line = file.readline().strip()

# figure out cave-index mapping for connection map
caves = {}
count=0
for i in connections:
    for j in i:
        if j not in caves:
            caves[j] = count
            count+=1
reverse = {v:k for k,v in caves.items()}

# create connection map
map=[]
for i in range(len(caves)):
    map.append([0]*len(caves))
for i in connections:
    map[caves[i[0]]][caves[i[1]]], map[caves[i[1]]][caves[i[0]]] = 2, 2

time = False
for j in range(len(map)):
    map[j][caves["start"]]=0 

ans = (traverse(map, caves["start"], caves, reverse, time))

print(ans)
