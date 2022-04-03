# get index of next bit after literal package
def literal(bin,i):
    # val=""
    ongoing="1"
    while ongoing=="1":
        ongoing=bin[i]
        # val+=bin[i+1:i+5]
        i+=5
    return(i)

# traverse packet starting at index i.
# maybe should also return starting index of next packet
def traverse_packet(bin,i):
    if i+10>len(bin):
        return(0,2**15)

    version = int(bin[i:i+3],2)
    type = int(bin[i+3:i+6],2)
    total=version
    
    # handling literals
    if type == 4:
        return(total, literal(bin,i+6))

    else:
        # goes over n bits of packages
        if bin[i+6]=="0":
            k=i+22
            while k<(i+22+int(bin[i+7:i+22],2)):
                toadd, k = traverse_packet(bin,k)
                total += toadd
            return(total,k)
        # iterates over n subpackets
        else:
            k=i+18
            for _ in range(int(bin[i+7:i+18],2)):
                toadd, k = traverse_packet(bin,k)
                total+=toadd
            return(total,k)
    
# I'm definitely vibing where part two is going, so will try and code such that I can easily mod.
hex = [i[:-1] for i in open('input.txt')][0]
bin = bin(int(hex, 16))[2:].zfill(4*len(hex))

total=traverse_packet(bin, 0)
print(total)
    
# set to first index of next packet
# if type 4, no length type id, just try to move past this block to next
# if anything else, is operator, so needs length string to say how much stuff is in it.