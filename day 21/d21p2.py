# using recursion.
# mixing with dynamic programming would be a more efficient method but requires more
# thought in the order of solving. May consider on a rewrite.

def roll(p1,p2,score1,score2,turnone,dist):
    if score1>20:
        return(1)
    elif score2>20:
        return(0)
    else:
        temp=0
        # if player 1's turn
        if turnone:
            for i in range(7):
                temp+=dist[i]*roll((p1+i+3)%10,p2,score1+(p1+i+3)%10+1,score2,False,dist)
            return(temp)
        # if player 2's turn
        else:
            for i in range(7):
                temp+=dist[i]*roll(p1,(p2+i+3)%10,score1,score2+(p2+i+3)%10+1,True,dist)
            return(temp)

# rewrite board locations as 0-9, over 1-10 (nicer for modular)
p1 = 8-1
p2 = 4-1
score1 = 0
score2 = 0
# every 3 die rolls branches into 27 paths.
# in one of these, total roll is 3, in 3 it is 4, in 6 it is 5, etc...
dist=(1,3,6,7,6,3,1)

print("P1 wins in: ", roll(p1,p2,score1,score2,True,dist))
# by symmetry
print("P2 wins in: ", roll(p2,p1,score1,score2,False,dist))
