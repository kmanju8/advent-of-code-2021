import numpy as np

file = open('./input.txt', 'r')

points = []
for i in range(500):
    line = file.readline().strip().replace(' -> ', ',').split(",")
    points.append([int(i) for i in line])

# all coordinates between 0 and 1000, found in quick test
board = np.zeros((1000,1000))

for i in range(500):

    if points[i][0]==points[i][2] and points[i][1]==points[i][3]:
        board[points[i][0]][points[i][1]]+=1
    elif points[i][0]==points[i][2]:
        board[points[i][0]][min(points[i][1],points[i][3]):max(points[i][1],points[i][3])+1]+=1
    elif points[i][1]==points[i][3]:
        board[:,points[i][1]][min(points[i][0],points[i][2]):max(points[i][0],points[i][2])+1]+=1

file.close()
print((board > 1).sum())
