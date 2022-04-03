def xfold(grid,sym):
    toremove=[]
    toadd=[]
    for point in grid:
        if point[0]<sym:
            toremove.append(point)
            toadd.append((2*sym-point[0],point[1]))
    for point in toremove:
        grid.remove(point)
    for point in toadd:
        grid.add(point)

file = open('./input.txt', 'r')
points = []
line = file.readline().strip()
while line:
    points.append([int(i) for i in line.split(",")])
    line = file.readline().strip()

grid = set()
for i in points:
    if tuple(i) not in grid:
        grid.add(tuple(i))

xfold(grid,655)

print(len(grid))