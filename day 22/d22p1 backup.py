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

# let's say that grid contains 3d cuboids with no overlapping points
grid=set()
counter=0
while line:
    counter+=1
    split = [i[2:] for i in line.replace(',',' ').split()]
    # tidy is the newly added cuboid.
    tidy = tuple([tuple(i.split('..')) for i in split])

    # is an on shape
    if tidy[0][0]=='':
        # can actually unindent the below, make the above conditional just
        # set add tidy
        tempgrid=set()
        addtidy = True
        # best programatically would be to break down the old shape, and keep the new shape whole (for the purposes of recursion).
        # so this for loop is only about adding in old cuboids/broken down cuboids
        for cuboid in grid:
            # when on 'on' cub intersects another, can always be broken down into at most 3 cubes: one cube stays the same, the other breaks into two smaller.
            match poi(cuboid, tidy[1:]):
                # old shape engulf new
                case 8:
                    tempgrid.add(cuboid)
                    addtidy = False
                    break
                # 4 points of new in old; make old into 5? Honestly probably simpler to
                # make new smaller and change tidy.
                case 4:
                    tempgrid.add(cuboid)
                    # shorten tidy
                    for i in range(len(tidy)):
                        for j in range(2):
                            if not cuboid[i][0]<=tidy[i][j]<=cuboid[i][1]:
                                temp=list(tidy)
                                temp[i] = (tidy[i][j],cuboid[i][0]-1) if j==0 else (cuboid[i][1]+1,tidy[i][j])
                                tidy=tuple(temp)
                # if two points in new in old, break old into 4
                case 2:
                    singlein=[]
                    bounds = -1
                    for i in range(len(tidy)):
                        if cuboid[i][0]<=tidy[i][0]<=cuboid[i][1] and cuboid[i][0]<=tidy[i][1]<=cuboid[i][1]:
                            temp1, temp2 = list(cuboid),list(cuboid)
                            temp1[i], temp2[i]= (cuboid[i][0],tidy[i][0]-1),(tidy[i][1]+1,cuboid[i][1])
                            tempgrid.add(tuple(temp1))
                            tempgrid.add(tuple(temp2))
                            bounds = i
                        elif cuboid[i][0]<=tidy[i][0]<=cuboid[i][1]:
                            singlein.append((i,0))
                        elif cuboid[i][0]<=tidy[i][1]<=cuboid[i][1]:
                            singlein.append((i,1))
                        # add remaining
                        temp3,temp4=list(cuboid),list(cuboid)
                        temp3[bounds] = (tidy[bounds][0],tidy[bounds][1])
                        temp4[bounds] = (tidy[i][0],tidy[i][1])

                        # want to redo
                        singlein[0]
                        for j in singlein:
                            if j[1]==0:
                                temp3[j[0]] == ((cuboid[j[1]][0],tidy[j[1]][0]-1))
                                temp4[j[0]] == ((cuboid[j[1]][0],tidy[j[1]][0]-1))
                                
                            else:
                                pass
                            
                        
                        
                # if one point in one in other, or two of old in new, break old into 3
                case 1:
                    pass
                case _:
                    match poi(tidy[1:],cuboid):
                        # new shape engulfs the other
                        # replace old with new
                        case 8:
                            continue
                        case 4:
                            pass
                        case 2:
                            pass
                        # no shared space
                        case _:
                            tempgrid.add(cuboid)

        if addtidy:
            tempgrid.add(tidy[1:])
        grid=tempgrid

    # if an off shape
    else:
        for cuboid in grid:
            # when 'off' cub intersects 'on' cube, just have to break 'on' cube down into 2 cubes.
            # if one/two point in one in other
            if True:
                pass
            # 'off' cube eclipses 'on' cube in two dimensions. this results in 'on' cube simply being resized actually very simialr to case for 'on'-'on'
            # if 
            elif True:
                pass
            # new shape engulfs the other. Delete old shape
            elif True:
                pass
            # 'off' shape engulf new. Definitely hardest part of this task... or is it. breaks down into 6 pieces.
            elif True:
                pass
            else:
                print("fail to remove", cube, tidy[1:])


    
    line = file.readline().strip()

# total=0
# for cube in grid:
#     total += volume(cube)
# print(volume)

for i in grid:
    print(i)
