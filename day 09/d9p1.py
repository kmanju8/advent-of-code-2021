size=100
total=0

# load into 2d array, with banding of 10s
heights = [[10]*(size+2)]+[([10]+[int(j) for j in i[:-1]]+[10]) for i in open('input.txt')]+[[10]*(size+2)]

for i in range(1,size+1):
    for j in range(1,size+1):
        total += (1+heights[i][j]) if heights[i][j]<min([heights[i-1][j],heights[i+1][j],heights[i][j-1],heights[i][j+1]]) else 0

print(total)