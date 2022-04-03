def prod(arr):
    product=1
    for i in arr:
        product*=i
    return(product)

# handles operators
def operator(arr, type):
    match type:
        case 0:
            return(sum(arr))
        case 1:
            return(prod(arr))
        case 2:
            return(min(arr))
        case 3:
            return(max(arr))
        case 5:
            return(1 if arr[0]>arr[1] else 0)
        case 6:
            return(1 if arr[0]<arr[1] else 0)
        case 7:
            return(1 if arr[0]==arr[1] else 0)

# get index of next bit after literal package
def literal(bin,i):
    val=""
    ongoing="1"
    while ongoing=="1":
        ongoing=bin[i]
        val+=bin[i+1:i+5]
        i+=5
    return(int(val,2), i)

# traverse packet starting at index i.
# maybe should also return starting index of next packet
def traverse_packet(bin,i):
    if i+10>len(bin):
        return(0,2**15)

    type = int(bin[i+3:i+6],2)
    
    # handling literals
    if type == 4:
        return(literal(bin,i+6))

    else:
        # goes over n bits of packages
        if bin[i+6]=="0":
            # length=bin[i+7:i+22], so i+22 is start of args
            k=i+22
            temp=[]
            while k<(i+22+int(bin[i+7:i+22],2)):
                toadd, k = traverse_packet(bin,k)
                temp.append(toadd)
            return(operator(temp,type),k)
        # iterates over n subpackets
        else:
            k=i+18
            temp=[]
            for _ in range(int(bin[i+7:i+18],2)):
                toadd, k = traverse_packet(bin,k)
                temp.append(toadd)
            return(operator(temp,type),k)
    
# inputs 6+ are tests for part 2
hex = [i[:-1] for i in open('input.txt')][0]
bin = bin(int(hex, 16))[2:].zfill(4*len(hex))

total=traverse_packet(bin, 0)
print(total[0])