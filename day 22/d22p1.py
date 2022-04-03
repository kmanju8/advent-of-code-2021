# maybe let's try to solve for the first example first for the more complicated method
# maybe let's carve into subcuboids
# maybe also should do in 2d first

def volume(cube):
    vol=1
    for i in range(3):
        vol*=(cube[i][1]-cube[i][0])+1
    return(vol)

# finds number of points of new cube in old (points of intersection)
# will probably use in reverse as well
def poi(old, new):
    total=0
    for i in range(len(new)):
        for j in range(2):
            if old[i][0]<=new[i][j]<=old[i][1]:
                total+=1
    
    if total<3:
        return(0)

    return(2**(total-3))

file = open('./input.txt', 'r')
line = file.readline().strip()

# let's do this focusing on volumes only
grid=set()
counter=0
while line:
    counter+=1
    split = [i[2:] for i in line.replace(',',' ').split()]
    # tidy is the newly added cuboid.
    current = tuple([tuple(i.split('..')) for i in split])

    # bulk of code

    i
    
    


    
    line = file.readline().strip()



for i in grid:
    print(i)
