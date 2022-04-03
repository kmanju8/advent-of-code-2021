# finds magnitude cubed. No point in rooting, as just focused on relatives not absolutes
def magnitude(a,b):
    mag=0
    for i in range(3):
        mag+=(a[i]-b[i])**2
    return(mag)

# finds number of values present in both of two separate lists
def same_vals(a,b):
    counter=0
    for i in a:
        if i in b:
            counter+=1
    return(counter)

# a and b are vectors. a is reference vector, b is transformer. want to find b to a.
# this is a (imo) kinda nice but hacky workaround to calculating the rotation
def find_rotation(a,b):
    rot=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(a)):
        if abs(a[i])==abs(b[0]):
            rot[i][0]=int(b[0]/a[i])
        elif abs(a[i])==abs(b[1]):
            rot[i][1]=int(b[1]/a[i])
        elif abs(a[i])==abs(b[2]):
            rot[i][2]=int(b[2]/a[i])
        else:
            print("check this out")

    for i in rot:
        if list(i)==list([0,0,0]):
            print(rot)
    return(rot)

# multiply point/vector by rotation matrix
def matrix_mult(matrix, arr):
    arr2=[]
    for i in matrix:
        arr2.append(i[0]*arr[0]+i[1]*arr[1]+i[2]*arr[2])
    return(arr2)

def vect_sub(a,b):
    ans=[]
    for i in range(len(a)):
        ans.append(a[i]-b[i])
    return(ans)

def linear_transform(points,shift):
    ans=[]
    for i in points:
        ans.append([i[j]+shift[j] for j in range(3)])
    return(ans)

# produce 3d rotation matrix to transform to absolute place (but doesn't not find transformation of origin)

# load all relative beacon locations into a 3d array.
# points[i][j][k] - i: scanner no., j: jth beacon, k: x,y,z coord
file = open('./input.txt', 'r')
points=[]
file.readline().strip()
line = file.readline().strip()
while line:
    scannerpoints = []
    while line:
        scannerpoints.append([int(i) for i in line.split(",")])
        line = file.readline().strip()
    points.append(scannerpoints)
    file.readline().strip()
    line = file.readline().strip() #take out scanner header

# # find lengths between all combinations of points for each scanner
# # magvals[i] has 2d magnitude matrix for ith scanner
magvals = []
for i in range(len(points)):
    temp=[]
    for j in points[i]:
        temp.append([magnitude(j,k) for k in points[i]])
    magvals.append(temp)

# find all pairs of scanners with at least 12 shared points
sharedscans=[]
for i in range(len(magvals)):
    for j in range(i+1,len(magvals)):
        added=False
        for x in magvals[i]:
            for y in magvals[j]:
                # print(same_vals(x,y))
                if same_vals(x,y)>11:
                    sharedscans.append((i,j))
                    added=True
                    break
            if added:
                break

vectors=[]
for i in sharedscans:
    for x in range(len(magvals[i[0]])):
        added=False
        for y in range(len(magvals[i[1]])):
            if same_vals(magvals[i[0]][x],magvals[i[1]][y])>11:
                # x and y now belong to the same point
                # let's pull out an identical vector
                for z in range(len(magvals[i[0]][x])):
                    
                    if magvals[i[0]][x][z]==0:
                        continue
                    
                    # funky orthogonality requirements. hackier workarounds but let's stay safe for now
                    if magvals[i[0]][x][z] in magvals[i[1]][y]:
                        x0 = points[i[0]][x]
                        x1 = points[i[0]][z]
                        x2 = points[i[1]][y]
                        x3 = points[i[1]][magvals[i[1]][y].index(magvals[i[0]][x][z])]
                        if 0 in vect_sub(x1,x0) or 0 in vect_sub(x3,x2):
                            continue
                        # (x,z) is same vector as (y,magvals[i[1]][x].index(magvals[i[0]][x][z]))
                        vectors.append(((x,z),(y,magvals[i[1]][y].index(magvals[i[0]][x][z]))))
                        break

                # just cutting things a bit short once 
                added=True
                break
        if added:
            break



sharedscans += [i[::-1] for i in sharedscans] # adds reversed tupled in sharedscans, to sharedscans
vectors += [i[::-1] for i in vectors]
# create a dictionary to store absolute values of points
# note that order of points in absolutepoints[i] is same as points[i]
absolutepoints={}
absolutepoints[0]=points[0]
absolutesensors={}
absolutesensors[0]=[0,0,0]
while len(absolutepoints)<len(points):
    for i in range(len(sharedscans)):
        if sharedscans[i][0] not in absolutepoints or sharedscans[i][1] in absolutepoints:
            continue
        print(sharedscans[i])
        # sharedscans[i] #tells us which scanners we're using. Imagine (0,1) for example.
        # x1-x0 is vector for reference. Will do something to make sure only works for scanners whose absolute values have already been found
        #  note that x2 is just x0 in a different reference frame.
        x0 = absolutepoints[sharedscans[i][0]][vectors[i][0][0]]
        x1 = absolutepoints[sharedscans[i][0]][vectors[i][0][1]]
        x2 = points[sharedscans[i][1]][vectors[i][1][0]]
        x3 = points[sharedscans[i][1]][vectors[i][1][1]]
        
        matrix = find_rotation(vect_sub(x1,x0),vect_sub(x3,x2))
        # print(matrix)
        rotated = [matrix_mult(matrix,j) for j in points[sharedscans[i][1]]] # points after rotating sensor to same way as sensor 0
        # linear tranformation to x ref. shift by adding x0-x2' (with x2' being x2 rotated to sensor0 orientation)
        x2_rot = matrix_mult(matrix,x2)
        
        absolute_sensor = [ x0[i]-x2_rot[i] for i in range(3)]
        absolutesensors[sharedscans[i][1]]=absolute_sensor
        absolutepoints[sharedscans[i][1]] = linear_transform(rotated,absolute_sensor)


def manhatten(a,b):
    return(sum([abs(a[i]-b[i]) for i in range(3)]))

maximum=0
for i in absolutesensors:
    for j in absolutesensors:
        maximum=max(maximum,manhatten(absolutesensors[i],absolutesensors[j]))

print(maximum)
    




