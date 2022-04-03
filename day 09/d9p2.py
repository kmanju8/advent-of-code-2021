# Recursive function to calculate the size of a given basin.
# Given a single point in basin, calculates basin size while deleting basin.
def calculate_basin(heights,i,j):
    if heights[i][j]<9:
        heights[i][j]=10
        return(1+calculate_basin(heights,i-1,j)+calculate_basin(heights,i+1,j)+calculate_basin(heights,i,j-1)+calculate_basin(heights,i,j+1))
    else:
        return 0

size=100
total=0

# load into 2d array, with banding of 10s
heights = [[10]*(size+2)]+[([10]+[int(j) for j in i[:-1]]+[10]) for i in open('input.txt')]+[[10]*(size+2)]

basins=[]
for i in range(1,size+1):
    for j in range(1,size+1):
        # finds a point in a basin.
        if heights[i][j] < 9:
            basins.append(calculate_basin(heights,i,j))

basins.sort(reverse=True)
print(basins[0]*basins[1]*basins[2])