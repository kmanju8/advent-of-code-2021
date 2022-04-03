def new_square(length, value):
    a=[]
    for i in range(length):
        a.append([value]*(length))
    return(a)

def neighbour_dist(cavern,risk,i,j,wall,visited,needvisit):
    neighbours=((-1,0),(1,0),(0,-1),(0,1))
    for x in neighbours:
        if i+x[0]>=0 and j+x[1]>=0 and i+x[0]<wall and j+x[1]<wall:
            if risk[i+x[0]][j+x[1]]>risk[i][j]+cavern[i+x[0]][j+x[1]]:
                risk[i+x[0]][j+x[1]]=risk[i][j]+cavern[i+x[0]][j+x[1]]
                if not visited[i+x[0]][j+x[1]]:
                    needvisit[(i+x[0],j+x[1])]=risk[i+x[0]][j+x[1]]

cavern = [[int(j) for j in i[:-1]] for i in open('input.txt')]
wall=len(cavern)

visited = new_square(wall,False)
risk = new_square(wall,100000)
needvisit={}
i,j = 0,0
risk[i][j]=0
while i!=wall-1 or j!=wall-1:
    # update that it has been visited
    visited[i][j] = True
    needvisit.pop((i,j), None)

    # calculate distance to all neighbours. Update if smaller than current
    neighbour_dist(cavern,risk,i,j,wall,visited,needvisit)

    # move to unvisited with smallest cost
    nextnode=min(needvisit, key=needvisit.get)
    i,j = nextnode[0],nextnode[1]

print(risk[wall-1][wall-1])