def flash(points,i,j):
    points[i][j]=None
    for x in range(-1,2):
        for y in range(-1,2):
            if i+x<0 or i+x>9 or j+y<0 or j+y>9:
                continue
            elif points[i+x][j+y]==None:
                continue
            points[i+x][j+y]+=1
            if points[i+x][j+y]>9:
                flash(points,i+x,j+y)

STEPS=100
counter=0

file = open('./input.txt', 'r')
points = [[int(j) for j in i[:-1]] for i in file]

for x in range(STEPS):
    for i in range(len(points)):
        for j in range(len(points[0])):
            if points[i][j]==None:
                continue
            points[i][j]+=1
            if points[i][j]>9:
                flash(points,i,j)

    for i in range(len(points)):
        for j in range(len(points[0])):
            if points[i][j]==None:
                counter+=1
                points[i][j]=0

print(counter)
