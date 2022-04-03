# rewrite board locations as 0-9, over 1-10 (nicer for modular)
p1 = 8 -1
p2 = 4 -1
score1 = 0
score2 = 0
dice=0

while score1 < 1000 and score2 <1000:
    for i in range(3):
        p1 = (p1 + (dice%100+1))%10
        dice += 1
    score1 += p1 + 1

    if score1>=1000:
        break
    
    for i in range(3):
        p2 = (p2 + (dice%100+1))%10
        dice += 1
    score2 += p2 + 1
    
loser = min(score1,score2)
print(dice * loser)