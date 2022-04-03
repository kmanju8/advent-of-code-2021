file = open('./input.txt', 'r')
line = file.readline().strip()

grid=set()
counter=0
while line:
    print(counter)
    counter+=1
    split = [i[2:] for i in line.replace(',',' ').split()]
    tidy = [i.split('..')for i in split]
    
    if tidy[0][0]=='':
        for i in range(int(tidy[1][0]),int(tidy[1][1])+1):
            for j in range(int(tidy[2][0]),int(tidy[2][1])+1):
                for k in range(int(tidy[3][0]),int(tidy[3][1])+1):
                    grid.add((i,j,k))
    else:
        for i in range(int(tidy[1][0]),int(tidy[1][1])+1):
            for j in range(int(tidy[2][0]),int(tidy[2][1])+1):
                for k in range(int(tidy[3][0]),int(tidy[3][1])+1):
                    if (i,j,k) in grid:
                        grid.remove((i,j,k))

    line = file.readline().strip()

print(len(grid))
