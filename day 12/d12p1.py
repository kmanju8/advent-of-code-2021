def traverse(map, current_loc, caves, reverse):
    if current_loc==caves["end"]:
        return 1

    total=0
    for i in range(len(map)):
        # if path can be traversed, will try to traverse it
        # indexing is map[from][to]
        if map[current_loc][i]>0:
            a=[]
            for y in map:
                a.append(list(y))
            # make impossible to go back to if small
            if reverse[current_loc].islower():
                for j in range(len(a)):
                    a[j][current_loc]=0
            total += traverse(a, i, caves, reverse)

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
    map[caves[i[0]]][caves[i[1]]], map[caves[i[1]]][caves[i[0]]] = 1, 1

print(traverse(map, caves["start"], caves, reverse))
