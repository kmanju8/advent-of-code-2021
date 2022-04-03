import numpy as np

file = open('./input.txt', 'r')

points = []
line = file.readline().strip()
while line:
    points.append([int(i) for i in line.replace(' -> ', ',').split(",")])
    line = file.readline().strip()

# all coordinates between 0 and 1000, found in quick test
board = np.zeros((1000,1000))

for i in range(len(points)):

    if points[i][0]==points[i][2] and points[i][1]==points[i][3]:
        board[points[i][0]][points[i][1]]+=1
    elif points[i][0]==points[i][2]:
        board[points[i][0]][min(points[i][1],points[i][3]):max(points[i][1],points[i][3])+1]+=1
    elif points[i][1]==points[i][3]:
        board[:,points[i][1]][min(points[i][0],points[i][2]):max(points[i][0],points[i][2])+1]+=1
    # only needs to handle 45 deg stuff
    else:
        if (points[i][0]-points[i][2])*(points[i][1]-points[i][3])>0:
            for j in range(abs(points[i][2]-points[i][0])+1):
                board[min(points[i][0],points[i][2])+j][min(points[i][1],points[i][3])+j]+=1
        else:
            for j in range(abs(points[i][2]-points[i][0])+1):
                board[min(points[i][0],points[i][2])+j][max(points[i][1],points[i][3])-j]+=1

file.close()
print((board > 1).sum())
