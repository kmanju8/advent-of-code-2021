def decode(arr,i,j,algo):
    if i==0 or j==0 or i==len(arr)-1 or j==len(arr)-1:
        return('1' if arr[i][j]=='0' else '0') #specific to input data, but quick and easy solution
    binary = arr[i-1][j-1:j+2]+arr[i][j-1:j+2]+arr[i+1][j-1:j+2]
    return(algo[int(binary,2)])
    
def enhance(arr, banding, algo):
    arr2 = [banding*(len(arr)+2)]

    for i in range(len(arr)):
        temp=banding
        for j in range(len(arr)):
            temp+=decode(arr,i,j,algo)
        temp+=banding
        arr2.append(temp)

    arr2.append(banding*(len(arr)+2))
    
    return(arr2)


file = open('./input.txt', 'r')
algo = file.readline().strip().replace('#','1').replace('.','0')
file.readline().strip()

# load up low res image
line = file.readline().strip()
arr=['0'*(len(line)+4)]
arr.append('0'*(len(arr[0])))
while line:
    arr.append('00'+line.replace('#','1').replace('.','0')+'00')
    line = file.readline().strip()
arr.append('0'*(len(arr[0])))
arr.append('0'*(len(arr[0])))

# this problem is trying to be clever: making algo[0]=# so the infinite grid becomes ones.
# get around this by banding with 1s after first enhance, 3rd enhance, 5th etc...
# after initial banding of two layers, only one layer is needed for each subsequent banding

for i in range(50):
    arr=enhance(arr,str((i+1)%2),algo)

count=0
for i in arr:
    for j in i:
        count += 1 if j=='1' else 0
print(count)