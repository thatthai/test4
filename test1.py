print("Hello")
print("How อายุ")
print("i'm ฟาย")
print("^^")
print("อามัดมีชู้")
print("Really?")
print("จริงครับ มีตั้ง20คน")
print("ใช่ป่าว พูดถึงตัวเองรึป่าวคับคุณ")

import random


def play():
    if scorecom == scoreplayer:
        rusult = "tie"
    elif scorecom > scoreplayer:
        rusult = "you lose"
    elif scorecom < scoreplayer :
        rusult = "you win"
    print(" ")
    print("         ************************")
    print(" ")
    print("         --------- %s ---------" %rusult)
    print(" ")
    print("         ************************")


card = ("A[S]","2[S]","3[S]","4[S]","5[S]","6[S]","7[S]","8[S]","9[S]","10[S]","J[S]","Q[S]","K[S]"
           ,"A[H]","2[H]","3[H]","4[H]","5[H]","6[H]","7[H]","8[H]","9[H]","10[H]","J[H]","Q[H]","K[H]"
           ,"A[D]","2[D]","3[D]","4[D]","5[D]","6[D]","7[D]","8[D]","9[D]","10[D]","J[D]","Q[D]","K[D]"
           ,"A[C]","2[C]","3[C]","4[C]","5[C]","6[C]","7[C]","8[C]","9[C]","10[C]","J[C]","Q[C]","K[C]")
i = random.randrange(len(card))
computer1 = card[i]
    
k = random.randrange(len(card))
player1 = card[k]
    
while True:
    if player1 == computer1:
        k = random.randrange(len(card))
        player1 = card[k]
    else:
        break

j = random.randrange(len(card))
computer2 = card[j]
while True:
    if player1 == computer2 or computer2 == computer1:
        j = random.randrange(len(card))
        computer2 = card[j]
    else:
        break
    
l = random.randrange(len(card))
player2 = card[l]
while True:
    if player2 == computer2 or player2 == computer1 or player2 == player1 :
        l = random.randrange(len(card))
        player2 = card[l]
    else:
        break
i = i + 1
j = j + 1 
k = k + 1
l = l + 1

while True:
    if i > 13 :
        i = i - 13
    else:
        break

while True:
    if j > 13 :
        j = j - 13
    else:
        break

while True:
    if k > 13 :
        k = k - 13
    else:
        break

while True:
    if l > 13 :
        l = l - 13
    else:
        break



if i == 10 or i == 11 or i == 12 or i == 13 :
    i = 0 

if j == 10 or j == 11 or j == 12 or j == 13 :
    j = 0 

if k == 10 or k == 11 or k == 12 or k == 13 :
    k = 0 

if l == 10 or l == 11 or l == 12 or l == 13 :
    l = 0 

scorecom = i + j
if scorecom == 10:
    scorecom = 0
elif scorecom > 10 :
    scorecom = scorecom % 10

scoreplayer = k + l
if scoreplayer == 10:
    scoreplayer = 0
elif scoreplayer > 10 :
    scoreplayer = scoreplayer % 10


print("My score : %d" %scoreplayer)
print("My cards   ->      %s      %s "%(player1 , player2))

print(" ")
deal = input("[1]Draw , [2] Check ->")


if deal == "2":
    if scorecom < 6 :
        y = random.randrange(len(card))
        computer3 = card[y]
        while True:
            if player2 == computer3 or computer3 == player1 or computer3 == computer2 or computer1 == computer3 :
                y = random.randrange(len(card))
                computer3 = card[y]
            else:
                break
        y = y + 1
        while True:
            if y > 13 :
                y = y - 13
            else:
                break
        if y == 10 or y == 11 or y == 12 or y == 13 :
            y  = 0 
    
        scorecom = i + j + y
        if scorecom == 10:
            scorecom = 0
        elif scorecom > 10 :
            scorecom = scorecom % 10

        print(" ")
        print("-------------------------------------------------")
        print("Computer score : %d" %scorecom)
        print("Computer cards   ->      %s      %s      %s" %(computer1 , computer2 , computer3))
        print("-------------------------------------------------")
    
    else :
        print(" ")
        print("-------------------------------------------------")
        print("Computer score : %d" %scorecom)
        print("Computer cards   ->      %s      %s " %(computer1 , computer2 ))
        print("-------------------------------------------------")
    play()

elif deal == "1":
    m = random.randrange(len(card))
    player3 = card[m]
    while True:
        if player3 == computer2 or player3 == computer1 or player3 == player1 or player3 == player2 :
            m = random.randrange(len(card))
            player3 = card[m]
        else:
            break

    if scorecom < 6 :
        y = random.randrange(len(card))
        computer3 = card[y]
        while True:
            if player3 == computer3 or player2 == computer3 or computer3 == player1 or computer3 == computer2 or computer1 == computer3 :
                y = random.randrange(len(card))
                computer3 = card[y]
            else:
                break
        y = y + 1
        while True:
            if y > 13 :
                y = y - 13
            else:
                break
        if y == 10 or y == 11 or y == 12 or y == 13 :
            y  = 0 
    
        scorecom = i + j + y
        if scorecom == 10:
            scorecom = 0
        elif scorecom > 10 :
            scorecom = scorecom % 10

        print(" ")
        print("-------------------------------------------------")
        print("Computer score : %d" %scorecom)
        print("Computer cards   ->      %s      %s      %s" %(computer1 , computer2 , computer3))
        print("-------------------------------------------------")
    
    else :
        print(" ")
        print("-------------------------------------------------")
        print("Computer score : %d" %scorecom)
        print("Computer cards   ->      %s      %s " %(computer1 , computer2 ))
        print("-------------------------------------------------")
    
    m = m + 1
    while True:
            if m > 13 :
                m = m - 13
            else:
                break
    if m == 10 or m == 11 or m == 12 or m == 13 :
        m  = 0 

    
    scoreplayer = k + l + m
    if scoreplayer == 10:
        scoreplayer = 0
    elif scoreplayer > 10 :
        scoreplayer = scoreplayer % 10
    
    

    print(" ")
    print("My score : %d" %scoreplayer)
    print("My cards   ->      %s      %s      %s"%(player1 , player2 , player3))
    print(" ")
    play()




