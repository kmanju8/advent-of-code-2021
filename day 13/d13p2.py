import numpy as np
from PIL import Image

def fold(grid,sym, x):
    toremove=[]
    toadd=[]
    if x:
        for point in grid:
            if point[0]<sym:
                toremove.append(point)
                toadd.append((2*sym-point[0],point[1]))
    else:
        for point in grid:
            if point[1]>sym:
                toremove.append(point)
                toadd.append((point[0],2*sym-(point[1])))
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

# folds
xorigin=0
line = file.readline().strip()
while line:
    if line[11]=="x":
        fold(grid, xorigin+int(line[13:]),True)
        xorigin+=int(line[13:])+1
    else:
        fold(grid,int(line[13:]), False)
    line=file.readline().strip()

# printing
pic = np.zeros( (7,50) )+255
for i in grid:
    pic[i[1]][i[0]-xorigin]=0
img = Image.fromarray( pic )       
img.show()    