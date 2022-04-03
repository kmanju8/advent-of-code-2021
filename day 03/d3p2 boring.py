oxy = [i[:-1] for i in open('input.txt')]
co2 = [i[:-1] for i in open('input.txt')]

def binary_to_int(bin):
    ans = 0
    for i in bin:
        ans = ans << 1
        if i ==  "1":
            ans+=1
    return ans

def most_common(arr, x):
    return "0" if ((len([y[x] for y in arr if y[x]=="1"])/len(arr))<0.5) else "1"

for i in range(12): 
    oxym = most_common(oxy, i)
    if len(oxy)!=1:
        oxy = [x for x in oxy if x[i]==oxym]

    co2l = str(abs(int(most_common(co2, i))-1))
    if len(co2)!=1:
        co2 = [x for x in co2 if x[i]==co2l]


print(binary_to_int(oxy[0]) * binary_to_int(co2[0]))